import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


# get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        TO DO: Create a while loop for user input that will prevent errors from throwing the program.
        TO DO: Define my filters in this function for the rest of the program, namely, CITY MONTH DAY.
        TO DO: Use a string method to promote case insenstivity for user input.
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')
    city = input('\nWhich city would you like to analyse today? (Chicago, New York City, Washington)\n').lower()
    response = ' '
    while city not in ("chicago","new york city","washington"):
        city = input("Sorry, that was not a valid choice. Let's try again. Please choose a city. ").lower()
        if response.lower() == ["chicago","new york city","washington"]:
            city = response
            break
    month = input('Would you like to filter the data by month, day, or not at all?  ').lower()
    while month not in ('month','day','not at all'):
        month = input("Sorry, that was not a valid choice. Let's try again. Please choose month, day, or 'not at all.' ").lower()
        response = ' '
        if response.lower() == 'month':
            print( )
            which_month = input('Awesome! Which month - January, February, March, April, May, or June? Please type out the full name. ').lower()
            month = which_month
        elif response.lower() == 'day':
            month = 'all'
            pass
        elif response.lower() == 'not at all':
            month = 'all'
            day = 'all'
            break
        else:
            if response.lower() != ('month','day','not at all'):
                print('Sorry, some of your previous answers wer not valid. Lets try this again.  ')
                continue
    day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all?  ').lower()
    while day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
        day = input("Sorry, that was not a valid choice. Let's try again. Please choose a day. ").lower()
        if response.lower() == ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            day = response
            break

            
    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    BIG TO DO: add a variable to prompt the user to view more rows of data.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Exceptions: incorrect entries will not break the programn but loop back to the original question.
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
        TO DO: extract data from the Start Time field for HOUR, MONTH DAY. Needed for other calulations.
        TO DO: Include a fliter for if month and day are not specified.
    """
    df = pd.read_csv(CITY_DATA[city])
    df.dropna(axis='index', how='all')
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        # months = ['January', 'February', 'March', 'April', 'May', 'June'] why didnt this work here?
        month = month.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Extract from main dataframe to define within this function. Convert the 'Start Time' column within this function using todate_time
    TO DO: extract from the HOUR MONTH DAY dataFrames previously created to answer the following print statements.
    """

    print('\nCalculating Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_month = df['month'].mode().max()
    popular_hour = df['hour'].mode().max()
    popular_day_of_week = df['day_of_week'].value_counts().index.max()


    # display the most common month
    print('\nPopular Month of Travel...\n', popular_month)
    print()


    # display the most common day of week
    print('\nPopular Day of Travel...\n', popular_day_of_week)
    print()



    print('\nPopular Hour of the day to Travel...\n', popular_hour)
    print()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    view_data = input('\nWould you like to view 5 rows of individual Popular Time data? Enter yes or no\n').lower()
    while view_data not in ("yes","no"):
        view_data = input("Hey now, quit trying to break stuff! Please Try again - Do you want more details, or just the summary for this category? type yes or no.  ").lower()
    start_loc = 0
    while view_data.lower() == 'yes':
        print(df.iloc[start_loc: ,  : 5])
        start_loc += 5
        view_data = input("Do you wish to see more? yes or no  ").lower()
        if view_data.lower() == 'yes':
            continue
        elif view_data.lower() == 'no':
            break
        while view_data.lower() not in ('yes','no'):
            view_data = input("You ok? That was not a valid choice either, try again please, yes or no. :-)  ").lower()
            continue                    
                    
def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Extract from main dataframe to define within this function.
    TO DO: use pandaSeries methods to define variables that answer the following print statements.
    
    """
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    df['both_stations'] = df['Start Station'] + df['End Station']
    popular_start = df['Start Station'].value_counts()
    popular_end = df['End Station'].value_counts()
    popular_stations = df['both_stations'].value_counts()

    # display most commonly used start station
    print('\nCalculating The Most Popular Starting Station...\n', popular_start)
    print()



    # display most commonly used end station
    print('\nCalculating The Most Popular End Station...\n', popular_end)
    print()


    # display most frequent combination of start station and end station trip
    print('\nCalculating The Most Popular Route, from Start Station to End Station...\n', popular_stations)
    print()



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    view_data = input('\nWould you like to view 5 rows of individual Popular Station data? Enter yes or no\n').lower()
    while view_data not in ("yes","no"):
        view_data = input("Hey now, quit trying to break stuff! Please Try again - Do you want more details, or just the summary for this category? type yes or no.  ").lower()
    start_loc = 0
    while view_data.lower() == 'yes':
        print(df.iloc[start_loc: ,  :5])
        start_loc += 5
        view_data = input("Do you wish to see more? yes or no  ").lower()
        if view_data.lower() == 'yes':
            continue
        elif view_data.lower() == 'no':
            break
        while view_data.lower() not in ('yes','no'):
            view_data = input("You ok? That was not a valid choice either, try again please, yes or no. :-)  ").lower()
            continue


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Extract from main dataframe to define within this function.
    TO DO: Use arithmetic operators on your pandaSeries to perform calulations that answer the following print statements. 
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    total_travel = df['Trip Duration'].sum()
    total_mean = np.mean(df['Trip Duration'])



    # display total travel time
    print('\nTotal Trip Duration Time (in hours):', total_travel//3600)
    print()


    # display mean travel time
    print('\nAverage Trip Duration Time (in seconds):', total_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    view_data = input('\nWould you like to view 5 rows of individual Trip Duration data? Enter yes or no\n').lower()
    while view_data not in ("yes","no"):
        view_data = input("Hey now, quit trying to break stuff! Please Try again - Do you want more details, or just the summary for this category? type yes or no.  ").lower()
    start_loc = 0
    while view_data.lower() == 'yes':
        print(df.iloc[start_loc: ,  :5])
        start_loc += 5
        view_data = input("Do you wish to see more? yes or no  ").lower()
        if view_data.lower() == 'yes':
            continue
        elif view_data.lower() == 'no':
            break
        while view_data.lower() not in ('yes','no'):
            view_data = input("You ok? That was not a valid choice either, try again please, yes or no. :-)  ").lower()
            continue


def user_stats(df):
    """Displays statistics on bikeshare users.
    Extract from main dataframe to define within this function.
    TO DO: Trick Question! This data is only available in 2 of 3 datasets. Create a while lopp to run calculations in this function that will not throw the program if values are not available.
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    user_type = df['User Type'].value_counts()
    """Washington does not have the above values in its dataframe, so a try statement was initiated here."""
    while True:
        try:
            if get_filters != 'Washington':
                gender = df['Gender'].value_counts()
                birth_year = df['Birth Year'].value_counts()
                user_type = df['User Type'].value_counts()
                print('\nNumbers by Gender:...\n', gender)
                print()
                print('\nThe first Birth Year to occur the most often and the least often:...\n', birth_year)
                print()
                print('\nNumber of User Types:...\n', user_type)
                break
        except KeyError:
            print("Gender and birth year values are not available for this city. Sorry!  ")
            user_type = df['User Type'].value_counts()
            print('\nNumber of User Types:...\n', user_type)
            print()
            break


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    view_data = input('\nWould you like to view 5 rows of individual Bikeshare User data? Enter yes or no\n').lower()
    while view_data not in ("yes","no"):
        view_data = input("Hey now, quit trying to break stuff! Please Try again - Do you want more details, or just the summary for this category? type yes or no.  ").lower()
    start_loc = 0
    while view_data.lower() == 'yes':
        print(df.iloc[start_loc: ,  :5])
        start_loc += 5
        view_data = input("Do you wish to see more? yes or no  ").lower()
        if view_data.lower() == 'yes':
            continue
        elif view_data.lower() == 'no':
            break
        while view_data.lower() not in ('yes','no'):
            view_data = input("You ok? That was not a valid choice either, try again please, yes or no. :-)  ").lower()
            continue



def main():
    while True:
        
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        print('-'*40)
        restart = input('\nWould you like to restart? Enter yes or no: \n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()








