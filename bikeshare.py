import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city you want to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get user input for city
    city = input("Please enter a city of choice to explore. Type 'chicago', 'new york city', 'washington': \n").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input("Please enter one of these cities. Type 'chicago', 'new york city', 'washington': \n").lower()

    # Get user input for month
    month = input("Please select a month of choice from January to June or 'all' to explore all months: \n").lower()
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while month not in months:
        month = input("Please enter a valid month or type 'all':\n").lower()

    # Get user input for day
    day = input("Please enter your favorite day of the week. Type the full name with no caps or 'all' for no filter: \n").lower()
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while day not in days:
        day = input("Please choose a valid day or 'all': \n").lower()
    print ('='*50)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    file_name = CITY_DATA[city]
    df = pd.read_csv(file_name)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['dow'] = df['Start Time'].dt.day_name()
    df["month"] = df['Start Time'].dt.month_name()

    df['dow'] = df['dow'].str.lower()
    df["month"] = df['month'].str.lower()

    if month != 'all':
        df = df.loc[df['month']== month,:]
    if day != 'all':
        df = df.loc[df['dow'] == day,:]

    return df

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Additional statistics calculations can be added here

    #print(f"This took {time.time()- start_time} seconds.")
    #print('=' * 50)

    # TO DO: display the most common month/
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    common_month = df['month'].mode()[0]
    MONTH_DATA  = {"January" : 1, "February" : 2, "March" :3, "April" :4, "May" : 5,
    "June": 6,"July" : 7, "August" : 8, "September": 9, "October": 10, "November": 11,
    "December": 12}

    for months in MONTH_DATA:
        if MONTH_DATA[months]==common_month:
            most_common_month = months.title()
            print(f"The month where the highest usage was recorded is: {most_common_month}")

        # TO DO: display the most common day of week
    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    common_day = df['day_of_week'].mode()[0]

        # TO DO: display the most common start hour
    df['hour']=pd.to_datetime(df['Start Time']).dt.hour
    common_hour = df['month'].mode()[0]
    print(f"The rush hour is: {common_hour}")
    print("\nThis took %s seconds." % round((time.time() - start_time), 4))
    print('='*50)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    common_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station is: {common_start_station}")

        # TO DO: display most commonly used end station

    common_end_station = df['End Station'].mode()[0]
    print(f"\nThe most commonly used end station is: {common_end_station}")

        # TO DO: display most frequent combination of start station and end station trip
    #modeStartStation = df['Start Station'].mode()[0]
    #modeEndStation = df['End Station'].mode()[0]
    frequent_combination = df['Start Station'] + ' to ' + df['End Station']
    modeComb = frequent_combination.mode()[0]
    print (f"\n The most popular trip is: {modeComb}")
    print("\nThis took %s seconds." % round((time.time() - start_time), 4))
    print('='*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # TO DO: display mean travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['travelTime'] = df['End Time'] - df['Start Time']

    totalTime = df['travelTime'].sum()
    meanTime = df['travelTime'].mean()

    '''Extract hours, minutes and seconds for clearere evaluation'''
    def to_days_hours_mins(Time):
        days = Time.days
        hours, remainder = divmod(Time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return days, hours,minutes, seconds

    tT_days, tT_hours, tT_mins, tT_secs = to_days_hours_mins(totalTime)
    mT_days, mT_hours, mT_mins, mT_secs = to_days_hours_mins(meanTime)

    print(f"The total travel time is:, {tT_days} days, {tT_hours} hours, {tT_mins} minutes and {tT_secs} seconds")
    print(f"The average travel time is:, {mT_days} days, {mT_hours} hours, {mT_mins} minutes and {mT_secs} seconds")
    print("\nThis took %s seconds." % round((time.time() - start_time), 4))
    print('='*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print(f"Count of user types:, {user_type_count}")

        # TO DO: Display counts of gender
    if city != 'washington':
            gender_count = df['Gender'].value_counts()
            print(f"Count of genders:, {gender_count}")

        # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year = df['Birth Year'].min()
    print(f"Earliest Birth Year of user is:, {round(earliest_year)}")
    recent_year = df['Birth Year'].max()
    print(f"Most recent Birth Year of user is:, {round(recent_year)}")
    most_common_year = df['Birth Year'].mode()
    print(f"Most common Birth Year is:', {round(most_common_year)}")
    print("\nThis took %s seconds." % round(time.time() - start_time, 4))
    print('='*40)

def raw_data(df, city):
    """Displays few data rows to the user"""
    row = 0
    while True:
        raw_data = input("Would you like to view some raw data? enter yes or no \n").lower()
        row = 0
        if raw_data == "yes":
            print (df.iloc[row:row+5])
            row +=5
        elif raw_data == "no":
            break
        else:
            print("Sorry! you have entered the wrong input, kindly try agaian")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
