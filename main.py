from scraper import fetch_jobs
from cleaner import filter_jobs
from storage import save_jobs
def main():
    print("\n===== JobPulse Automation Started =====\n")

    jobs = fetch_jobs()

    if not jobs:
        print("No jobs found")
        return

    filtered_jobs = filter_jobs(jobs)

    if not filtered_jobs:
        print("No matching jobs found")
        return

    save_jobs(filtered_jobs)

    print("\n===== Automation Completed Successfully =====\n")


if __name__ == "__main__":
    main()
