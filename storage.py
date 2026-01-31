import csv
import os
from config import DATA_FILE
def file_exists():
    return os.path.isfile(DATA_FILE)
def get_existing_links():
    links = set()

    if not file_exists():
        return links

    with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            links.add(row["link"])

    return links
def save_jobs(jobs):
    os.makedirs("data", exist_ok=True)

    existing_links = get_existing_links()
    new_jobs = []

    for job in jobs:
        if job["link"] not in existing_links:
            new_jobs.append(job)

    write_header = not file_exists()

    with open(DATA_FILE, "a", newline="", encoding="utf-8") as file:
        fieldnames = ["title", "company", "location", "link"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if write_header:
            writer.writeheader()

        for job in new_jobs:
            writer.writerow(job)

    print(f"Saved {len(new_jobs)} new jobs")
