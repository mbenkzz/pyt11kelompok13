import pandas as pd
import matplotlib.pyplot as plt
import re

# Load the dataset
df = pd.read_csv('./csv/Travel details dataset.csv')

# drop the rows with missing values
df = df.dropna()

# Convert the date columns to datetime
df['Start date']=pd.to_datetime(df['Start date'])
df['End date']=pd.to_datetime(df['End date'])

# Modify column for cost, format it into numerical values
# define a regular expression pattern to match numeric values
pattern = re.compile(r'\d+(,\d+)*\.?\d*')

# apply the regular expression pattern to the column and convert the resulting strings to numeric data type
df['Accommodation cost'] = df['Accommodation cost'].apply(lambda x: float(pattern.search(x).group().replace(',', '')) if pattern.search(x) else None)
df['Transportation cost'] = df['Transportation cost'].apply(lambda x: float(pattern.search(x).group().replace(',', '')) if pattern.search(x) else None)

# Count the number of trips per destination
trips_per_destination = df['Destination'].value_counts()

# Create a bar chart
plt.bar(x=trips_per_destination.index, height=trips_per_destination.values)
plt.xlabel('Destination')
plt.ylabel('Number of Trips')
plt.xticks(rotation=360-90)

plt.show()

# # Create a bar chart
# fig = px.bar(x=trips_per_destination.index, y=trips_per_destination.values,
#              labels={'x': 'Destination', 'y': 'Number of Trips'},
#              title='Number of Trips per Destination')
# fig.show()

# print(df.info())
# print(df.isna().sum())
# print(list(df['Accommodation cost'].head(20)))