import csv
from datetime import datetime
import matplotlib.pyplot as plt
import sys

filename = 'sitka_weather_2018_simple.csv'

# Get data from CSV
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            continue
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

def plot_highs():
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')
    plt.title("Daily High Temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

def plot_lows():
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')
    plt.title("Daily Low Temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

def main():
    while True:
        print("\nMenu:")
        print("1 - View High Temperatures")
        print("2 - View Low Temperatures")
        print("3 - Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            plot_highs()
        elif choice == '2':
            plot_lows()
        elif choice == '3':
            print("Exiting program. Have a nice day!")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main()
