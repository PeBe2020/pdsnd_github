#%% Import Packages
import time
import datetime
import pandas as pd
import numpy as np

#%% Import Data
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#%% Function to get filters from user input
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
    # While loop to ensure valid user input or repeat input process.
    city = ''
    while city not in CITY_DATA.keys():
        # Infrom user what to do.
        print("\nPlease select the city you would like to know more about:\nType in the corresponding number or the name of the city.")
        print("\nPlease choose between:\n(1) Chicago \n(2) New York City\n(3) Washington")
        # Get user input (accepting city name or corresponding numbers).
        user_input = input()
        if user_input == '1':
            city = 'chicago'
        elif user_input == '2':
            city = 'new york city'
        elif user_input == '3':
             city = 'washington'
        else:
             # Convert user input into lowercase to accept not case sensitive inputs.
            city = user_input.lower()

        # If user input is not valid, inform user. Checking user input against CITY_DATA.keys().
        if city not in CITY_DATA.keys():
            print("\nYour input is not valid. Please enter a valid city name.")

    # If user input is valid, inform user which city has been selected.
    print("\n--> You have selected: {}.".format(city.upper()))

    # TO DO: get user input for month (all, january, february, ... , june).
    # While loop to ensure valid user input or repeat input process.
    month = ''
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        print("\nPlease specify if you want to explore the data for a specific month or view the data for all months.")
        print("\nIf you seek data for a specific month, please type in the name of the month ('January' to 'June').")
        print("\nIf you want to see the data for all month, please type 'all'.")
        # Convert user input into lowercase to accept not case sensitive intput.
        month = input().lower()

        # If user input is not valid, inform user
        if month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            print("\nYour input is not valid.")

    # If user input is valid, inform user which month has been selected.
    print("\n--> You have selected: {}.".format(month.upper()))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday).
    # While loop to ensure valid user input or repeat input process.
    day = ''
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        print("\nPlease specify if you want to explore the data for a specific day of the week or view the data for all days in a week.")
        print("\nIf you seek data for a specific day, please type in the name of the day ('Monday' to 'Sunday').")
        print("\nIf you want to see the data for all month, please type 'all'.")
       # Convert user input into lowercase to accept not case sensitive intput
        day = input().lower()

        # if user input is not valid, inform user
        if day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            print("\nYour input is not valid.")

    # If user input is valid, inform user which day has been selected
    print("\n--> You have selected: {}.".format(day.upper()))

    print('-'*40)
    # Return user input for city, month & day
    return city, month, day


#%% Function to load data from .csv
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
    # Load city data into pd.dataframe.
    df = pd.read_csv(CITY_DATA[city])

    # Create column with start time in pd.dataframe.
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Create column for month (extracted from df['Start Time']) (dtype: int).
    df['month'] = df['Start Time'].dt.month

    # Create column for day (extracted from df['Start Time']) (dtype: string).
    df['week_day'] = df['Start Time'].dt.weekday_name

    # Filter by month, if user choose to filter by a specific month.
    if month != 'all':
        # Create a list of month to "convert" user input (str) into corresponding month int value (e.g. 'January' = 1).
        month_to_int = ['january', 'february', 'march', 'april', 'may', 'june']
        # Get index from list month_to_int corresponding user input; add 1 to index value to get correct month int value.
        month = month_to_int.index(month) + 1

        # Filter by month if applicable.
        df = df[df['month'] == month]

    # Filter by day, if user choose to filter by a specific day of the week.
    if day != 'all':
        df = df[df['week_day'] == day.title()]

    # Return dataframe with relevant data filtered by user filter inputs.
    return df


#%% Function to calculate statistics for time, day, month.
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month.
    # Use mode() function on the month column to get the value that appears most often.
    # Converting mode() function result to int - 1 to select corresponding month as string from list.
    most_month = df['month'].mode()[0]
    temp_month = int(df['month'].mode()[0]) - 1
    int_to_month = ['january', 'february', 'march', 'april', 'may', 'june']
    # Display result for most common month as a string (e.g. 'January' instead of 1).
    print('The most common month is: ' + int_to_month[temp_month].upper() + '.')

    # TO DO: display the most common day of week
    # Use mode() function on the day column to get the value that appears most often.
    most_day = df['week_day'].mode()[0]
    print('The most common day of the week is: ' + str(most_day).upper() + '.')

    # TO DO: display the most common start hour
    # Extract hour from 'Start Time' & create new column.
    df['hour'] = df['Start Time'].dt.hour
    # Use mode() function on the hour column to get the value that appears most often.
    most_hour = df['hour'].mode()[0]
    print("The most common start hour is: " + str(most_hour) + " o'clock.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#%% Function to analyse station data
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station.
    # Use mode() function on the Start Station column to get the value that appears most often.
    start_station = df['Start Station'].mode()[0]

    print(f'The most common start station is: {start_station}.')

    # TO DO: display most commonly used end station.
    # Use mode() function on the End Station column to get the value that appears most often.
    end_station = df['End Station'].mode()[0]

    print(f'The most common end station is: {end_station}.')

    # TO DO: display most frequent combination of start station and end station trip
    # Create new column in data frame to combine start & end station via .cat() function.
    df['Trip Stations'] = df['Start Station'].str.cat(df['End Station'], sep = ' - ')

    # Use mode() function to find the most commom combination of start & end station.
    most_common_stations_combi = df['Trip Stations'].mode()[0]

    print(f'The most popular combination of start and end station is: \n{most_common_stations_combi}.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#%% Function to calculate statistics for travel time
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time.
    # Use .sum() to calculate the total travel time (Unit: seconds).
    total_travel_time = df['Trip Duration'].sum()

    # Transform Trip Duration to "days, hh:mm:ss" format (Inspiration source: https://docs.python.org/3/library/datetime.html)
    total_travel_time = datetime.timedelta(seconds = int(total_travel_time))

    print(f'The total travel time sums up to: {total_travel_time}')

    # TO DO: display mean travel time.
    # Use .mean() to calculate the mean travel time (Unit: seconds).
    mean_travel_time = df['Trip Duration'].mean()

    # Transform Trip Duration to "days, hh:mm:ss" (Inspiration source: https://docs.python.org/3/library/datetime.html).
    mean_travel_time = datetime.timedelta(seconds = int(mean_travel_time))

    print(f'The mean travel time is: {mean_travel_time}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#%% Function to calculate statistics on user
def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types.
    # Inspiration source: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html.
    # Use value_counts() method to count user by user type.
    user_type = df['User Type'].value_counts()

    print(f'Number of users by user type:\n{user_type}')

    # TO DO: Display counts of gender.
    # Problem: there is no gender column in washington.csv file.
    # if clause to inform user that there is no gender information, if Washington was selected as city.
    if city == 'washington':
        print('\nNumber of users by gender:')
        print(f'\nSorry, there is no gender information available for ' + city.title() + '.')
    else:
        user_gender = df['Gender'].value_counts()
        print(f'\nNumber of users by gender:\n{user_gender}')

    # TO DO: Display earliest, most recent, and most common year of birth.
    # Problem: there is no gender column in washington.csv file.
    # if clause to inform user that there is no Birth Year information, if Washington was selected as city.
    if city == 'washington':
        print('\nStatistics for users year of birth:')
        print(f'\nSorry, there is no birth year information available for the users from ' + city.title() + '.')
    else:
        # Use .min(), max(), mode() functions to get earliest, most recent & most popular year of birth.
        birth_year_earliest = int(df['Birth Year'].min())
        birth_year_recent = int(df['Birth Year'].max())
        birth_year_common = int(df['Birth Year'].mode()[0])

        print('\nStatistics for users year of birth:')
        print(f'\nThe earliest year of birth is: {birth_year_earliest}.\nThe most recent year of birth is: {birth_year_recent}.\nThe most popular year of birth is: {birth_year_common}.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_raw_data(df):
    """Shows the user 5 rows of raw data from the selected city"""
    # Initialize counter variable.
    counter = 0
    # List to check user input.
    check_user_input = ['yes', 'no']
    # Ask user if he/she wants to view a few rows of raw data.
    while True:
        view_raw = input("\nWould you like to view some rows of raw data? Please enter 'yes' or 'no'.\n")
        if view_raw.lower() == 'yes':
            print(df[counter:counter+5])
            counter += 5
        elif view_raw.lower() not in check_user_input:
            print('\nYour input is not valid.')
        else:
            break
    print('-'*40)

# Function to call the other functions defined before this part
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        view_raw_data(df)


        restart = input("\nWould you like to restart? Enter 'yes' or 'no'.\n")
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
