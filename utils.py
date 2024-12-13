import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import seaborn as sns
from typing import List

def two_bar_subplots(df1_x: pd.DataFrame, df2_x: pd.DataFrame, df1_y: pd.DataFrame, df2_y: pd.DataFrame,
                     title_1: str, title_2: str, y1_label: str, y2_label: str,
                     x1_ticks: pd.DataFrame, x2_ticks: pd.DataFrame, color_palette: sns.color_palette) -> None:
    """Create two bar subplots with the specified parameters.
    Parameters
    ----------
    df1_x : pd.DataFrame
        The x-axis values for the first dataframe.
    df2_x : pd.DataFrame
        The x-axis values for the second dataframe.
    df1_y : pd.DataFrame
        The y-axis values for the first dataframe.
    df2_y : pd.DataFrame
        The y-axis values for the second dataframe.
    title_1 : str
        The title for the first subplot.
    title_2 : str
        The title for the second subplot.
    y1_label : str
        The y-axis label for the first subplot.
    y2_label : str
        The y-axis label for the second subplot.
    x1_ticks : pd.DataFrame
        The x-axis ticks for the first subplot.
    x2_ticks : pd.DataFrame
        The x-axis ticks for the second subplot.
    color_palette : sns.color_palette :
        The color palette to use for the bars.
    Returns
    -------
    None
    """
    fig, axes = plt.subplots(1, 2, figsize=(20, 5))
    # Bar Chart 1
    ax1 = sns.barplot(x=df1_x, y=df1_y, ax=axes[0], palette=color_palette)
    ax1.bar_label(ax1.containers[0])
    axes[0].set_title(title_1)
    axes[0].set_xticklabels(rotation=45, labels=x1_ticks, ha='right')
    axes[0].set_ylabel(y1_label)
    # Bar Chart 2
    ax2 = sns.barplot(x=df2_x, y=df2_y, ax=axes[1], palette=color_palette)
    ax2.bar_label(ax2.containers[0])
    axes[1].set_title(title_2)
    axes[1].set_xticklabels(rotation=45, labels=x2_ticks, ha='right')
    axes[1].set_ylabel(y2_label)

def two_bar_subplots_legend(df1: pd.DataFrame, df2: pd.DataFrame, x1: str, x2: str, y1: str, y2: str, hue_1: str, hue_2: str,
                            title_1: str, title_2: str, y1_label: str, y2_label: str,
                            x1_ticks: pd.DataFrame, x2_ticks: pd.DataFrame, color_palette: sns.color_palette) -> None:
    """Create two bar subplots with the specified parameters.
    Parameters
    ----------
    df1 : pd.DataFrame
        The first dataframe.
    df2 : pd.DataFrame
        The second dataframe.
    x1 : str
        The x-axis column for the first dataframe.
    x2 : str
        The x-axis column for the second dataframe.
    y1 : str
        The y-axis column for the first dataframe.
    y2 : str
        The y-axis column for the second dataframe.
    hue_1 : str
        The hue column for the first dataframe.
    hue_2 : str
        The hue column for the second dataframe.
    title_1 : str
        The title for the first subplot.
    title_2 : str
        The title for the second subplot.
    y1_label : str
        The y-axis label for the first subplot.
    y2_label : str
        The y-axis label for the second subplot.
    x1_ticks : pd.DataFrame
        The x-axis ticks for the first subplot.
    x2_ticks : pd.DataFrame
        The x-axis ticks for the second subplot.
    color_palette : sns.color_palette :
        The color palette to use for the bars.
    Returns
    -------
    None
    """
    fig, axes = plt.subplots(1, 2, figsize=(20, 5))
    # Bar Chart 1
    ax1 = sns.barplot(data=df1, x=x1, y=y1, hue=hue_1, dodge=False, ax=axes[0], palette=color_palette)
    for container in ax1.containers:
        ax1.bar_label(container)
    axes[0].set_title(title_1)
    axes[0].set_xticklabels(rotation=45, labels=x1_ticks, ha='right')
    axes[0].set_ylabel(y1_label)
    # Bar Chart 2
    ax2 = sns.barplot(data=df2, x=x2, y=y2, hue=hue_2, dodge=False, ax=axes[1], palette=color_palette)
    for container in ax2.containers:
        ax2.bar_label(container)
    axes[1].set_title(title_2)
    axes[1].set_xticklabels(rotation=45, labels=x2_ticks, ha='right')
    axes[1].set_ylabel(y2_label)

def two_pie_subplots(df1: pd.DataFrame, df2: pd.DataFrame, df1_labels: pd.DataFrame, df2_labels: pd.DataFrame,
                     title_1: str, title_2: str, color_palette: sns.color_palette) -> None:
    """Create two pie chart subplots with the specified parameters.
    Parameters
    ----------
    df1 : pd.DataFrame
        The first dataframe.
    df2 : pd.DataFrame
        The second dataframe.
    df1_labels : pd.DataFrame
        The labels for the first pie chart.
    df2_labels : pd.DataFrame
        The labels for the second pie chart.
    title_1 : str
        The title for the first subplot.
    title_2 : str
        The title for the second subplot.
    color_palette : sns.color_palette :
        The color palette to use for the pie charts.
    Returns
    -------
    None
    """
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    # Chart 1
    axes[0].pie(df1, labels=df1.index,
                    autopct=lambda pct: detailed_labels(pct, df1),
                    startangle=100, colors=color_palette)
    axes[0].set_title(title_1)
    # Chart 2
    axes[1].pie(df2, labels=df2.index,
                    autopct=lambda pct: detailed_labels(pct, df2),
                    startangle=100, colors=color_palette)
    axes[1].set_title(title_2)

def basemap_map(scaling_factor: int, df: pd.DataFrame, min_lat: int, max_lat: int, min_lon: int, max_lon: int,
                labels_dict: dict, title: str) -> None:
    """Create a basemap map with the specified parameters.
    Parameters
    ----------
    scaling_factor : int
        The scaling factor for the map.
    df : pd.DataFrame
        The dataframe.
    min_lat : int
        The minimum latitude value.
    max_lat : int
        The maximum latitude value.
    min_lon : int
        The minimum longitude value.
    max_lon : int
        The maximum longitude value.
    labels_dict : dict
        The dictionary containing the labels and latitude, longitude coordinates for the basemap map.
    title: str
        The title of the map.
    Returns
    -------
    None
    """
    # Set marker sizes
    marker_sizes = {label: value / scaling_factor for label, value in df.items()}

    # Draw the Basemap
    plt.figure(figsize=(15, 20))
    m = Basemap(projection='merc', llcrnrlat=min_lat, urcrnrlat=max_lat, llcrnrlon=min_lon, urcrnrlon=max_lon, resolution='i')
    m.drawcoastlines()
    m.drawcountries()
    m.drawmapboundary(fill_color='aqua')
    m.fillcontinents(color='lightgray', lake_color='aqua')

    # Add labels to Basemap
    for label, (lat, lon) in labels_dict.items():
        x, y = m(lon, lat)
        m.plot(x, y, 'ro', markersize=marker_sizes[label], label=f'{label}\nInfections: {df[label]}')
        plt.text(x, y, label, fontsize=8, ha='left')
        
    # Set title, legend, and show the plot
    plt.title(title)
    plt.legend()
    plt.show()
    
    
def convert_columns(df_list: list, to_float: list, to_str: list) -> dict:
    """Convert columns to specified datatypes.
        Column names that are within the 'to_float' list are converted to `float` datatype.
        Column names that are within the 'to_str' list are converted to `string` datatype.
        Column names that contain the word 'date' are converted to `datetime` datatype.
        Parameters
        ----------
        df_list : list
            A list of dataframes.
        to_float : list
            A list of columns names to be converted to `float` datatype.
        to_str : list
            A list of columns names to be converted to `string` datatype.
        Returns
        -------
        df_list : list
            A list of dataframes with the specified datatypes.
    """
    for df in df_list:
        if df.index.name:
            col_list = [df.index.name] + df.columns.tolist()
        else:
            col_list = df.columns.tolist()
        for col in col_list:
            if re.search(r'(^|_)date\b', col):
                df[col] = df[col].replace(' ', np.nan)
                df[col] = pd.to_datetime(df[col])
            if col in to_float:
                df[col] = df[col].replace('-', np.nan)
                df[col] = df[col].astype(float)
            if col in to_str:
                df[col] = df[col].astype(str)
    return df_list

def map_category(value: str, keywords: dict) -> str:
    """Return a category name based on the keyword that was found within the value.
    If none of the keywords are found within the value, return 'Other'
    """
    for keyword, keyword_value in keywords.items():
        if keyword in value.lower():
            return keyword_value
    return "Other"

def detailed_labels(pct, allvals):
    """Return a string with the absolute value and percentage of the total.
    """
    absolute = int(round(pct/100.*sum(allvals)))
    return f"{absolute}\n({pct:.1f}%)"