# DataCamp - Exploratory Data Analysis in Python
# 1.1. Getting to Know a Dataset - Initial exploration
# Print the first five rows of unemployment
print(unemployment.head())

# Print a summary of non-missing values and data types in the unemployment DataFrame
print(unemployment.info())

# Print summary statistics for numerical columns in unemployment
print(unemployment.describe())

# Count the values associated with each continent in unemployment
print(unemployment["continent"].value_counts())

# Import the required visualization libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Create a histogram of 2021 unemployment; show a full percent in each bin
sns.histplot(data=unemployment, x="2021", binwidth=1)
plt.show()

# 1.2. Getting to Know a Dataset - Data validation
# Update the data type of the 2019 column to a float
unemployment["2019"] = unemployment["2019"].astype(float)
# Print the dtypes to check your work
print(unemployment.dtypes)

# Define a Series describing whether each continent is outside of Oceania
not_oceania = ~unemployment["continent"].isin(["Oceania"])

# Print unemployment without records related to countries in Oceania
print(unemployment[not_oceania])

# Print the minimum and maximum unemployment rates during 2021
print(unemployment['2021'].min(), unemployment['2021'].max())

# Create a boxplot of 2021 unemployment rates, broken down by continent
sns.boxplot(data=unemployment, x='2021', y='continent')
plt.show()
# 1.3. Getting to Know a Dataset - Data summarization
# Print the mean and standard deviation of rates by year
print(unemployment.agg(['mean', 'std']))

# Print yearly mean and standard deviation grouped by continent
print(unemployment.groupby('continent').agg(['mean', 'std']))

continent_summary = unemployment.groupby("continent").agg(
    # Create the mean_rate_2021 column
    mean_rate_2021=("2021", "mean"),
    # Create the std_rate_2021 column
    std_rate_2021=("2021", "std")
)
print(continent_summary)

# Create a bar plot of continents and their average unemployment
sns.barplot(x="continent", y="2021", data=unemployment)
plt.show()

# 2.1. Getting to Know a Dataset - Addressing missing data
# 2.2. Getting to Know a Dataset - Converting and analyzing categorical data
# 2.3. Getting to Know a Dataset - Working with numeric data
# 2.4. Getting to Know a Dataset - Handling outliers

# 3.1. Relationships in Data - Patterns over time
# 3.2. Relationships in Data - Correlation
# 3.3. Relationships in Data - Factor relationships and distributions

# 4.1. Turning Exploratory Analysis into Action - Consideration for categorical data
# 4.2. Turning Exploratory Analysis into Action - Generating new features
# 4.3. Turning Exploratory Analysis into Action - Generating hypotheses
