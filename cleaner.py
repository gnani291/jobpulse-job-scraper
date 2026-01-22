import re
from config import KEYWORDS


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9 ]", "", text)
    return text.strip()


def filter_jobs(jobs):
    filtered = []

    for job in jobs:
        title = clean_text(job["title"])

        for keyword in KEYWORDS:
            if keyword in title:
                filtered.append(job)
                break

    print(f"Filtered to {len(filtered)} relevant jobs")
    return filtered
