'''
Inner joins and number of rows returned
All of the merges you have studied to this point are called
 inner joins. It is necessary to understand that inner joins only return the rows 
 with matching values in both tables.


ONe to many Relationship

with a one-to-many relationship, a row in the left table may be repeated if 
it is related to multiple rows in the right table.


Enriching a dataset
Setting how='left' with the .merge()method is a useful technique for enriching or
 enhancing a dataset with additional information from a different table.


Using outer join to select actors

One cool aspect of using an outer join is that, because it returns all
 rows from both merged tables and null where they do not match, 
you can use it to find rows that do not have a match in the other table. 

'''


'''
Concatenation basics


You have been given a few tables of data with musical
 track info for different albums from the metal band, Metallica. 
 The track info comes from their Ride The Lightning, Master Of Puppets, and St. 
 Anger albums. Try various features of the .concat() method by concatenating the tables vertically together in different ways.

The tables tracks_master, tracks_ride, and tracks_st have loaded for you.
'''

#Concatenate tracks_master, tracks_ride,
# and tracks_st, in that order, setting sort to True.

 # Concatenate the tracks
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st], 
                               sort=True)
print(tracks_from_albums)


#Concatenate tracks_master, 
#tracks_ride, and tracks_st, where the index goes from 0 to n-1.

# Concatenate the tracks so the index goes from 0 to n-1
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               ignore_index=True,
                               sort=True)
print(tracks_from_albums)


#Concatenate tracks_master,
 #tracks_ride, and tracks_st, showing only columns that are in all tables.

 # Concatenate the tracks, show only columns names that are in all tables
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               join='inner',
                               sort=True)
print(tracks_from_albums)


"""
Concatenating with keys
The leadership of the music streaming company has come to you and asked you for assistance in analyzing sales for a recent business quarter. They would like to know which month in the quarter saw the highest average invoice total. You have been given three tables with invoice data named inv_jul, inv_aug, and inv_sep. 
Concatenate these tables into one to create a graph of the average monthly invoice total.
"""
"""
Concatenate the three tables together vertically in order with the oldest month first, adding '7Jul', '8Aug', and '9Sep' as keys for their respective months, and save to variable avg_inv_by_month.
Use the .agg() method to find the average of the total column from the grouped invoices.
Create a bar chart of avg_inv_by_month.
"""
# Concatenate the tables and add keys
inv_jul_thr_sep = pd.concat([inv_jul, inv_aug, inv_sep], 
                            keys=['7Jul','8Aug','9Sep'])

# Group the invoices by the index keys and find avg of the total column
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total':'mean'})

# Bar plot of avg_inv_by_month
avg_inv_by_month.plot(kind='bar')
plt.show()

'''
Using the append method
The .concat() method is excellent when you need a lot of control over how concatenation is performed. However, if you do not need as much control, then the .append() method is another option. You'll try this method out by appending the track lists together from different Metallica albums. From there, you will merge it with the invoice_items table to determine which track sold the most.

The tables tracks_master, tracks_ride, tracks_st, and invoice_items have loaded for you.

Task
Use the .append() method to combine (in this order)tracks_ride, tracks_master, and tracks_st together vertically, and save to metallica_tracks.
Merge metallica_tracks and invoice_items on tid with an inner join, and save to tracks_invoices.
For each tid and name in tracks_invoices, sum the quantity sold column, and save as tracks_sold.
Sort tracks_sold in descending order by the quantity column, and print the table.

'''
# Use the .append() method to combine the tracks tables
metallica_tracks = tracks_ride.append([tracks_master, tracks_st], sort=False)

# Merge metallica_tracks and invoice_items
tracks_invoices = metallica_tracks.merge(invoice_items, on='tid')

# For each tid and name sum the quantity sold
tracks_sold = tracks_invoices.groupby(['tid','name']).agg({'quantity':'sum'})

# Sort in decending order by quantity and print the results
print(tracks_sold.sort_values(['quantity'], ascending=False))



'''
Concatenate and merge to find common songs
The senior leadership of the streaming service is
 requesting your help again. You are given the historical 
 files for a popular playlist in the classical music genre in 2018 and 2019.
  Additionally, you are given a similar set of files for the most popular pop
   music genre playlist on the streaming service in 2018 and 2019. Your goal is 
   to concatenate the respective files to make a large classical playlist table 
   and overall popular music table. Then filter the classical music table using a
    semi-join to return only the most popular classical music tracks.

The tables classic_18, classic_19, and pop_18, pop_19 have been loaded for you.
 Additionally, pandas has been loaded as pd.




'''

# Concatenate the classic tables vertically
classic_18_19 = pd.concat([classic_18, classic_19], ignore_index=True)

# Concatenate the pop tables vertically
pop_18_19 = pd.concat([pop_18, pop_19], ignore_index=True)

# Merge classic_18_19 with pop_18_19
classic_pop = classic_18_19.merge(pop_18_19, on='tid')

# Using .isin(), filter classic_18_19 rows where tid is in classic_pop
popular_classic = classic_18_19[classic_18_19['tid'].isin(classic_pop['tid'])]

# Print popular chart
print(popular_classic)


#Merger ordered method 

# Use merge_ordered() to merge gdp and sp500 on year and date
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on="year", right_on="date", 
                             how="left")

# Print gdp_sp500
print(gdp_sp500)

# Use merge_ordered() to merge gdp and sp500, interpolate missing value
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', 
                             how='left',  fill_method='ffill')

# Print gdp_sp500
print (gdp_sp500)


# Use merge_ordered() to merge gdp and sp500, interpolate missing value
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', 
                             how='left',  fill_method='ffill')

# Subset the gdp and returns columns
gdp_returns = gdp_sp500[['gdp','returns']]

# Print gdp_returns correlation
print(gdp_returns.corr())

#Merge_ordered

# Use merge_ordered() to merge inflation, unemployment with inner join
inflation_unemploy = pd.merge_ordered(inflation, unemployment, 
                                      on='date', how='inner')

# Print inflation_unemploy 
print(inflation_unemploy)

# Plot a scatter plot of unemployment_rate vs cpi of inflation_unemploy
inflation_unemploy.plot(kind='scatter', x='unemployment_rate', y='cpi')
plt.show()



#merge_ordered() caution, multiple columns

# Merge gdp and pop on date and country with fill and notice rows 2 and 3
ctry_date = pd.merge_ordered(gdp,pop, on=("date","country"),
                             fill_method='ffill')

# Print ctry_date
print(ctry_date)

# Merge gdp and pop on country and date with fill
date_ctry = pd.merge_ordered(gdp,pop, on=("country","date"),
                             fill_method='ffill')

# Print date_ctry
print(date_ctry)

'''
Using merge_asof() to study stocks
You have a feed of stock market prices that you record.
 You attempt to track the price every five minutes. Still, due to some network latency, 
 the prices you record are roughly every 5 minutes. You pull your price logs for three
  banks, JP Morgan (JPM), Wells Fargo (WFC), and Bank Of America (BAC).
   You want to know how the price change of the two other banks compare
    to JP Morgan. Therefore, you will need to merge these three logs into one table. 
    Afterward, you will use the pandas .diff() method to compute the price change over 
    time. Finally, plot the price changes so you can review your analysis.

The three log files have been loaded for you as tables named jpm, wells, and bac.
'''

# Use merge_asof() to merge jpm and wells
jpm_wells = pd.merge_asof(jpm, wells, on='date_time', 
                          suffixes=('', '_wells'), direction='nearest')

# Use merge_asof() to merge jpm_wells and bac
jpm_wells_bac = pd.merge_asof(jpm_wells, bac, on='date_time', 
                              suffixes=('_jpm', '_bac'), direction='nearest')

# Compute price diff
price_diffs = jpm_wells_bac.diff()

# Plot the price diff of the close of jpm, wells and bac only
price_diffs.plot(y=['close_jpm','close_wells','close_bac'])
plt.show()




'''
Using merge_asof() to create dataset
The merge_asof() function can be used to create datasets
where you have a table of start and stop dates, and you want
to use them to create a flag in another table. You have been given gdp,
which is a table of quarterly GDP values of the US during the 1980s. Additionally, 
the table recession has been given to you. It holds the starting date of every US recession
since 1980, and the date when the recession was declared to be over. Use merge_asof() to
merge the tables and create a status flag if a quarter was during a recession. Finally,
to check your work, plot the data in a bar chart.

The tables gdp and recession have been loaded for you.
'''

# Merge gdp and recession on date using merge_asof()
gdp_recession = pd.merge_asof(gdp, recession, on="date")

# Create a list based on the row value of gdp_recession['econ_status']
is_recession = ['r' if s=='recession' else 'g' for s in gdp_recession['econ_status']]

# Plot a bar chart of gdp_recession
gdp_recession.plot(kind="bar", y="gdp", x="date", color="red", rot=90)
plt.show()











