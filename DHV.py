import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

# Read the CSV file
data = pd.read_csv('laptops_test.csv')

# Plotting the figure by specifying figure size and grids using GridSpec()
fig = plt.figure(figsize=(22, 18))
grid = gridspec.GridSpec(3, 2)

# Heading given to the dashboard
fig.suptitle("Laptop Price "
             "Predictions\n Name: Sam Philip Solo, Student ID: 22013137\n",
             fontsize=20, fontweight='bold', fontname='Times New Roman')

# Plotting various plots into the dashboard.
# 1. Pie Chart
ax1 = fig.add_subplot(grid[1, 1])

# Filtering the values to be plotted
categories1 = ["Gaming"]
manufacturers1 = ["Asus", "Dell", "MSI", "Lenovo"]
filt_1 = data[data["Category"].isin(categories1) & data["Manufacturer"].isin
              (manufacturers1)]

# Taking the count of Manufacturers
manufacturer_counts = filt_1["Manufacturer"].value_counts()

# Plot the Pie Chart and setting the Title with Legend
ax1.pie(manufacturer_counts, labels=manufacturer_counts.index,
        autopct="%1.1f%%")
ax1.set_title("Gaming Laptops", weight="bold")
ax1.legend(loc='best')

# 2. Histogram
ax2 = fig.add_subplot(grid[0, 0])

# Filter by Storage
filt_storage = data[data['Storage'] == '512GB SSD']

# Extract the 'Price' column
price_data = filt_storage['Price']

# Plot the histogram
ax2.hist(price_data, bins=10, edgecolor='black', color='yellow')
ax2.set_xlabel('Price')
ax2.set_ylabel('Frequency')
ax2.set_title('Distribution of Laptop Prices for Storage = 512GB SSD',
              weight='bold')

# 3. Line Plot
ax5 = fig.add_subplot(grid[1, 0])

# Filtering values
category_prices = data.groupby('Category')['Price'].mean().sort_values()

# Plotting line plot and specifying xlabels, ylabels and title
ax5.plot(category_prices.index, category_prices.values, marker='o')
ax5.set_xlabel('Category')
ax5.set_ylabel('Average Price')
ax5.set_title('Average Price by Category', weight='bold')
ax5.set_xticklabels(category_prices.index, rotation=45)

# 4. Bar plot
ax4 = fig.add_subplot(grid[2, 0])

# Filtering values from dataframe
cpu = data[['CPU', 'Manufacturer']].groupby('CPU').agg(
    'count').sort_values('Manufacturer', ascending=False).reset_index()

# Plotting Bar graph.
sns.barplot(data=cpu.head(10), x='Manufacturer', y='CPU', ax=ax4)
ax4.set_title('CPU vs Total Count of Manufacturers', weight='bold')

# Text grid
ax5 = fig.add_subplot(grid[2:, 1])
ax5.axis('off')
ax5.text(0.1, 0.5, '\nLaptop Price Predictions.\n The Dashboard on Laptop'
         'Price Predictions\n shows what factors affect Laptop price hikes.'
         '\nThese vary with specifications, features, brand,'
         'and so on.\n The following plots are explained as follows:'
         '\n 1. First plot is a Histogram that visualizes the \n distribution'
         'of laptop prices for laptops with \n a storage capacity of 512 GB'
         'SSD.\n 2. Second plot is a line plot, that computes the \n Average'
         'Price by comparing with their Category.'
         '\n 3. Third plot is a Horizontal bar plot, which compares \n each of'
         'the processors with the Manufacturers.\n In this graph, it takes'
         'the total count of manufacturers \n from this we can conclude most'
         'of the manufacturers use Intel \n Core i5 CPU.'
         '\n 4. Fourth plot is a Pie plot, which gives \n a count of Gaming'
         'laptops each manufacturer have.', fontsize=20,
         fontname="Times New Roman")

# Adjust the layout and spacing
fig.tight_layout()

# Save to PNG file
plt.savefig('22013137.png', dpi=300)
# Show the plot
plt.show()
