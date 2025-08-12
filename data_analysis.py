# Life Expectancy Data Analysis
# Reads life-expectancy.csv and provides summary statistics and year-based analysis
# I added code to allow the user type the country to show minimum and maximum life expectancy for that country.

import csv


filename = "life-expectancy.csv"

# Get user input first
year_of_interest = int(input("Enter the year of interest: "))
country_of_interest = input("Enter the country of interest: ").strip()

# Variables to track overall min/max
overall_min = float('inf')
overall_max = float('-inf')
overall_min_country = ""
overall_min_year = 0
overall_max_country = ""
overall_max_year = 0

# Store all data for analysis
data = []

# Read and process data
with open(filename, "r", encoding="utf-8") as file:
    header = file.readline().strip().split(",")
    entity_idx = header.index("Entity")
    year_idx = header.index("Year")
    life_exp_idx = header.index("Life expectancy (years)")
    for line in file:
        parts = line.strip().split(",")
        if len(parts) < max(entity_idx, year_idx, life_exp_idx) + 1:
            continue
        country = parts[entity_idx]
        try:
            year = int(parts[year_idx])
            life_exp = float(parts[life_exp_idx])
        except ValueError:
            continue
        data.append({"country": country, "year": year, "life_exp": life_exp})
        if life_exp < overall_min:
            overall_min = life_exp
            overall_min_country = country
            overall_min_year = year
        if life_exp > overall_max:
            overall_max = life_exp
            overall_max_country = country
            overall_max_year = year

# Print overall min/max
print(f"\nThe year and country with the lowest life expectancy: {overall_min_year}, {overall_min_country} ({overall_min:.3f})")
print(f"The year and country with the highest life expectancy: {overall_max_year}, {overall_max_country} ({overall_max:.3f})\n")

# Year-based analysis
year_data = [row for row in data if row["year"] == year_of_interest]
if year_data:
    avg_life_exp = sum(row["life_exp"] for row in year_data) / len(year_data)
    max_row = max(year_data, key=lambda x: x["life_exp"])
    min_row = min(year_data, key=lambda x: x["life_exp"])
    print(f"\nFor the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was {avg_life_exp:.2f}")
    print(f"The max life expectancy was in {max_row['country']} with {max_row['life_exp']:.2f}")
    print(f"The min life expectancy was in {min_row['country']} with {min_row['life_exp']:.3f}")
else:
    print(f"No data found for the year {year_of_interest}.")

# Country-based analysis
country_data = [row for row in data if row["country"].lower() == country_of_interest.lower()]
if country_data:
    avg_country_life_exp = sum(row["life_exp"] for row in country_data) / len(country_data)
    max_country_row = max(country_data, key=lambda x: x["life_exp"])
    min_country_row = min(country_data, key=lambda x: x["life_exp"])
    print(f"\nFor {country_of_interest.capitalize()}:")
    print(f"The average life expectancy was {avg_country_life_exp:.2f}")
    print(f"The max life expectancy was {max_country_row['life_exp']:.2f} in {max_country_row['year']}")
    print(f"The min life expectancy was {min_country_row['life_exp']:.2f} in {min_country_row['year']}")
else:
    print(f"No data found for {country_of_interest}.")
