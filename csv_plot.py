# Read and plot the CSV files generated after the Aranet4 andriod app
# pulls data from the sensor.

import pandas as pd
import numpy as np

from matplotlib import pylab as plt
import matplotlib.dates as mdates
plt.ion()
import seaborn as sns

filename = 'Aranet4 file.csv'
df = pd.read_csv(fliename)
df.set_index('Time')
df['Time'] = pd.to_datetime(df['Time'])  

# select time/date range
mask = np.logical_and(df['Time']>'2021-01-01 01:00:00' ,
                      df['Time']<'2021-01-02 02:00:00')

fig, ax = plt.subplots()
sns.lineplot(x='Time', y='CO₂(ppm)', data = df.loc[mask],ax=ax)
plt.grid()
ax.xaxis.set_major_locator(mdates.AutoDateLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
fig.autofmt_xdate()
ax.set_title('$\mathrm{CO}_2 \mathrm{[ppm]}$')
