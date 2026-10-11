#!/usr/bin/env python3

# analyzer.py

from collections import Counter
from constants import ISSUES, NEGATIVE_WORDS, POSITIVE_WORDS, STOPWORDS


def normalize_word(word: str) -> str:
    """Very simple stemming/normalization for common plural endings."""
    if word.endswith("ies") and len(word) > 4:
        return word[:-3] + "y"

    if word.endswith("es") and len(word) > 4:
        if word.endswith(("ses", "xes", "zes", "ches", "shes")):
            return word[:-2]

    if word.endswith("s") and len(word) > 4 and not word.endswith(("us", "ss")):
        return word[:-1]

    return word


def filter_words(words: list[str]) -> list[str]:
    """Remove stopwords and short words after normalizing."""
    filtered = []

    for word in words:
        word = normalize_word(word)

        if word not in STOPWORDS and len(word) > 2:
            filtered.append(word)

    return filtered


def build_frequency_table(words: list[str]) -> dict[str, int]:
    """Build word frequency table using a hash table/dictionary."""
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq


def top_n_words(freq_table: dict[str, int], n: int = 15) -> list[tuple[str, int]]:
    """Return the top n most frequent words."""
    return Counter(freq_table).most_common(n)


def count_issues(words: list[str]) -> dict[str, int]:
    """Count occurrences of words belonging to each issue category."""
    counts = {}

    for issue, keywords in ISSUES.items():
        counts[issue] = sum(1 for word in words if word in keywords)

    return counts


def compute_sentiment(words: list[str]) -> dict[str, float]:
    """Compute simple lexicon-based sentiment counts and score."""
    positive_count = 0
    negative_count = 0

    for word in words:
        if word in POSITIVE_WORDS:
            positive_count += 1
        elif word in NEGATIVE_WORDS:
            negative_count += 1

    total = positive_count + negative_count
    score = 0.0 if total == 0 else (positive_count - negative_count) / total

    return {
        "positive_count": positive_count,
        "negative_count": negative_count,
        "sentiment_score": score,
    }