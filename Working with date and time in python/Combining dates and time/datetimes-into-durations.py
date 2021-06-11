'''
Turning pairs of datetimes into durations
When working with timestamps, we often want to know how much
 time has elapsed between events. Thankfully, we can use datetime
  arithmetic to ask Python to do the heavy lifting 
for us so we don't need to worry about day, month, or year
 boundaries. Let's calculate the number of seconds that the bike 
 was out of the dock for each trip.

Continuing our work from a previous coding exercise,
 the bike trip data has been loaded as the list onebike_datetimes.
  Each element of the list consists of two datetime objects, corresponding
   to the start and end of a trip, respectively.


'''
# Initialize a list for all the trip durations
onebike_durations = []

for trip in onebike_datetimes:
  # Create a timedelta object corresponding to the length of the trip
  trip_duration = trip['end'] - trip['start']
  
  # Get the total elapsed seconds in trip_duration
  trip_length_seconds = trip_duration.total_seconds()
  
  # Append the results to our list
  onebike_durations.append(trip_length_seconds)



  '''
The long and the short of why time is hard
Out of 291 trips taken by W20529, how long was the longest? How short was the shortest? Does anything look fishy?

As before, data has been loaded as onebike_durations.


  '''
# Calculate shortest and longest trips
shortest_trip = min(onebike_durations)
longest_trip = max(onebike_durations)

# Print out the results
print("The shortest trip was " + str(shortest_trip) + " seconds")
print("The longest trip was " + str(longest_trip) + " seconds")