import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

SUNSPOTS = "Sunspotsdata.csv"


def main():

    # Create Data Frame Using Pandas
    sun_df = pd.read_csv(SUNSPOTS, header=None, sep=";")

    # Sanity Check Print
    print(sun_df.head())

    # Calculate Moving Averages
    sun_df['MA_10'] = sun_df[3].rolling(window=10, center=True, min_periods=1).mean()
    sun_df['MA_100'] = sun_df[3].rolling(window=100, center=True, min_periods=1).mean()

    # Plotting

    plt.figure(figsize=(10, 8), dpi=700)
    plt.scatter(x=sun_df[2], y=sun_df[3], color = 'orange')
    plt.plot(sun_df[2], sun_df.MA_10, color='blue', label='10-year Moving Average')
    plt.plot(sun_df[2], sun_df.MA_100, color='red', label='100-year Moving Average')
    plt.grid()
    plt.title("Sunspot Visualization")
    plt.xlabel("Date In Fraction Year")
    plt.ylabel("Mean Monthly Sunspots")
    plt.legend(prop={'size': 8})
    plt.show()

main()

'''
Manual Derivation of Sunspot Cycle 
Find Difference Between Peak Mean Monthly Sunspot and Where Spot Values are 0 
1754-1749 = 5 years 
Values 0 and 96.7
Point 0 and Point 61

Computational Idea:
Find Peak Values using the find_peaks function and also try to find the minimum values using a similar idea 
Then subtract the years of the two data points and average all of the sunspot cycles we measure


'''