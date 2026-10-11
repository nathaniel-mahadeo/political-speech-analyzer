#!/usr/bin/env python3

# political_speech_test.py

import unittest

from loader import strip_html, tokenize
from analyzer import (
    filter_words,
    build_frequency_table,
    count_issues,
    compute_sentiment,
    normalize_word,
)


class TestPoliticalSpeech(unittest.TestCase):
    def test_strip_html(self):
        text = "<br />Hello&nbsp;world<br />"
        cleaned = strip_html(text)
        self.assertNotIn("<br />", cleaned)
        self.assertNotIn("&nbsp;", cleaned)

    def test_tokenize(self):
        text = "Jobs, jobs, JOBS!"
        words = tokenize(text)
        self.assertEqual(words, ["jobs", "jobs", "jobs"])

    def test_normalize_word(self):
        self.assertEqual(normalize_word("parties"), "party")
        self.assertEqual(normalize_word("jobs"), "jobs")
        self.assertEqual(normalize_word("class"), "class")

    def test_filter_words(self):
        words = ["the", "economy", "is", "strong"]
        filtered = filter_words(words)
        self.assertIn("economy", filtered)
        self.assertIn("strong", filtered)
        self.assertNotIn("the", filtered)
        self.assertNotIn("is", filtered)

    def test_build_frequency_table(self):
        words = ["jobs", "growth", "jobs"]
        freq = build_frequency_table(words)
        self.assertEqual(freq["jobs"], 2)
        self.assertEqual(freq["growth"], 1)

    def test_count_issues(self):
        words = ["jobs", "tax", "medicare", "school", "war"]
        issues = count_issues(words)
        self.assertGreaterEqual(issues["economy"], 2)
        self.assertGreaterEqual(issues["healthcare"], 1)
        self.assertGreaterEqual(issues["education"], 1)
        self.assertGreaterEqual(issues["security_foreign_policy"], 1)

    def test_compute_sentiment(self):
        words = ["progress", "stronger", "crisis", "war"]
        sentiment = compute_sentiment(words)
        self.assertEqual(sentiment["positive_count"], 2)
        self.assertEqual(sentiment["negative_count"], 2)
        self.assertAlmostEqual(sentiment["sentiment_score"], 0.0, places=6)


if __name__ == "__main__":
    unittest.main()