import pandas as pd
import matplotlib.pyplot as plt
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

def show_chart_1():
    """Number of trips per Destination Chart"""
    # Count the number of trips per destination
    trips_per_destination = df['Destination'].value_counts()
    
    plt.bar(x=trips_per_destination.index, height=trips_per_destination.values)
    plt.xlabel('Destination')
    plt.ylabel('Number of Trips')
    plt.xticks(rotation=360-90)

    plt.show()
    return True

# Accomodation type distribution
def show_chart_2():
    """Accomodation type distribution"""
    trips_per_accommodation_type = df['Accommodation type'].value_counts()
    
    plt.pie(x=trips_per_accommodation_type.values, labels=trips_per_accommodation_type.index, autopct='%1.1f%%')
    plt.title('Accommodation Type Distribution')
    plt.show()
    return True

# Number of trips per month
def show_chart_3():
    """Number of trips per month"""
    # Convert start date to datetime
    df['Start date'] = pd.to_datetime(df['Start date'])

    # Group the trips by month
    trips_per_month = df.groupby(df['Start date'].dt.strftime('%Y-%m'))['Trip ID'].count()
    
    plt.plot(trips_per_month.index, trips_per_month.values)
    plt.xlabel('Month')
    plt.ylabel('Number of Trips')
    plt.xticks(rotation=360-90)
    plt.show()
    return True

# Travel Nationalist
def show_chart_4():
    """Travel Nationalist"""
    nationalities = df['Traveler nationality'].value_counts()
    plt.bar(x=nationalities.index, height=nationalities.values)
    plt.xlabel("Country")
    plt.ylabel("Number of Trips")
    plt.xticks(rotation=360-90)
    plt.show()
    return True

# Trip Duration and Accommodation Cost by Destination
def show_chart_5():
    """Trip Duration and Accommodation Cost by Destination"""
    # plt.figure(figsize=(10, 5))
    
    # box chart with x = accomodation_type y=accomodation_cost
    for accomodation_type in df['Accommodation type'].unique():
        plt.boxplot(df[df['Accommodation type'] == accomodation_type]['Accommodation cost'], positions=[accomodation_type])
        
    plt.xlabel('Accommodation Type')
    plt.ylabel('Accommodation Cost')
    
    plt.show()
        
    return True
