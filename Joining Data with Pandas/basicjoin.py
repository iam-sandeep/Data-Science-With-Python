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