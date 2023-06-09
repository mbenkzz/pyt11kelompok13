import pandas as pd
import matplotlib.pyplot as plt
import re # regular expression

df = pd.read_csv('./csv/Travel details dataset.csv')

# drop the rows with missing values
df = df.dropna()

# [OPTIONAL] pick country name only after the comma
df['Destination'] = df['Destination'].apply(lambda x: x.split(', ')[1] if ',' in x else x) 

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
    
    # create smaller figure
    fig, ax = plt.subplots(figsize=(6, 3))
    
    ax.bar(x=trips_per_destination.index, height=trips_per_destination.values)
    fig.subplots_adjust(bottom=0.3)
    # plt.bar(x=trips_per_destination.index, height=trips_per_destination.values)
    plt.xlabel('Tujuan Wisata')
    plt.ylabel('Jumlah')
    plt.xticks(rotation=360-90)

    plt.show()

# Accomodation type distribution
def show_chart_2():
    """Accomodation type distribution"""
    trips_per_accommodation_type = df['Accommodation type'].value_counts()
    
    plt.pie(x=trips_per_accommodation_type.values, labels=trips_per_accommodation_type.index, autopct='%1.1f%%')
    plt.title('Tipe Akomodasi')
    
    plt.show()

# Number of trips per month
def show_chart_3():
    """Number of trips per month"""
    # Give choice to user to select month or year
    print('Pilih periode')
    print('1. Bulan (M)')
    print('2. Tahun (Y)')
    inp = ''
    while inp.upper() != 'M' and inp.upper() != 'Y':
        inp = input('Periode (M/Y) : ')
        if inp.upper() == 'M' or inp.upper() == 'Y':
            break
        else:
            print('Tolong masukkan huruf M atau Y')
        
    # Convert start date to datetime
    df['Start date'] = pd.to_datetime(df['Start date'])
    
    # Group the trips by month
    if inp.upper() == 'M':
        trips_per_month = df.groupby(df['Start date'].dt.strftime('%Y-%m'))['Trip ID'].count()
    else:
        trips_per_month = df.groupby(df['Start date'].dt.strftime('%Y'))['Trip ID'].count()
    
    fig, ax = plt.subplots(figsize=(10, 5))
    # need more space because of the month labels longer than year labels
    if inp.upper() == 'M':
        fig.subplots_adjust(bottom=.15)
        plt.plot(trips_per_month.index, trips_per_month.values)
        plt.xticks(rotation=360-90)
        plt.xlabel('Bulan')
    if inp.upper() == 'Y':
        plt.bar(x=trips_per_month.index, height=trips_per_month.values)
        plt.xlabel('Tahun')
    
    plt.ylabel('Jumlah')
    
    plt.show()

# Travel Nationalist
def show_chart_4():
    """Travel Nationalist"""
    nationalities = df['Traveler nationality'].value_counts()
    
    fig, ax = plt.subplots(figsize=(10, 5))
    fig.subplots_adjust(bottom=.25)
    
    plt.bar(x=nationalities.index, height=nationalities.values)
    plt.xlabel("Negara asal wisatawan")
    plt.ylabel("Jumlah")
    plt.xticks(rotation=360-90)
    
    plt.show()

# Transportation cost by Accomodation type
def show_chart_5():
    """Transportation cost by Accomodation type"""
    
    # box chart with x = accomodation_type y=accomodation_cost
    labels = df['Accommodation type'].unique()
    
    all_data = [df[df['Accommodation type'] == accomodation_type]['Transportation cost'] for accomodation_type in labels]
    plt.boxplot(all_data, labels=labels)
    
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "${:,}".format(int(x))))
        
    plt.xlabel('Tipe Akomodasi')
    plt.ylabel('Biaya Transportasi')
    plt.title('Biaya Transportasi Berdasarkan Tipe Akomodasi')
    
    plt.show()

def show_chart_6():
    """Number of Trips per Gender"""
    gender_counts = df['Traveler gender'].value_counts()
    
    fig, ax = plt.subplots(figsize=(6, 3))
    
    labels_name = {'Male': 'Laki Laki', 'Female': 'Perempuan'} # translation purpose
    labels_color = {'Male': '#3258a8', 'Female': '#f59dd0'} # blue and pink
    label = gender_counts.index.map(lambda x: labels_name[x])
    colors = gender_counts.index.map(lambda x: labels_color[x])
    
    plt.pie(x=gender_counts.values, labels=label, autopct='%1.1f%%', colors=colors)
    plt.title('Data Wisatawan Berdasarkan Jenis Kelamin')
    
    plt.show()
    
