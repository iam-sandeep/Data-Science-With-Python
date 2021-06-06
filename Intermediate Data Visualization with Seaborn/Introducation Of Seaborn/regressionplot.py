'''
Create a regression plot
For this set of exercises, we will be looking at FiveThirtyEight's 
data on which US State has the worst drivers. The data set includes 
summary level information about fatal accidents as well as insurance 
premiums for each state as of 2010.

In this exercise, we will look at the difference between the regression plotting functions.

'''

# Create a regression plot of premiums vs. insurance_losses
sns.regplot(data=df,
            x="insurance_losses",
            y="premiums")

# Display the plot
plt.show()

# Create an lmplot of premiums vs. insurance_losses
sns.lmplot(data=df, x="insurance_losses", y="premiums")


# Display the second plot
plt.show()


'''

Plotting multiple variables
Since we are using lmplot() now, we can look at the more complex interactions of data.
 This data set includes geographic information by state and area. It might be interesting 
to see if there is a difference in relationships based on the Region of the country.
'''
# Create a regression plot using hue
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           hue="Region")

# Show the results
plt.show()


'''
Facetting multiple regressions
lmplot() allows us to facet the data across multiple rows and columns. 
In the previous plot, the multiple lines were difficult to read in one plot. 
We can try creating multiple plots by Region to see if that is a more useful visualization.

'''
# Create a regression plot with multiple rows
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           row="Region")

# Show the plot
plt.show()
