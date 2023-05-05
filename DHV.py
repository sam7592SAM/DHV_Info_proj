import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

data = pd.read_csv('laptops_test.csv')
# print (data.dtypes)

fig = plt.figure(figsize=(20, 18))
grid = gridspec.GridSpec(3, 2)

# Code to plot a Pie chart
ax1 = fig.add_subplot(grid[0, 0])
categories1 = ["Gaming"]
manufacturers1 = ["Asus", "Dell", "MSI", "Lenovo"]
filt_1 = data[data["Category"].isin(categories1) & data["Manufacturer"].isin
              (manufacturers1)]
manufacturer_counts = filt_1["Manufacturer"].value_counts()
ax1.pie(manufacturer_counts, labels=manufacturer_counts.index,
        autopct="%1.1f%%")
ax1.set_title("Gaming Laptops", weight="bold")
ax1.legend(loc='best')

# Create the histogram subplot
ax2 = fig.add_subplot(grid[1, 1])

# Filter by Storage
filt_storage = data[data['Storage'] == '512GB SSD']

# Extract the 'Price' column
price_data = filt_storage['Price']

# Plot the histogram
ax2.hist(price_data, bins=10, edgecolor='black', color='yellow')
ax2.set_xlabel('Price')
ax2.set_ylabel('Frequency')
ax2.set_title('Distribution of Laptop Prices for Storage = 512GB SSD')

# Bar graph
ax3 = fig.add_subplot(grid[1, 0])
manufacturers3 = ['Dell', 'HP', 'Asus', 'Lenovo', 'MSI']
cpu = 'Intel Core i7 7700HQ 2.8GHz'
filt_3 = data[(data['Manufacturer'].isin(manufacturers3))
              & (data['CPU'] == cpu)]
manufacturer_prices = filt_3.groupby(
    'Manufacturer')['Price'].mean().sort_values()
color_palette = ['blue', 'green', 'orange', 'red', 'brown']
ax3.bar(manufacturer_prices.index,
        manufacturer_prices.values, color=color_palette)
ax3.set_xlabel('Manufacturer')
ax3.set_ylabel('Average Price')
ax3.set_title('Average Price of Laptops with Highest CPU spec', weight='bold')

# Adjust the layout and spacing
fig.tight_layout()

# Show the plot
plt.show()
