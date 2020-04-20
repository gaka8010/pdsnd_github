import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march','april','may','june','all']
days = ['all','monday','tuesday','wednesday','friday','saturday','sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input('choose city ').lower()
        if city in cities:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march','april','may','june','all']
    while True:
        month = input('choose month ').lower()
        if month in months:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all','monday','tuesday','wednesday','friday','saturday','sunday']
    while True:
        day = input('choose day of the week ').lower()
        if day in days:
            break

    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        month =  months.index(month) + 1
        df = df[ df['month'] == month ]
    if day != 'all':
        df = df[ df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("Most common month is :", most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("Most common day of the week is:",most_common_day_of_week)


    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("Most common start hour is :", most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mcuss = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station is:",mcuss)


    # TO DO: display most commonly used end station
    mcues = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station is:",mcues)


    # TO DO: display most frequent combination of start station and end station trip
    mfcses = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most frequeny combination of start station and end station : {} , {}".format(mfcses[0],mfcses[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    print("Counts of user types:",user_counts)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        counts_of_gender = df['Gender'].value_counts()
        print("Counts of gender:\n",counts_of_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birth_year = df['Birth Year']
        earliest_year = birth_year.min()
        print("The most earliest birth year:", earliest_year)
        most_recent = birth_year.max()
        print("The most recent birth year:", most_recent)
        most_common_year = birth_year.value_counts().idxmax()
        print("The most common birth year:", most_common_year)
  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """ displays raw data"""
    print('\nDisplay raw data:\n')
    start_loc = 0
    end_loc = 5

    display = input("Do you want to see raw data?: ").lower()
    if display == 'yes':
        while end_loc <= df.shape[0] - 1:
            print(df.iloc[start_loc:end_loc,:])
            start_loc += 5
            end_loc += 5
            end_display = input("Do you wish to continue?: ").lower()
            if end_display == 'no':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
