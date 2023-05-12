'''
Nathaniel Yee
May 22nd 2023
DS 2500
'''
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
SPY = 'SPY.csv'

def reader(FILE):
    """Function reader
    Param: File
    Does: Reads in the SPY CSV and creates a date time conversion and takes that df and makes a month column
    """
    df = pd.read_csv(SPY)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month
    return df

def create_objects(df):
    """Function: create objects
    Params: df
    Does creates a new dataframe that is a dictionary
    """
    df_2 = pd.DataFrame({'Date':df['Date'],'Volume':df['Volume'],'Month':df['Month']})
    return df_2


def plotting(df,x,y,hue,size):
    """Function plotting
    Param: df,x,y,hue,size
    Does: Plots a relplot of volumes of the SPY throughout history
    """
    plt.figure(figsize=(12,6))
    sns.relplot(df,x=x,y=y,hue=hue,size=size,sizes=(50,500),palette='coolwarm')
    plt.title("Date vs. Volume traded of SPY From May 1993 to May 2023")
    plt.tight_layout()
    plt.show()
    pass

def main():
    # Initialize the Data
    SPY = reader('SPY')
    #print(SPY)
    # Create the Data frame objects
    objects = create_objects(SPY)
    # Sanity Check print
    print(objects)
    # Begin the plotting by calling the plotting function
    plotting(SPY,x=objects.Date,y=objects.Volume, hue='Volume',size='Volume')
    pass
if __name__ == "__main__":
    main()