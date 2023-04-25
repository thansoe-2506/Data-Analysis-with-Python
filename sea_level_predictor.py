import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('csv/epa-sea-level.csv')
    y = df['CSIRO Adjusted Sea Level']
    x = df['Year']

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x, y)


    # Create first line of best fit
    res = linregress(x, y)
    x_pred = pd.Series([i for i in range(1880,2051)])
    y_pred = res.slope*x_pred + res.intercept

    plt.plot(x_pred,y_pred,'g')


    # Create second line of best fit
    df1 = df.loc[df['Year']>=2000]
    x1 = df1['Year']
    y1 = df1['CSIRO Adjusted Sea Level']

    res1 = linregress(x1, y1)
    x_pred1 = pd.Series([i for i in range(2000,2051)])
    y_pred1 = res1.slope*x_pred1 + res1.intercept

    plt.plot(x_pred1,y_pred1,'r')



    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Lavel(inches)')

    ax.set_title('Rise in Sea Lave')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('img/sea_level_plot.png')
    return plt.gca()

draw_plot()