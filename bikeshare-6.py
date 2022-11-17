import numpy as np
import pandas as pd
import time


CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}

cities = ('chicago', 'new york city', 'washington')
months = ['january', 'febuary', 'march', 'april', 'may', 'june', 'all']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Getting the user to select the city
    while True:
        city = input(
            "Please choose the city you are visiting! (Chicago, New York City, Washington)\n\n) : ").lower()
        if city in cities:
            print('Thank you, One moment please!')
            break
        else:
            print('Invalid City, Please try again.')
            continue

            # getting the user to select the month it currently is
    while True:
        month = input(
            "Almost done! Please select the month (january, febuary, march, april, may, june)\n\n) : ").lower()
        if month in months:
            print('Thank you, One moment please!')
            break
        else:
            print('Invalid Month, Please try again.')
            continue

            # getting the user to select the day
    while True:
        day = input('Last one! Please pick the Day. ').lower()
        if day in days:
            print('Thank you, One moment please!')
            break
        else:
            print('Invalid Day')
            continue

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
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.dayofweek
    df['Start Hour'] = df['Start Time'].dt.hour

    #filter by month if needed
    if month != 'all':
        month = months.index(month) + 1
        df = df[df['Month'] == month]

        # filter by day of week if needed
    if day != 'all':
        day = days.index(day)
        df = df[df['Day of Week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_popular_month = df['Month'].value_counts().idxmax()
    print("The most popular month is :", most_popular_month)

    # display the most common day of week
    most_popular_day_of_week = df['Day of Week'].value_counts().idxmax()
    print("The most popular day of week is :", most_popular_day_of_week)

    # display the most common start hour
    most_popular_start_hour = df['Start Hour'].value_counts().idxmax()
    print("The most popular start hour is :", most_popular_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # most commonly used start station
    most_used_start_station = df['Start Station'].value_counts().idxmax()
    print("The most used start station :", most_used_start_station)

    # most commonly used end station
    most_used_end_station = df['End Station'].value_counts().idxmax()
    print("The most used end station :", most_used_end_station)

    # the most common start and stop stations
    most_used_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most used start station and end station : {}, {}"\
            .format(most_used_start_end_station[0], most_used_start_end_station[1]))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel =  df['Trip Duration'].sum()
    print(total_travel)


    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print(mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The number of users in the data is: \n" + str(user_types))

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print("Counts of each gender: \n" + str(gender))

    
    
    if 'Birth Year' in df:
    # Display earliest, most recent, and most common year of birth
        the_birth_year = df['Birth Year']

    # the most common birth year
        the_most_common_year = the_birth_year.value_counts().idxmax()
        print("The most common birth year:", the_most_common_year)

    # the most recent birth year
        the_most_recent_year = the_birth_year.max()
        print("The most recent birth year:", the_most_recent_year)

    # the most earliest birth year
        the_most_earliest_year = the_birth_year.min()
        print("The most earliest birth year:", the_most_earliest_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(yz):
    i = 0
        
    while True:
        yes_or_no = input('Would you like to see 5 lines of Raw Data')
        if yes_or_no == 'yes':
            print('Thank you, one moment please')
            print(yz.iloc[i:i + 5])
            i = i + 5
        else:  
            break
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

