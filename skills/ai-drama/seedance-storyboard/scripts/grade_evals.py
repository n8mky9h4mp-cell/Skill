#!/usr/bin/env python3
"""Grade seedance-storyboard eval outputs."""
import json
import re
import sys
from pathlib import Path


NEGATIVE_WORDS = ["严禁", "禁止", "不要", "绝不", "切勿"]


def extract_prompt_block(text: str) -> str:
    m = re.search(r"```(?:text)?\s*\n(.*?)```", text, re.DOTALL)
    return m.group(1).strip() if m else ""


def grade_output(content: str, eval_name: str) -> dict:
    prompt_block = extract_prompt_block(content)
    expectations = []

    # char limit
    char_count = len(prompt_block)
    passed_char = char_count <= 2000 if prompt_block else False
    expectations.append({
        "text": "最终提示词块字数 ≤ 2000",
        "passed": passed_char,
        "evidence": f"提示词块 {char_count} 字" if prompt_block else "未找到 ```text 提示词块"
    })

    # contains checks per eval
    checks = {
        "bamboo-portrait-9x16": [
            ("包含「画面无任何字幕」", "画面无任何字幕" in content),
            ("包含画幅 9:16", "9:16" in content),
            ("包含时长 5秒", "5秒" in content),
            ("使用镜头1/镜头2 编号格式", "镜头1" in content and "镜头2" in content),
        ],
        "cyberpunk-chase-16x9": [
            ("包含「画面无任何字幕」", "画面无任何字幕" in content),
            ("包含画幅 16:9", "16:9" in content),
            ("包含时长 12秒", "12秒" in content),
            ("包含对白「他们来了」或 {他们来了}", "他们来了" in content),
        ],
        "waterfall-doc-16x9": [
            ("包含「画面无任何字幕」", "画面无任何字幕" in content),
            ("包含画幅 16:9", "16:9" in content),
            ("包含时长 15秒", "15秒" in content),
            ("使用镜头编号格式（镜头1）", "镜头1" in content),
        ],
    }

    for text, passed in checks.get(eval_name, []):
        expectations.append({
            "text": text,
            "passed": passed,
            "evidence": "通过" if passed else "未在输出中找到"
        })

    # negative words - check prompt block primarily
    check_text = prompt_block or content
    found_neg = [w for w in NEGATIVE_WORDS if w in check_text]
    expectations.append({
        "text": "无严禁/禁止/不要等负面词",
        "passed": len(found_neg) == 0,
        "evidence": f"发现: {found_neg}" if found_neg else "无负面词"
    })

    passed_count = sum(1 for e in expectations if e["passed"])
    return {
        "expectations": expectations,
        "pass_rate": passed_count / len(expectations) if expectations else 0,
        "passed_count": passed_count,
        "total_count": len(expectations),
    }


def main():
    base = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("seedance-storyboard-workspace/iteration-1")
    for eval_dir in sorted(base.iterdir()):
        if not eval_dir.is_dir():
            continue
        eval_name = eval_dir.name
        for config in ("with_skill", "without_skill"):
            out_path = eval_dir / config / "outputs" / "output.md"
            if not out_path.exists():
                continue
            content = out_path.read_text(encoding="utf-8")
            result = grade_output(content, eval_name)
            grading_path = eval_dir / config / "grading.json"
            grading_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"{eval_name}/{config}: {result['passed_count']}/{result['total_count']}")


if __name__ == "__main__":
    main()
