'''
Building a JointGrid and jointplot
Seaborn's JointGrid combines univariate plots such as histograms, rug plots and kde plots with bivariate plots such as scatter and regression plots. The process for creating these plots should be familiar to you now. 
These plots also demonstrate how Seaborn provides convenient functions to combine multiple plots together.
'''
# Build a JointGrid comparing humidity and total_rentals
sns.set_style("whitegrid")
g = sns.JointGrid(x="hum",
                  y="total_rentals",
                  data=df,
                  xlim=(0.1, 1.0))

g.plot(sns.regplot, sns.distplot)

plt.show()
plt.clf()

# Create a jointplot similar to the JointGrid 
sns.jointplot(x="hum",
        y="total_rentals",
        kind='reg',
        data=df)

plt.show()
plt.clf()

'''
Jointplots and regression
Since the previous plot does not show a relationship between humidity and rental amounts,
 we can look at another variable that we reviewed earlier. Specifically, the relationship 
 between temp and total_rentals.
'''
# Plot temp vs. total_rentals as a regression plot
sns.jointplot(x="temp",
         y="total_rentals",
         kind='reg',
         data=df,
         order= 2,
         xlim=(0, 1))

plt.show()
plt.clf()

# Plot a jointplot showing the residuals
sns.jointplot(x="temp",
        y="total_rentals",
        kind='resid',
        data=df,
        order=2)

plt.show()
plt.clf()


'''
Complex jointplots
The jointplot is a convenience wrapper around many of the JointGrid functions. However,
 it is possible to overlay some of the JointGrid plots on top of the standard jointplot. 
 In this example, we can look at the different distributions for riders that are considered
  casual versus those that are registered.


'''
# Create a jointplot of temp vs. casual riders
# Include a kdeplot over the scatter plot
g = (sns.jointplot(x="temp",
             y="casual",
             kind='scatter',
             data=df,
             marginal_kws=dict(bins=10, rug=True))
    .plot_joint(sns.kdeplot))
    
plt.show()
plt.clf()

# Replicate the above plot but only for registered riders
g = (sns.jointplot(x="temp",
             y="registered",
             kind='scatter',
             data=df,
             marginal_kws=dict(bins=10, rug=True))
    .plot_joint(sns.kdeplot))

plt.show()
plt.clf()
