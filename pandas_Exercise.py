
import statistics
import pandas

# Read the entire CSV file into a pandas DataFrame
df = pandas.read_csv('shopping_data.csv')


# Filter out the column, value_eur
onLine_Amt = df['Amt-OnLine']

print(onLine_Amt)
mean_value_In_Shop = round(statistics.mean(onLine_Amt), 2)



"""
store_Amt = df['Amt_InShop']
print(store_Amt)

# Compute and display the mean
mean_value_In_Shop = round(statistics.mean(onLine_Amt), 2)
print("Mean Value In Store ",mean_value_In_Shop)

print("Mean Value:", type(mean_value),mean_value)

# Compute and display the median
median_value = statistics.median(player_values)
print("Median Value:", median_value)

# Compute and display the min and max values
print("Min: €%f, Max: €%f" %(min(player_values),max(player_values)))

# Second smallest unique value
s1 = list(set(sorted(player_values)))
s2 = sorted(s1)
print("Min:", s2[1])
print("Max:", s2[len(s2)-1])
"""