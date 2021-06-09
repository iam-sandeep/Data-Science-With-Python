'''
Finding duplicates
A new update to the data pipeline feeding into ride_sharing has added the
 ride_id column, which represents a unique identifier for each ride.

The update however coincided with radically shorter average ride duration 
times and irregular user birth dates set in the future. 
Most importantly, the number of rides taken has increased by 20% overnight, 
leading you to think there might be both complete and incomplete duplicates 
in the ride_sharing DataFrame.

In this exercise, you will confirm this suspicion by finding those duplicates.
 A sample of ride_sharing is in your environment, as well as all the packages 
 you've been working with thus far.

'''

# Find duplicates
duplicates = ride_sharing.duplicated(subset = 'ride_id', keep = False)

# Sort your duplicated rides
duplicated_rides = ride_sharing[duplicates].sort_values('ride_id')

# Print relevant columns
print(duplicated_rides[['ride_id','duration','user_birth_year']])

'''
Treating duplicates
In the last exercise, you were able to verify that the new update feeding into ride_sharing contains a bug generating both complete and incomplete duplicated rows for some values of the ride_id column, with occasional discrepant values for the user_birth_year and duration columns.

In this exercise, you will be treating those duplicated rows by first dropping complete duplicates, and then merging the incomplete duplicate rows into one while keeping the average duration, and the minimum user_birth_year for each set of incomplete duplicate rows.
'''
