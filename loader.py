#!/usr/bin/env python3

# loader.py

import json
import re


def load_speech(path: str) -> dict:
    """Load one Miller Center JSON speech file."""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def strip_html(text: str) -> str:
    """Remove simple HTML tags and common entities."""
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("&nbsp;", " ")
    text = text.replace("&amp;", "&")
    text = text.replace("’", "'")
    text = text.replace("“", '"').replace("”", '"')
    text = text.replace("–", "-").replace("—", "-")
    text = text.replace("--", " ")
    return text


def tokenize(text: str) -> list[str]:
    """Convert text into lowercase alphabetic tokens."""
    cleaned = strip_html(text).lower()
    cleaned = cleaned.replace("'", "")
    return re.findall(r"[a-z]+", cleaned)