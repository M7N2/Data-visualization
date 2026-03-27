# Sitka's daily precipitation totals for 2018.
import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open (filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Reading dates, minimum and maximum temperatures.
    dates, prcp = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            prc = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")    
        else:
            dates.append(current_date)
            prcp.append(prc)

# Plotting data on a chart.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
#ax.plot(dates, prcp, c='blue', alpha=0.5)
ax.bar(dates, prcp, color='blue', alpha=0.5, width=0.8)
#plt.fill_between(dates, prcp, facecolor='blue', alpha=0.1)

# Formatting a chart.
plt.title("Daily precipitation - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitation (Inches)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
