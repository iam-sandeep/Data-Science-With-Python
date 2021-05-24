"""
Slicing index values
Slicing lets you select consecutive elements of an object using first:last syntax. 
DataFrames can be sliced by index values or by row/column number; we'll start with the first case. 
This involves slicing inside the .loc[] method.

Compared to slicing lists, there are a few things to remember.

You can only slice an index if the index is sorted (using .sort_index()).
To slice at the outer level, first and last can be strings.
To slice at inner levels, first and last should be tuples.
If you pass a single slice to .loc[], it will slice the rows.
pandas is loaded as pd. temperatures_ind has country and city in the index, and is available.
"""
# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Russia
print(temperatures_srt.loc["Pakistan":"Russia"])

# Try to subset rows from Lahore to Moscow
print(temperatures_srt.loc["Lahore":"Moscow"])

# Subset rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[("Pakistan", "Lahore"):("Russia", "Moscow")])


"""
Slicing in both directions
You've seen slicing DataFrames by rows and by columns, but since DataFrames are two-dimensional 
objects, it is often natural to slice both dimensions at once.
 That is, by passing two arguments to .loc[], you can subset by rows and columns in one go.
"""
# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq", "Baghdad")])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:, "date":"avg_temp_c"])

# Subset in both directions at once
print(temperatures_srt.loc[("India", "Hyderabad")                           :("Iraq", "Baghdad"),  "date":"avg_temp_c"])


"""
Slicing time series
Slicing is particularly useful for time series since it's a common thing to want to filter
 for data within a date range. Add the date column to the index, then use .loc[] 
 to perform the subsetting. The important thing to remember is to keep your dates
  in ISO 8601 format, that is, yyyy-mm-dd.

Recall from Chapter 1 that you can combine multiple Boolean conditions
 using logical operators (such as &). To do so in one line of code, you'll
  need to add parentheses () around each condition.



"""

# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(
    temperatures["date"] >= "2010-01-01") & (temperatures["date"] <= "2011-12-31")]
print(temperatures_bool)

# Set date as an index and sort the index
temperatures_ind = temperatures.set_index("date").sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc["2010":"2011"])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc["2010-08":"2011-02"])


# Exampleof pivot table
# Subset for Egypt to India
temp_by_country_city_vs_year.loc["Egypt":"India"]
# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[("Egypt", "Cairo"):("India", "Delhi")]

# Subset in both directions at once
temp_by_country_city_vs_year.loc[("Egypt", "Cairo"):(
    "India", "Delhi"), "2005":"2010"]

# Just Example


"""
Subsetting by row/column number
The most common ways to subset rows are the ways we've previously discussed:
 using a Boolean condition or by index labels. However, it is also occasionally
  useful to pass row numbers.

This is done using .iloc[], and like .loc[], it can take two arguments to 
let you subset by rows and columns.


"""

# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[22, 1])

# Use slicing to get the first 5 rows
print(temperatures.iloc[:5])

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:, 2:4])

# Use slicing in both directions at once
print(temperatures.iloc[:5, 2:4])
