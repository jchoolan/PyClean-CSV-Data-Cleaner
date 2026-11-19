import csv

# Input and output files
input_file = "messy_customers.csv"
output_file = "cleaned_customers.csv"

cleaned_data = []
seen_emails = set()

duplicates_removed = 0
missing_values = 0

# Step 1: Read the messy CSV
with open(input_file, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

# Step 2: Clean the data
for row in rows:
    name = row["Name"].strip().title()
    city = row["City"].strip().title()
    email = row["Email"].strip().lower()

    if not name or not city or not email:
        missing_values += 1

    # Keep rows without email; deduplicate only nonempty email addresses
    if email and email in seen_emails:
        duplicates_removed += 1
        continue

    if email:
        seen_emails.add(email)

    cleaned_data.append({
        "Name": name,
        "City": city,
        "Email": email
    })

# Step 3: Save the cleaned CSV
with open(output_file, "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "City", "Email"])
    writer.writeheader()
    writer.writerows(cleaned_data)

# Step 4: Display cleaning summary
print("=" * 40)
print("       PYCLEAN - CSV DATA CLEANER")
print("=" * 40)
print("Original records:", len(rows))
print("Duplicates removed:", duplicates_removed)
print("Cleaned records:", len(cleaned_data))
print("Rows with missing values:", missing_values)
print("=" * 40)
print("CSV cleaning completed successfully!")
print("Output saved to:", output_file)
