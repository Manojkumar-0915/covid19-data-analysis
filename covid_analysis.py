import pandas as pd
import matplotlib.pyplot as plt
# Load dataset from CSV file
df = pd.read_csv("/content/Covid 19.csv")
country_summary = df.groupby("Country")[["Cumulative_cases", "Cumulative_death"]].max().reset_index()

# Sort by confirmed cases (Top 10 countries)
top_countries = country_summary.sort_values(by="Cumulative_cases", ascending=False).head(10)

print("Top 10 countries with highest COVID-19 cases:")
print(top_countries)
print(" ")
# Convert to numeric and handle missing values
df["Cumulative_cases"] = pd.to_numeric(df["Cumulative_cases"], errors="coerce").fillna(0)
df["Cumulative_death"] = pd.to_numeric(df["Cumulative_death"], errors="coerce").fillna(0)

# --- Country-level Summary ---
country_summary = df.groupby("Country")[["Cumulative_cases", "Cumulative_death"]].max().reset_index()

# Sort and pick top 10 countries by confirmed cases
top_countries = country_summary.sort_values(by="Cumulative_cases", ascending=False).head(10)

# --- Plot 1: Confirmed Cases ---
plt.figure(figsize=(12,6))
plt.bar(top_countries["Country"], top_countries["Cumulative_cases"], color="skyblue")
plt.title("Top 10 Countries - COVID-19 Confirmed Cases")
plt.xlabel("Country")
plt.ylabel("Total Confirmed Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- Plot 2: Deaths ---
plt.figure(figsize=(12,6))
plt.bar(top_countries["Country"], top_countries["Cumulative_death"], color="salmon")
plt.title("Top 10 Countries - COVID-19 Deaths")
plt.xlabel("Country")
plt.ylabel("Total Deaths")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- Time Series Trend for Top 3 Countries ---
top3_countries = top_countries["Country"].head(3)  # Select top 3
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y", errors="coerce")
trend_data = df[df["Country"].isin(top3_countries)]

plt.figure(figsize=(14,7))
for country in top3_countries:  # Use top3_countries instead of top5_countries
    country_data = trend_data[trend_data["Country"] == country].sort_values("Date")
    plt.plot(country_data["Date"], country_data["Cumulative_cases"], label=country)

plt.title("COVID-19 Spread Over Time (Top 3 Countries)")
plt.xlabel("Date")
plt.ylabel("Cumulative Confirmed Cases")
plt.legend()
plt.tight_layout()
plt.show()
