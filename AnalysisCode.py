"""
Creater: Sheikh "Nash" Nasher
Date Created: April 1st, 2018
"""

"""
The CSV file named "Products" contains the information about 28,000+ products sold on Sephora website. 
About 20,000 of them are discontinued (disregard them). For the remaining products, calculate the mean 
number of reviews for the 10% cheapest products (the bottom decile), the next eight deciles, and for the 
top 10% most expensive products (the top decile). Plot the numbers against the price deciles. The plot 
shall use dots but no lines. The plot shall have the grid and the axes labels, but no legend. The title 
and the X axis ticks are optional. Save the figure as a PNG file with the resolution of 150dpi.
Write a paragraph that explains your observations from the graph. In particular, explain what could be 
two possible reasons for the observed behavior
"""

import pandas as pd
from matplotlib import pyplot as plt

'''
Load the file contains the information about 28,000+ products sold on 
the Sephora website
'''

csvfile = 'products.csv'
df = pd.read_csv(csvfile)

'''
About 20,000 of them are discontinued. We disregard them and 
work with the remaining products
'''
continued_products = df['discontinued']==False
df = df [continued_products]

# Data Manipulation with pandas.qcut 
'''
Used pandas.qcut page on pandas 0.22.0 documentation from pandas.pydata.org
as a resource
'''
bins = pd.qcut(df['price'], 10) 

# DataFrame with GroupBy 
'''
Used pandas.DataFrame.groupby
page on pandas 0.22.0 documentation from pandas.pydata.org as a resource 
'''

# Calculate the mean number of reviews 
final_data = df.groupby(bins)['reviews'].mean()

# Print the final data 
print(final_data)

# Ploting the final data for the graph using dots  

plt.figure()
final_data.plot(style=['o','rx'])
plt.grid()
plt.savefig('Sephora Products Plot.png',dpi=150)
plt.show()
