# Plot the pandas histogram
df['fmr_2'].plot.hist()
plt.show()
plt.clf()

# Set the default seaborn style
sns.set()

# Plot the pandas histogram again
df['fmr_2'].plot.hist()
plt.show()
plt.clf()



'''
Comparing styles
Seaborn supports setting different styles that can control the aesthetics of the final plot. 
In this exercise,
 you will plot the same data in two different styles in order to see how the styles change the output
'''
# Plot with a dark style 
sns.set_style('dark')
sns.distplot(df['fmr_2'])
plt.show()

# Clear the figure
plt.clf()


'''
Removing spines
In general, visualizations should minimize extraneous markings

 so that the data speaks for itself. Seaborn allows you to remove 
 the lines on the top, bottom, left and right axis, which are often called spines.
'''

# Set the style to white
sns.set_style('white')

# Create a regression plot
sns.lmplot(data=df,
           x='pop2010',
           y='fmr_2')

# Remove the spines
sns.despine()

# Show the plot and clear the figure
plt.show()
plt.clf()

