'''
Printing dates in a friendly format
Because people may want to see dates in many different formats, Python comes with very flexible functions for turning date objects into strings.

Let's see what event was recorded first in the Florida hurricane data set. In this exercise, you will format the earliest date in the florida_hurriance_dates list in two ways so you can 
decide which one you want to use: either the ISO standard or the typical US style


'''

# Assign the earliest date to first_date
first_date = min(florida_hurricane_dates)

# Convert to ISO and US formats
iso = "Our earliest hurricane date: " + first_date.isoformat()
us = "Our earliest hurricane date: " + first_date.strftime("%m/""%d/""%Y")

print("ISO: " + iso)
print("US: " + us)



'''
Representing dates in different ways
date objects in Python have a great number of ways they can be 
printed out as strings. In some cases, you want to know the date in a clear,
 language-agnostic format. In other cases, you want something which can fit into
  a paragraph and flow naturally.

Let's try printing out the same date, August 26, 1992 (the day that Hurricane
 Andrew made landfall in Florida), in a number of different ways, to practice using the 
 .strftime() method.

A date object called andrew has already been created.

'''

