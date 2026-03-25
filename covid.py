import pandas as pd

# Load dataset
df = pd.read_csv("covid_19_data.csv")

# Show first rows
print("First 5 rows:")
print(df.head())

# Basic info
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Top 10 countries with highest confirmed cases
top_countries = df.groupby("Country/Region")["Confirmed"].max().sort_values(ascending=False).head(10)

print("\nTop 10 Countries by Confirmed Cases:")
print(top_countries)

# Total global cases
total_cases = df["Confirmed"].sum()
print("\nTotal Global Cases:", total_cases)
import matplotlib.pyplot as plt

top_countries.plot(kind='bar')
plt.title("Top 10 Countries COVID Cases")
plt.xlabel("Country")
plt.ylabel("Confirmed Cases")
plt.savefig("output.png")
plt.show()