
#Loading a csv file in Pandas
# Import pandas
import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv('capital-onebike.csv', 
                    parse_dates = ['Start date', 'End date'])

# Print the initial (0th) row
print(rides.iloc[0])


'''
Making timedelta columns
Earlier in this course, you wrote a loop to subtract datetime objects and determine how long our sample bike had been out of the docks. Now you'll do the same thing with Pandas.

rides has already been loaded for you.

'''


# Subtract the start date from the end date
ride_durations = rides["End date"] - rides["Start date"]

# Convert the results to seconds
rides["Duration"] = ride_durations.dt.total_seconds()

print(rides['Duration'].head())














# Create joyrides
joyrides = (rides["Start station"] == rides["End station"])

# Total number of joyrides
print("{} rides were joyrides".format(joyrides.sum()))

# Median of all rides
print("The median duration overall was {:.2f} seconds"\
      .format(rides['Duration'].median()))

# Median of joyrides
print("The median duration for joyrides was {:.2f} seconds"\
      .format(rides[joyrides]['Duration'].median()))



'''
It's getting cold outside, W20529
Washington, D.C. has mild weather overall, but the average high temperature in 
October (68ºF / 20ºC) is certainly higher than the average high temperature in December 
(47ºF / 8ºC). People also travel more in December, and they work fewer days so they commute less.

How might the weather or the season have affected the length of bike trips?

'''
# Import matplotlib
import matplotlib.pyplot as plt

# Resample rides to daily, take the size, plot the results
rides.resample('D', on = 'Start date')\
  .size()\
  .plot(ylim = [0, 15])

# Show the results
plt.show()

# Import matplotlib
import matplotlib.pyplot as plt

# Resample rides to monthly, take the size, plot the results
rides.resample("M", on = 'Start date')\
  .size()\
  .plot(ylim = [0, 150])

# Show the results
plt.show()

'''
Members vs casual riders over time
Riders can either be "Members", meaning they pay yearly for the ability to take a 
bike at any time, or "Casual", meaning they pay at the kiosk attached to the bike dock.

Do members and casual riders drop off at the same rate over October to December, 
or does one drop off faster than the other?

As before, rides has been loaded for you. You're going to use the Pandas method 
.value_counts(), which returns the number of instances of each value in a Series.
 In this case, the counts of "Member" or "Casual".

'''
# Resample rides to be monthly on the basis of Start date
monthly_rides = rides.resample("M", on = "Start date")['Member type']

# Take the ratio of the .value_counts() over the total number of rides
print(monthly_rides.value_counts() / monthly_rides.size())


'''
Combining groupby() and resample()
A very powerful method in Pandas is .groupby(). Whereas .resample() 
groups rows by some time or date information, .groupby() groups rows based on
 the values in one or more columns. For example, rides.groupby('Member type').size() 
 would tell us how many rides there were by member type in our entire DataFrame.

.resample() can be called after .groupby(). For example, how long was the median ride 
by month, and by Membership type?

'''
# Group rides by member type, and resample to the month
grouped = rides.groupby('Member type')\
  .resample('M', on = 'Start date')

# Print the median duration for each group
print(grouped['Duration'].median())