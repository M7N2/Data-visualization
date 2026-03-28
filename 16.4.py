# Automatic indexes.
import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print("Available columns:", header_row)

    # Creating dict {'STATION': 0, 'DATE': 1, 'TMAX': 2, 'TMIN': 3}.
    header_dict = {}
    for index, column_name in enumerate(header_row):
        header_dict[column_name] = index

    # Find indexes by name.
    date_index = header_dict['DATE']
    tmax_index = header_dict['TMAX']
    tmin_index = header_dict['TMIN']
    
    # Reading dates, minimum and maximum temperatures.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[date_index], "%Y-%m-%d")
        try:
            high = int(row[tmax_index])
            low = int(row[tmin_index])
        except ValueError:
            print(f"Missing data {current_date}.")    
        else:    
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
        
# Plotting data on a chart.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Formatting a chart.
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

#ax.set_ylim(0, 140)

plt.show()
