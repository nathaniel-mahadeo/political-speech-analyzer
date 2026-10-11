#!/usr/bin/env python3

# political_speech.py

import sys

from analyzer import (
    build_frequency_table,
    compute_sentiment,
    count_issues,
    filter_words,
    top_n_words,
)
from loader import load_speech, tokenize
from plotter import plot_issue_counts, plot_sentiment, plot_top_words, show_plots


def analyze_speech(path: str) -> None:
    speech = load_speech(path)

    title = speech.get("title", "Unknown Title")
    date = speech.get("date", "Unknown Date")
    transcript = speech.get("transcript", "")

    words = tokenize(transcript)
    filtered_words = filter_words(words)

    freq_table = build_frequency_table(filtered_words)
    most_common = top_n_words(freq_table, 15)
    issue_counts = count_issues(filtered_words)
    sentiment = compute_sentiment(filtered_words)

    print("=" * 60)
    print("POLITICAL SPEECH ANALYSIS")
    print("=" * 60)
    print(f"File:  {path}")
    print(f"Title: {title}")
    print(f"Date:  {date}")
    print(f"Total words (raw):      {len(words)}")
    print(f"Total words (filtered): {len(filtered_words)}")
    print()

    print("Top 15 most frequent words:")
    for word, count in most_common:
        print(f"{word:<15} {count}")
    print()

    print("Issue counts:")
    for issue, count in issue_counts.items():
        print(f"{issue:<25} {count}")
    print()

    print("Sentiment analysis:")
    print(f"Positive words:  {sentiment['positive_count']}")
    print(f"Negative words:  {sentiment['negative_count']}")
    print(f"Sentiment score: {sentiment['sentiment_score']:.3f}")
    print()

    plot_issue_counts(issue_counts)
    plot_top_words(most_common)
    plot_sentiment(sentiment)
    show_plots()


def main() -> None:
    path = "obama.json"

    if len(sys.argv) > 1:
        path = sys.argv[1]

    analyze_speech(path)


if __name__ == "__main__":
    main()