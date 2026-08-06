import unittest

from validate_timeline import validate


class ValidateTimelineTests(unittest.TestCase):
    def test_accepts_continuous_timeline_at_limit(self):
        data = {
            "song_duration_sec": 30,
            "max_clip_sec": 10,
            "segments": [
                {"start_sec": 0, "end_sec": 10, "duration_sec": 10},
                {"start_sec": 10, "end_sec": 20, "duration_sec": 10},
                {"start_sec": 20, "end_sec": 30, "duration_sec": 10},
            ],
        }
        self.assertEqual(validate(data), [])

    def test_rejects_clip_over_user_limit(self):
        data = {
            "song_duration_sec": 21,
            "max_clip_sec": 10,
            "segments": [
                {"start_sec": 0, "end_sec": 11, "duration_sec": 11},
                {"start_sec": 11, "end_sec": 21, "duration_sec": 10},
            ],
        }
        self.assertTrue(any("超过上限" in error for error in validate(data)))

    def test_rejects_gap_and_wrong_total(self):
        data = {
            "song_duration_sec": 20,
            "max_clip_sec": 15,
            "segments": [
                {"start_sec": 0, "end_sec": 8, "duration_sec": 8},
                {"start_sec": 9, "end_sec": 18, "duration_sec": 9},
            ],
        }
        errors = validate(data)
        self.assertTrue(any("应从 8s 开始" in error for error in errors))
        self.assertTrue(any("不等于歌曲总时长" in error for error in errors))

    def test_rejects_non_integer_limit(self):
        data = {
            "song_duration_sec": 20,
            "max_clip_sec": 10.5,
            "segments": [
                {"start_sec": 0, "end_sec": 10, "duration_sec": 10},
                {"start_sec": 10, "end_sec": 20, "duration_sec": 10},
            ],
        }
        self.assertTrue(any("10–15" in error for error in validate(data)))


if __name__ == "__main__":
    unittest.main()

