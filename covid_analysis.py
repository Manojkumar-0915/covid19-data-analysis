import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (you can mention the source if needed)
# Example: df = pd.read_csv("covid_data.csv")  # Not provided here
# For demo, let's create some simple data
data = {
    'Country': ['USA', 'India', 'Brazil', 'Russia', 'UK'],
    'Confirmed': [30000000, 29000000, 17000000, 5000000, 4500000],
    'Deaths': [500000, 400000, 450000, 120000, 110000]
}

df = pd.DataFrame(data)

# Show basic info
print("Top 5 countries with confirmed COVID-19 cases:")
print(df)

# Plot bar chart
plt.figure(figsize=(10, 5))
plt.bar(df['Country'], df['Confirmed'], color='skyblue')
plt.title('COVID-19 Confirmed Cases by Country')
plt.xlabel('Country')
plt.ylabel('Confirmed Cases')
plt.savefig("covid_cases_chart.png") 
plt.show()
