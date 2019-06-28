import time
import pandas as pd
import numpy as np
from collections import Counter
from itertools import combinations
from datetime import datetime

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
    #city_list = [all, 'chicago', 'new york city', 'washington']

    cities = ['chicago','new york city','washington']
    months = ['january','february','march','april','may','june','all']
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    while True:
        try:
            city = cities.index(input('Enter city to analyze (all, Chicago, New York City or Washington?): ').lower())
            month = months.index(input('Enter month (e.g. all, january, february, march, april, may, june): ').lower())
            # get user input for day of week (all, monday, tuesday, ... sunday)
            day = days.index(input('Enter day(all, monday, tuesday, wednesday, thursday, friday, saturday, sunday): ').lower())
            return (cities[city], months[month], days[day])
        except ValueError:
            print('Invalid entry, please enter valid city, month or day')
        #return get_filters()
            print(get_filters())
    return city, month, day
print('-'*40)

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
    CITY_DATA = { 'chicago': 'chicago.csv',
                  'new york city': 'new_york_city.csv',
                  'washington': 'washington.csv' }

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    # filter by hour
    #if hour != 'all':
        # filter by hour create the new dataframe
    #    df = df[df['hour'] == hour]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    common_month = df['month'].mode()

    print('Most common Start month:', common_month)


    # TO DO: display the most common day of week

    common_day = df['day_of_week'].mode()

    print('Most common day of week:', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()

    print('Most Popular Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode() #[0]
    print('Most Popular common_start_station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode() #[0]
    print('Most Popular common_end_station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip

    trip_series = df["Start Station"].astype(str) + " to " + df["End Station"].astype(str)
    trip_series.describe()
    most_popular_trip = trip_series.describe()["top"]
    print(most_popular_trip)
    print('Most frequent combination of start/end station trip: ', most_popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print ('Total_travel_time: ', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Mean_travel_time: ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_types = df.groupby(['User Type']).count()
        print('user_types: ', user_types)
    except KeyError:
        print('User_Type Column is not available')
    # TO DO: Display counts of gender
    try:
        gender_count = df.groupby(['Gender']).count()
        print('Gender_count: ', gender_count)
    except KeyError:
        print('Gender Column is not available')

    # TO DO: Display earliest, most recent, and most common year of birth
    df['year'] = df['Start Time'].dt.year
    earliest_year = df['year'].min()
    most_recent_year = df['year'].max()
    most_common_year = df['year'].mode()

    print("\nearliest year of birth:", earliest_year)
    print("\nmost recent year of birth:", most_recent_year)
    print("\nmost common year of birth:", most_common_year)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

# Acknowledgements:
# I will to acknowledege Stack overflow where i took a number of ideas and codes and modified for my purpose
# Udacity students hub for reviewing and commenting on various aspects of this code 
