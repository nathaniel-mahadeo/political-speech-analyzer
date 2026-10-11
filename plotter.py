#!/usr/bin/env python3

# plotter.py

import matplotlib.pyplot as plt


def plot_issue_counts(issue_counts: dict[str, int]) -> None:
    """Create a bar chart of issue keyword counts."""
    labels = list(issue_counts.keys())
    values = list(issue_counts.values())

    plt.figure(figsize=(10, 5))
    plt.bar(labels, values)
    plt.title("Issue Keyword Frequency in Speech")
    plt.xlabel("Issue")
    plt.ylabel("Count")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()


def plot_top_words(top_words: list[tuple[str, int]]) -> None:
    """Create a bar chart of the most frequent words."""
    labels = [word for word, _ in top_words]
    values = [count for _, count in top_words]

    plt.figure(figsize=(10, 5))
    plt.bar(labels, values)
    plt.title("Top Words in Speech")
    plt.xlabel("Word")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()


def plot_sentiment(sentiment: dict[str, float]) -> None:
    """Create a simple positive vs. negative sentiment chart."""
    labels = ["Positive", "Negative"]
    values = [sentiment["positive_count"], sentiment["negative_count"]]

    plt.figure(figsize=(6, 5))
    plt.bar(labels, values)
    plt.title("Sentiment Word Counts")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.tight_layout()


def show_plots() -> None:
    plt.show()