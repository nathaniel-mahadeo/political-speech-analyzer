#!/usr/bin/env python3

# constants.py

STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "if", "then", "so", "than",
    "to", "of", "in", "on", "for", "with", "by", "at", "from", "as",
    "is", "are", "was", "were", "be", "been", "being",
    "it", "its", "this", "that", "these", "those",
    "i", "me", "my", "we", "our", "ours", "you", "your", "yours",
    "he", "him", "his", "she", "her", "hers", "they", "them", "their",
    "what", "which", "who", "whom", "whose",
    "do", "does", "did", "doing", "have", "has", "had",
    "can", "could", "should", "would", "will", "shall", "may", "might",
    "not", "no", "nor", "too", "very", "just", "only", "also",
    "up", "down", "out", "over", "under", "again", "further",
    "here", "there", "when", "where", "why", "how",
    "all", "any", "both", "each", "few", "more", "most", "other", "some",
    "such", "own", "same", "s", "t", "don", "now",
    "us", "let", "lets", "mr", "speaker", "vice", "president",
    "applause", "nbsp", "br", "new", "years", "year", "time", "get", "make",
    "work", "need", "people", "tonight", "thats", "like", "must", "right",
    "even", "one", "every", "well"
}

ISSUES = {
    "economy": {
        "economy", "economic", "job", "jobs", "wage", "wages", "income",
        "growth", "business", "businesses", "manufacturing", "deficit",
        "debt", "tax", "taxes", "budget", "prosperity", "middle", "class",
        "worker", "workers"
    },
    "healthcare": {
        "health", "healthcare", "care", "medicare", "medical", "hospital",
        "hospitals", "insurance", "doctor", "doctors", "patient", "patients",
        "prescription", "drug", "drugs"
    },
    "education": {
        "education", "school", "schools", "student", "students", "college",
        "colleges", "teacher", "teachers", "preschool", "graduation",
        "curricula", "standards", "degree"
    },
    "energy_climate": {
        "energy", "oil", "gas", "renewable", "wind", "solar", "climate",
        "carbon", "pollution", "emissions", "science", "research",
        "drought", "wildfire", "flood"
    },
    "immigration": {
        "immigration", "immigrant", "immigrants", "border", "citizenship",
        "citizen", "citizens", "legal", "english"
    },
    "security_foreign_policy": {
        "war", "military", "security", "troop", "troops", "terrorist",
        "terrorists", "terrorism", "afghanistan", "iran", "north", "korea",
        "cyber", "defense", "missile", "weapon", "weapons", "allies"
    },
    "gun_violence_rights": {
        "gun", "guns", "violence", "vote", "voting", "rights", "freedom",
        "democracy", "background", "checks", "children"
    }
}

POSITIVE_WORDS = {
    "progress", "stronger", "confidence", "healing", "rebounding", "growth",
    "opportunity", "secure", "prosperity", "improve", "improving", "fair",
    "hope", "help", "better", "freedom", "peace", "innovation", "jobs",
    "support", "success", "strong", "protect", "reward", "encourage"
}

NEGATIVE_WORDS = {
    "crisis", "debt", "deficit", "cuts", "harsh", "bad", "worse", "burden",
    "struggling", "poverty", "violence", "war", "threat", "threats",
    "terrorist", "terrorists", "terrorism", "dangerous", "drought",
    "wildfire", "wildfires", "flood", "floods", "murdered", "killed",
    "gun", "guns", "crime", "recession", "unemployment", "hardship",
    "chaos", "attacks"
}