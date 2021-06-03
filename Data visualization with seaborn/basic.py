'''
Making a scatter plot with lists
'''

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=phones)

# Show plot
plt.show()

#Making a count plot with a list



# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns


# Create count plot with region on the y-axis
sns.countplot(y=region)

# Show plot
plt.show()



# Import Matplotlib, Pandas, and Seaborn
import matplotlib.pyplot as pyplo
import pandas as pd
import seaborn as sns

# Create a DataFrame from csv file
df =pd.read_csv(csv_filepath)

# Create a count plot with "Spiders" on the x-axis
sns.countplot(x= "Spiders", data = df)

# Display the plot
pyplo.show()
