#MapPlot.py
#Name:
#Date:
#Assignment:

import airlines
airlines = airlines.get_airports()

num_items = len(airlines)
years = []
canceled = []

for spot in range(num_items):
    year = airlines[spot]["Time"]["Year"]
    canceledFlights = airlines[spot]["Statistics"]["Flights"]["Cancelled"]
    years.append(year)
    canceled.append(canceledFlights)

import matplotlib.pyplot as plt
plt.plot(years, canceled, "ro")
plt.savefig("output")
