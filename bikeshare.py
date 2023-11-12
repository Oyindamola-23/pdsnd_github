import pandas as pd

def load_data(city):
    # Load data for the specified city
    file_path = f'{city.lower().replace(" ", "_")}.csv'  # Adjusted file name with underscores
    try:
      df = pd.read_csv(file_path, parse_dates=['Start Time'])
      return df
    except FileNotFoundError:
      print(f"Data file not found for {city}. Please make sure the file exists.")
      return None


def get_user_input():
    city = input("Select a city (chicago, washington, new york city): ").lower()

    if city not in ['chicago', 'washington', 'new york city']:
        print("Invalid city. Please choose a valid city.")
        return get_user_input()

    filter_type = input("Do you want to filter by day, month, or not at all? ").lower()

    if filter_type not in ['day', 'month', 'not at all']:
        print("Invalid filter type. Please choose a valid option.")
        return get_user_input()

    return city, filter_type

def filter_data(df, filter_type, time_period):
    # Filter data based on user input
    if filter_type == 'not at all':
        print("Not applying any filters.")
        return df
    elif filter_type == 'month':
        return df[df['Start Time'].dt.strftime('%B') == time_period]
    elif filter_type == 'day':
        return df[df['Start Time'].dt.day_name() == time_period]

def print_statistics(df):
    # Print statistics based on the filtered data

    print("\nStatistics:\n")

    print("City Statistics:")
    print(df['Start Time'].count())

    print("\nTrip Duration Statistics:")
    print("Total Trips:", df['Trip Duration'].count())
    print("Average Trip Duration:", df['Trip Duration'].mean())

    print("\nStation Statistics:")
    print("Most Popular Start Station:", df['Start Station'].mode().iloc[0])
    print("Most Common End Station:", df['End Station'].mode().iloc[0])
    print("Most Common Trip from Start to End:", df.groupby(['Start Station', 'End Station']).size().idxmax())

    print("\nUser Type Statistics:")
    print(df['User Type'].value_counts())

    if 'Gender' in df.columns:
        print("\nGender Statistics:")
        print(df['Gender'].value_counts())

    if 'Birth Year' in df.columns:
        print("\nBirth Year Statistics:")
        print("Earliest Year of Birth:", int(df['Birth Year'].min()))
        print("Most Recent Year of Birth:", int(df['Birth Year'].max()))
        print("Most Common Year of Birth:", int(df['Birth Year'].mode().iloc[0]))

    print("\nTime Statistics:")
    print("Most Common Month:", df['Start Time'].dt.strftime('%B').mode().iloc[0])
    print("Most Common Day of Week:", df['Start Time'].dt.day_name().mode().iloc[0])
    print("Most Common Hour of Day:", df['Start Time'].dt.hour.mode().iloc[0])

def main():
    city, filter_type = get_user_input()
    df = load_data(city)

    if df is not None:
        if filter_type in ['month', 'day']:
            if filter_type == 'month':
                time_period = input(f"Enter the {filter_type} (e.g., january, february, march, april, may, june): ").title()
            elif filter_type == 'day':
                time_period = input(f"Enter the {filter_type} (e.g., monday, tuesday, wednesday, thursday, friday, saturday, sunday): ").title()

            df = filter_data(df, filter_type, time_period)

        print_statistics(df)

if __name__ == "__main__":
    main()


def main():
    city = input("Select a city (chicago, washington, new york city): ").lower()

    if city not in ['chicago', 'washington', 'new york city']:
            print("Invalid city. Please choose a valid city.")
            return get_user_input()

    filter_type = input("Do you want to filter by day, month, or not at all? ").lower()

    if filter_type not in ['day', 'month', 'not at all']:
            print("Invalid filter type. Please choose a valid option.")
            return get_user_input()

    return city, filter_type

    def filter_data(df, filter_type, time_period):
        # Filter data based on user input
        if filter_type == 'not at all':
            print("Not applying any filters.")
            return df
        elif filter_type == 'month':
            return df[df['Start Time'].dt.strftime('%B') == time_period]
        elif filter_type == 'day':
            return df[df['Start Time'].dt.day_name() == time_period]

    def print_statistics(df):
        # Print statistics based on the filtered data
        print("\nStatistics:\n")

        print("City Statistics:")
        print(df['Start Time'].count())

        print("\nTrip Duration Statistics:")
        print("Total Trips:", df['Trip Duration'].count())
        print("Average Trip Duration:", df['Trip Duration'].mean())

        print("\nStation Statistics:")
        print("Most Popular Start Station:", df['Start Station'].mode().iloc[0])
        print("Most Common End Station:", df['End Station'].mode().iloc[0])
        print("Most Common Trip from Start to End:", df.groupby(['Start Station', 'End Station']).size().idxmax())

        print("\nUser Type Statistics:")
        print(df['User Type'].value_counts())

        if 'Gender' in df.columns:
            print("\nGender Statistics:")
            print(df['Gender'].value_counts())

        if 'Birth Year' in df.columns:
            print("\nBirth Year Statistics:")
            print("Earliest Year of Birth:", int(df['Birth Year'].min()))
            print("Most Recent Year of Birth:", int(df['Birth Year'].max()))
            print("Most Common Year of Birth:", int(df['Birth Year'].mode().iloc[0]))

        print("\nTime Statistics:")
        print("Most Common Month:", df['Start Time'].dt.strftime('%B').mode().iloc[0])
        print("Most Common Day of Week:", df['Start Time'].dt.day_name().mode().iloc[0])
        print("Most Common Hour of Day:", df['Start Time'].dt.hour.mode().iloc[0])

def run_analysis(city, filter_type, time_period=None):
    df = load_data(city)

    if df is not None:
        if filter_type in ['month', 'day']:
            if filter_type == 'month':
                time_period = input(f"Enter the {filter_type} (e.g., january, february, march, april, may, june): ").title()
            elif filter_type == 'day':
                time_period = input(f"Enter the {filter_type} (e.g., monday, tuesday, wednesday, thursday, friday, saturday, sunday): ").title()

        df = filter_data(df, filter_type, time_period)

        print_statistics(df)

def main():
    while True:
        city, filter_type = get_user_input()
        run_analysis(city, filter_type)

        restart = input("Do you want to see more? (yes/no): ").lower()
        if restart == 'no':
            print("Goodbye!")
            break




if __name__ == "__main__":
    main()


print("Wait! you're about to see something fun")

import pandas as pd

def show_raw_data(df):
    """
    Display raw data from a DataFrame in increments of 5 rows based on user input.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the raw data.

    Returns:
    None
    """
    i = 0
    raw = input("Do you want to see the raw data? (yes/no): ").lower()

    while True:
        if raw == 'no':
            break
        elif raw == 'yes':
            # Displaying the next 5 rows
            print(df[i:i+5])

            # Prompting the user to view more rows
            raw = input("Do you want to see 5 more rows of the raw data? (yes/no): ").lower()
            i += 5
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    # Load data from CSV files
    chicago_df = pd.read_csv('chicago.csv')
    washington_df = pd.read_csv('washington.csv')
    new_york_city_df = pd.read_csv('new_york_city.csv')

    # Concatenate the DataFrame
    frames = [chicago_df, washington_df, new_york_city_df]
    combined_df = pd.concat(frames, sort=False)

    # Call the function to show raw data
    show_raw_data(combined_df)

    print("Goodbye!")

if __name__ == "__main__":
    main()
