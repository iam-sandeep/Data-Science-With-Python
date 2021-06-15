'''
Dropping columns
Often, a DataFrame will contain columns that are not useful to your analysis.
 Such columns should be dropped from the DataFrame, to make it easier for you to focus 
 on the remaining columns.

In this exercise, you'll drop the county_name column because it only contains missing values,
 and you'll drop the state column because all of the traffic stops took place in one state
  (Rhode Island). Thus, these columns can be dropped because they contain no useful information.
   The number of missing values
 in each column has been printed to the console for you.


'''

# Examine the shape of the DataFrame
print(ri.shape)

# Drop the 'county_name' and 'state' columns
ri.drop(['county_name', "state"], axis='columns', inplace=True)

# Examine the shape of the DataFrame (again)
print(ri.shape)

'''
Dropping rows
When you know that a specific column will be critical to your analysis, and only a small fraction of rows are missing a value in that column, it often makes sense to remove those rows from the dataset.

During this course, the driver_gender column will be critical to many of your analyses. Because only a small fraction of rows are missing driver_gender, we'll drop those rows from the dataset.



'''
# Count the number of missing values in each column
print(ri.isnull().sum())

# Drop all rows that are missing 'driver_gender'
ri.dropna(subset=['driver_gender'], inplace=True)

# Count the number of missing values in each column (again)
print(ri.isnull().sum())

# Examine the shape of the DataFrame
print(ri.shape)