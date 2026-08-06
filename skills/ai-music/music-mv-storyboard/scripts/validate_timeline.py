#!/usr/bin/env python3
"""Validate an MV storyboard timeline stored as JSON."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def validate(data: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["根对象必须是 JSON object"]

    total = data.get("song_duration_sec")
    limit = data.get("max_clip_sec")
    segments = data.get("segments")

    if not is_int(total) or total <= 0:
        errors.append("song_duration_sec 必须是正整数")
    if not is_int(limit) or not 10 <= limit <= 15:
        errors.append("max_clip_sec 必须是 10–15 之间的整数")
    if not isinstance(segments, list) or not segments:
        errors.append("segments 必须是非空数组")
        return errors

    expected_start = 0
    duration_sum = 0

    for index, segment in enumerate(segments, start=1):
        label = f"segment {index}"
        if not isinstance(segment, dict):
            errors.append(f"{label} 必须是 object")
            continue

        start = segment.get("start_sec")
        end = segment.get("end_sec")
        duration = segment.get("duration_sec")
        if not all(is_int(value) for value in (start, end, duration)):
            errors.append(f"{label} 的 start_sec/end_sec/duration_sec 必须是整数")
            continue

        if duration <= 0:
            errors.append(f"{label} 的 duration_sec 必须大于 0")
        if is_int(limit) and duration > limit:
            errors.append(f"{label} 时长 {duration}s 超过上限 {limit}s")
        if start != expected_start:
            errors.append(f"{label} 应从 {expected_start}s 开始，实际为 {start}s")
        if end - start != duration:
            errors.append(f"{label} 的 end_sec-start_sec 与 duration_sec 不一致")

        expected_start = end
        duration_sum += duration

    if is_int(total):
        if expected_start != total:
            errors.append(f"时间轴终点 {expected_start}s 不等于歌曲总时长 {total}s")
        if duration_sum != total:
            errors.append(f"分段时长总和 {duration_sum}s 不等于歌曲总时长 {total}s")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("用法: python validate_timeline.py <timeline.json>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"读取失败: {exc}", file=sys.stderr)
        return 2

    errors = validate(data)
    if errors:
        print("校验失败:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("校验通过：时间轴连续，分段均为整数秒且未超过上限，总时长一致。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

