import sqlite3
import requests
import csv
from bs4 import BeautifulSoup

# Step 1: Scrape Job Listings
url = "https://realpython.github.io/fake-jobs"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Step 2: Connect to SQLite Database
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# Step 3: Create Jobs Table (if not exists)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        job_title TEXT,
        company_name TEXT,
        location TEXT,
        job_description TEXT,
        application_link TEXT,
        UNIQUE(job_title, company_name, location)
    )
""")

# Step 4: Extract and Insert Job Data
jobs = soup.find_all("div", class_="card-content")

for job in jobs:
    title = job.find("h2", class_="title").text.strip() if job.find("h2", class_="title") else "N/A"
    company = job.find("h3", class_="company").text.strip() if job.find("h3", class_="company") else "N/A"
    location = job.find("p", class_="location").text.strip() if job.find("p", class_="location") else "N/A"
    description = job.find("div", class_="description")
    description = description.text.strip() if description else "No description available"
    apply_link = job.find("a", class_="apply")["href"] if job.find("a", class_="apply") else "No link available"

    cursor.execute("""
        INSERT OR IGNORE INTO jobs (job_title, company_name, location, job_description, application_link)
        VALUES (?, ?, ?, ?, ?)
    """, (title, company, location, description, apply_link))

conn.commit()

# Step 5: Filtering Jobs
def filter_jobs(filter_type, filter_value):
    query = f"SELECT * FROM jobs WHERE {filter_type} = ?"
    cursor.execute(query, (filter_value,))
    return cursor.fetchall()

# Step 6: Export Jobs to CSV
def export_to_csv(jobs, filename="filtered_jobs.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company Name", "Location", "Job Description", "Application Link"])
        writer.writerows(jobs)
    print(f"Filtered jobs exported to {filename}")

# Step 7: Ask User for Filtering
filter_type = input("Filter by (company_name/location): ").strip()
filter_value = input(f"Enter {filter_type}: ").strip()

filtered_jobs = filter_jobs(filter_type, filter_value)

if filtered_jobs:
    export_to_csv(filtered_jobs)
else:
    print("No matching job listings found.")

conn.close()
print("Job listings scraped and stored successfully.")
