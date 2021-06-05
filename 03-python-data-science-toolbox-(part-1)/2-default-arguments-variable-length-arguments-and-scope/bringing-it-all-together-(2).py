'''
Bringing it all together (2)
100xp

Wow, you've just generalized your Twitter language analysis that you did in the previous chapter
to include a default argument for the column name. You're now going to generalize this function
one step further by allowing the user to pass it a flexible argument, that is, in this case,
as many column names as the user would like!

Once again, for your convenience, pandas has been imported as pd and the 'tweets.csv' file has
been imported into the DataFrame tweets_df. Parts of the code from your previous work are also
provided.

Instructions
-Complete the function header by supplying the parameter for the dataframe df and the flexible
argument *args.
-Complete the for loop within the function definition so that the loop occurs of the tuple args.
-Call count_entries() by passing the tweets_df DataFrame and the column name 'lang'. Assign the
result to result1.
-Call count_entries() by passing the tweets_df DataFrame and the column names 'lang' and 'source'.
Assign the result to result2.
'''
# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
tweets_df = pd.read_csv('tweets.csv')

# Define count_entries()
def count_entries(df, *args):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    #Initialize an empty dictionary: cols_count
    cols_count = {}
    
    # Iterate over column names in args
    for col_name in args:
    
        # Extract column from DataFrame: col
        col = df[col_name]
    
        # Iterate over the column in DataFrame
        for entry in col:
    
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
    
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Call count_entries(): result2
result2 = count_entries(tweets_df, 'lang', 'source')

# Print result1 and result2
print(result1)
print(result2)


'''
*args

The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function. It is used to pass a non-key worded, variable-length argument list. 

The syntax is to use the symbol * to take in a variable number of arguments; by convention, it is often used with the word args.
What *args allows you to do is take in more arguments than the number of formal arguments that you previously defined. With *args, any number of extra arguments can be tacked on to your current formal parameters (including zero extra arguments).
For example : we want to make a multiply function that takes any number of arguments and able to multiply them all together. It can be done using *args.
Using the *, the variable that we associate with the * becomes an iterable meaning you can do things like iterate over it, run some higher-order functions such as map and filter, etc.
 

 **kwargs

The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is because the double star allows us to pass through keyword arguments (and any number of them).



A keyword argument is where you provide a name to the variable as you pass it into the function.
One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it. That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.

'''





