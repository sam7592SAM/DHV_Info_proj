import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

data = pd.read_csv('laptops_test.csv')
# print (data.dtypes)

# Filter by Category and Manufacturers
categories1= ['Gaming']
manufacturers1 = ['Asus', 'Dell', 'MSI', 'Lenovo']
# price_range = (data["Price"]<=3600000 ) & (data["Price"] >= 1000000)


filt_1 = data[data['Category'].isin(categories1)
                     & data['Manufacturer'].isin(manufacturers1)]

'''
# Drop specified columns
columns_to_drop = ['Model Name', 'Screen Size', 'Screen', 'CPU', 'GPU', 'Operating System', 'Operating System Version', 'Weight']
filt_1 = filt_1.drop(columns_to_drop, axis=1)
'''

# Plot the pie chart
manufacturer_counts = filt_1['Manufacturer'].value_counts()

plt.figure(figsize=(8, 6))
plt.pie(manufacturer_counts, labels=manufacturer_counts.index,
        autopct='%2.1f%%')
plt.title('Gaming Laptops', fontsize=15, weight="bold")
plt.axis('equal')
plt.legend()
plt.show()


# To plot Line Graph
# Define the filter conditions
manufacturers = ['Asus', 'Dell', 'HP']
category = 'Notebook'

# Apply the filters
filtered_data = data[
    (data['Manufacturer'].isin(manufacturers)) &
    (data['Category'] == category)]

# Group the data by Manufacturer and calculate the average price
manufacturer_prices = filtered_data.groupby('Manufacturer')['Price'].mean().sort_values()

# Plot the line graph
plt.figure(figsize=(10, 6))
plt.plot(manufacturer_prices.index, manufacturer_prices.values, marker='o')
plt.xlabel('Manufacturer')
plt.ylabel('Average Price')
plt.title('Average Price of Notebooks by Manufacturer')
plt.xticks(rotation=45)
# plt.grid(True)
plt.show()


# Bar graph
# Define the filter conditions
manufacturers3 = ['Dell', 'HP', 'Asus', 'Lenovo', 'MSI']
cpu = 'Intel Core i7 7700HQ 2.8GHz'

# Apply the filters
filt_3 = data[
    (data['Manufacturer'].isin(manufacturers3)) &
    (data['CPU'] == cpu)
]

# Group the data by Manufacturer and calculate the average price
manufacturer_prices = filt_3.groupby('Manufacturer')['Price'].mean().sort_values()

color_palette = ['blue', 'green', 'orange', 'red', 'brown']

# Plot the bar graph
plt.figure(figsize=(10, 6))
plt.bar(manufacturer_prices.index, manufacturer_prices.values,
        color=color_palette)
plt.xlabel('Manufacturer')
plt.ylabel('Average Price')
plt.title('Average Price of Laptops with Highest CPU spec', weight="bold")
plt.xticks(rotation=45)
# plt.grid(True)
plt.show()

cpu = data[['CPU','Manufacturer']].groupby('CPU').agg('count').sort_values(
    'Manufacturer', ascending=False).reset_index()
sns.barplot(data=cpu.head(10), x="Manufacturer", y="CPU")
plt.title("CPU vs Total Count of Manufacturers", weight="bold")
