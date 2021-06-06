'''
Plot a histogram
The distplot() function will return a Kernel Density Estimate (KDE) by default. 
The KDE helps to smooth the distribution and is a useful way to look at the data. 
However, Seaborn can also support
 the more standard histogram approach if that is more meaningful for your analysis.
'''
# Create a distplot
sns.distplot(df['Award_Amount'],
             kde=False,
             bins=20)

# Display the plot
plt.show()


'''
Rug plot and kde shading
Now that you understand some function arguments for distplot(),
 we can continue further refining the output.
 This process of creating a visualization and 
 updating it in an incremental fashion is a useful and 
 common approach to look at data from multiple perspectives.

Seaborn excels at making this process simple.

'''
# Create a distplot of the Award Amount
sns.distplot(df['Award_Amount'],
             hist=False,
             rug=True,
             kde_kws={'shade':True})

# Plot the results
plt.show()