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
