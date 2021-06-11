'''
Putting the bike trips into the right time zone
Instead of setting the timezones for W20529 by hand, let's 
assign them to their IANA timezone: 'America/New_York'. Since we know their political jurisdiction, 
we don't need to look up their UTC offset. Python will do that for us.



'''

# Import tz
from dateutil import tz

# Create a timezone object for Eastern Time
et = tz.gettz('America/New_York')

# Loop over trips, updating the datetimes to be in Eastern Time
for trip in onebike_datetimes[:10]:
  # Update trip['start'] and trip['end']
  trip['start'] = trip['start'].replace(tzinfo = et)
  trip['end'] = trip['end'].replace(tzinfo = et)



  '''
What time did the bike leave? (Global edition)
When you need to move a datetime from one timezone into another, use .astimezone() and tz. 
Often you will be moving things into UTC, but for fun let's try 
moving things from 'America/New_York' into a few different time zones.

  '''

  # Create the timezone object
uk = tz.gettz('Europe/London')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in the UK?
notlocal = local.astimezone(uk)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())



# Create the timezone object
ist = tz.gettz('Asia/Kolkata')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in India?
notlocal = local.astimezone(ist)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())



# Create the timezone object
sm = tz.gettz("Pacific/Apia")

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in Samoa?
notlocal = local.astimezone(sm)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())