import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re # regular expression

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

# box chart with x = accomodation_type y=accomodation_cost
# for accomodation_type in df['Accommodation type'].unique():
#     data = df[df['Accommodation type'] == accomodation_type]['Accommodation cost']
#     print(data)
    # plt.boxplot(df[df['Accommodation type'] == accomodation_type]['Accommodation cost'], positions=[accomodation_type])
labels = df['Accommodation type'].unique()
    
all_data = [df[df['Accommodation type'] == accomodation_type]['Accommodation cost'] for accomodation_type in labels]

plt.boxplot(all_data, labels=labels)

plt.xlabel('Accommodation Type')
plt.ylabel('Accommodation Cost')

plt.show()