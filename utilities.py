import pandas as pd
import matplotlib.pyplot as plt
import folium
from folium.plugins import FastMarkerCluster

# Set up some default parameters for graphing
from matplotlib import cycler
colour = "#00C2AB" # The default colour for the barcharts
colors = cycler('color',
                ['#4FBBA9', '#E56D13', '#D43A69',
                 '#25539f', '#88BB44', '#FFBBBB'])
plt.rc('axes', facecolor='#E6E6E6', edgecolor='none',
       axisbelow=True, grid=True, prop_cycle=colors)
plt.rc('grid', color='w', linestyle='solid')
plt.rc('xtick', direction='out', color='gray')
plt.rc('ytick', direction='out', color='gray')
plt.rc('patch', edgecolor='#E6E6E6')
plt.rc('lines', linewidth=2)
font = {'family' : 'DejaVu Sans',
        'weight' : 'normal',
        'size'   : 16}
plt.rc('font', **font)
plt.rc('legend', fancybox = True, framealpha=1, shadow=True, borderpad=1)



# This will make all of our charts for us
def charter (full_data, date_column, date_format, mnth_name,
        counting_column, measure, filename, title, function):
    full_data[date_column] = pd.to_datetime(full_data[date_column], format=date_format, errors='coerce') # Format the date
    
    # Organize the data
    this_data = full_data.groupby([date_column])[counting_column].agg(function) # For each day, count the number of inspections/enforcements/violations # Summarize inspections/enforcements/violations on a monthly basis  
    this_data = this_data.loc[((this_data.index.month == 3) | (this_data.index.month == 4))  & (this_data.index.year >= 2001)] # Filter to higher quality data timeframe (post-2001) and back to just the selected month 
    this_data = this_data.resample('Y').sum() # Add together the two months (3 - 4) we're looking at
    this_data = pd.DataFrame(this_data) # Put our data into a dataframe
    this_data = this_data.rename(columns={counting_column: measure}) # Format the data columns
    this_data.index = this_data.index.strftime('%Y') # Make the x axis (date) prettier

    # Create the chart
    ax = this_data.plot(kind='bar', title = ""+title+" in %s of each year across ECHO history" %(mnth_name), figsize=(20, 10), fontsize=16, color=colour)
    ax

    # Label trendline
    trend=this_data[measure].mean()
    ax.axhline(y=trend, color='#e56d13', linestyle='--', label = "Average "+title+" in %s across ECHO history" %(mnth_name))

    # Label the previous three years' trend (2017, 2018, 2019)
    trend_month=pd.concat([this_data.loc["2017"],this_data.loc["2018"],this_data.loc["2019"]])
    trend_month=trend_month[measure].mean()
    ax.axhline(y=trend_month, xmin = .82, xmax=.93, color='#d43a69', linestyle='--', label = "Average for %s 2017-2019" %(mnth_name))

    # Label plot
    ax.legend()
    ax.set_xlabel("March and April of Each Year")
    ax.set_ylabel(title)

    # Export data 
    this_data.to_csv(filename) # This will make all of our charts for us


# Helps us make the map!
# Based on https://medium.com/@bobhaffner/folium-markerclusters-and-fastmarkerclusters-1e03b01cb7b1
def mapper(df):
    # Initialize the map
    m = folium.Map(
        location = [df.mean()["FAC_LAT"], df.mean()["FAC_LONG"]]
    )

    # Create the Marker Cluster array
    #kwargs={"disableClusteringAtZoom": 10, "showCoverageOnHover": False}
    mc = FastMarkerCluster("")
 
    # Add a clickable marker for each facility
    for index, row in df.iterrows():
        mc.add_child(folium.CircleMarker(
            location = [row["FAC_LAT"], row["FAC_LONG"]],
            popup = row["FAC_NAME"] + "<p><a href='"+row["DFR_URL"]+"' target='_blank'>Link to ECHO detailed report</a></p>",
            radius = 8,
            color = "black",
            weight = 1,
            fill_color = "orange",
            fill_opacity= .4
        ))
    
    m.add_child(mc)
    bounds = m.get_bounds()
    m.fit_bounds(bounds)

    # Show the map
    return m