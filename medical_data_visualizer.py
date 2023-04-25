import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('csv/medical_examination.csv')

df['overweight'] = (df['weight'] / (df['height']/100**2))
df['overweight'] = df['overweight'].apply(lambda x: 1 if x > 25 else 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# re-weritten the below as the normalization talks about gluc and cholesterol levels
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1

# Draw Categorical Plot


def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=[
                     'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], ignore_index=True)

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()
    # Draw the catplot with 'sns.catplot()'

    # Get the figure for the output
    fig = sns.catplot(
        x='variable',
        y='total',
        kind='bar',
        hue='value',
        col='cardio',
        data=df_cat
    )

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():

    # Clean the data
    df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) & 
    (df['height'] >= (df['height'].quantile(0.025))) &
    (df['height'] <= (df['height'].quantile(0.975))) &
    (df['weight'] >= (df['weight'].quantile(0.025))) &
    (df['weight'] <= (df['weight'].quantile(0.975)))]
    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(9,9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(
      corr,
      annot=True, 
      fmt='.1f', 
      linewidths=1, 
      mask=mask, 
      vmax=.8, 
      center=0.09,
      square=True, 
      cbar_kws = {'shrink':0.5})


    # Do not modify the next two lines
    fig.savefig('img/heatmap.png')
    return fig

draw_heat_map()