# San Francisco annual maximum and minimum temperature chart.
import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'data/san_francisco.csv'
with open (filename) as f:
    reader = csv.reader(f, delimiter=';')
    header_row = next(reader)
    
    # Reading dates, minimum and maximum temperatures.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[4])
            low = int(row[5])
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
plt.title("Daily high and low temperatures - 2018\nSan Francisco, CA",
          fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

#ax.set_ylim(0, 140) #  Установить масштаб по оси Y 

plt.show()
