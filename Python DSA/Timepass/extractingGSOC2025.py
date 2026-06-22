import json
import csv

# Load JSON files
with open('gsoc25.json', "r", encoding="utf-8") as file:
    data25 = json.load(file)
with open('gsoc24.json', "r", encoding="utf-8") as file:
    data24 = json.load(file)

# Extract organization names from 2024 data
organisationNames24 = set(org["name"] for org in data24)

# Find new organizations in 2025
newOrgs = []
for org in data25:
    if org["name"] not in organisationNames24:
        newOrgs.append({
            "name": org["name"],
            "website_url": org["website_url"],
            "gsoc_url": f"https://summerofcode.withgoogle.com/programs/2025/organizations/{org['slug']}"
        })

# Save data to CSV file
csv_filename = "new_orgs.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "website_url", "gsoc_url"])
    writer.writeheader()  # Write column names
    writer.writerows(newOrgs)  # Write data

print("-" * 20)
print("No. of orgs found in 2024:", len(organisationNames24))
print("-" * 20)
print("No. of new orgs found:", len(newOrgs))
print("-" * 20)
print(f"Data has been saved to {csv_filename}")
