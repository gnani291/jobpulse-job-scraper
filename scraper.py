import requests
from bs4 import BeautifulSoup
def fetch_jobs():
    print("Fetching job listings...")

    response = requests.get("https://realpython.github.io/fake-jobs/")

    if response.status_code != 200:
        print("Failed to fetch website")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    job_cards = soup.find_all("div", class_="card-content")

    jobs = []

    for job in job_cards:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()

        link_tag = job.find("a", text="Apply")
        link = link_tag["href"] if link_tag else "N/A"

        jobs.append({
            "title": title,
            "company": company,
            "location": location,
            "link": link
        })

    print(f"Scraped {len(jobs)} jobs")
    return jobs
