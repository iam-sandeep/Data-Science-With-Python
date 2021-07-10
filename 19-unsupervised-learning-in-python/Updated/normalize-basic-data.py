'''

Now that you are aware of normalization, let us try to normalize some data.
 goals_for is a list of goals scored by a football team in their last ten matches. 
 Let us standardize the data using the whiten() function.



'''
# Import the whiten function
from scipy.cluster.vq import whiten 

goals_for = [4,3,2,3,1,1,2,0,1,4]

# Use the whiten() function to standardize the data
scaled_data = whiten(goals_for)
print(scaled_data)





'''
Visualize normalized data
After normalizing your data, you can compare the scaled data to the original data to see the difference.
 The variables from the last exercise, goals_for and scaled_data are already available to you.




'''
# Plot original data
plt.plot(goals_for, label='original')

# Plot scaled data
plt.plot(scaled_data, label='scaled')

# Show the legend in the plot
plt.legend()

# Display the plot
plt.show()




'''
Normalization of small numbers
In earlier examples, you have normalization of whole numbers. In this exercise,
 you will look at the treatment of fractional numbers - the change of interest rates 
 in the country of Bangalla over the years. 
For your use, matplotlib.pyplot is imported as plt.





'''
# Prepare data
rate_cuts = [0.0025, 0.001, -0.0005, -0.001, -0.0005, 0.0025, -0.001, -0.0015, -0.001, 0.0005]

# Use the whiten() function to standardize the data
scaled_data = whiten(rate_cuts)

# Plot original data
plt.plot(rate_cuts, label='original')

# Plot scaled data
plt.plot(scaled_data, label='scaled')

plt.legend()
plt.show()