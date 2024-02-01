# 1.1. Introduction to Plotly - Univariate visualizations

# Create the bar plot
fig = px.bar(data_frame=student_scores, 
             x='student_name', 
             y='score', 
             title='Student Scores by Student')

# Show the plot
fig.show()

# Create the box plot
fig = px.box(
  			# Set the data
  			data_frame=revenues, 
  			# Set the y variable
            y= 'Revenue', 
            # Add in hover data to see outliers
            hover_data=['Company'])

# Show the plot
fig.show()

# Create a simple histogram
fig = px.histogram(
  			data_frame=revenues, 
            # Set up the x-axis
           	x='Revenue',
            # Set the number of bins
            nbins=5)

# Show the plot
fig.show()

# 1.2. Introduction to Plotly - Customizing color
# Create your own continuous color scale
my_scale = ['rgb(255, 0, 0)', 'rgb(3, 252, 40)']

# Create the bar plot
fig = px.bar(data_frame=student_scores, 
             x='student_name', y='score', title='Student Scores by Student',
             # Set the color variable and scale
             color='score',
             color_continuous_scale=my_scale
             )

# Show the plot
fig.show()

# Create the industry-color map
ind_color_map = {'Tech': 'rgb(124, 250, 120)', 'Oil':'rgb(112, 128, 144)' , 
                 'Pharmaceuticals':'rgb(137, 109, 247)', 'Professional Services': 'rgb(255, 0, 0)'}

# Create the basic box plot
fig = px.box(
  			# Set the data and y variable
  			data_frame=revenues, y='Revenue',
  			# Set the color map and variable
			color_discrete_map=ind_color_map,
			color='Industry')

# Show the plot
fig.show()

# Create the industry-color map
ind_color_map = {'Tech': 'rgb(124, 250,120)', 'Oil': 'rgb(112,128,144)', 
                 'Pharmaceuticals': 'rgb(137,109,247)', 
                 'Professional Services': 'rgb(255,0,0)'}

# Create a simple histogram
fig = px.histogram(
  			# Set the data and x variable
  			data_frame=revenues, x='Revenue', nbins=5,
    		# Set the color map and variable
			color_discrete_map=ind_color_map,
			color='Industry')

# Show the plot
fig.show()

# 2.1. Customizing Plots - Bivariate visualizations
# Set up the color map
color_map = {'Adelie': 'rgb(235, 52, 52)' , 'Gentoo': 'rgb(235, 149, 52)', 'Chinstrap': 'rgb(67,52,235)'}

# Create a scatterplot
fig = px.scatter(data_frame=penguins, title="Penguin Culmen Statistics",
    x='Culmen Length (mm)',
    y='Culmen Depth (mm)',
    # Set the colors to use your color map
    color='Species',
    color_discrete_map=color_map
)

# Show your work
fig.show()

# Create a correlation table with pandas
penguin_corr = penguins.corr(method='pearson')

# Set up the correlation plot
fig = go.Figure(go.Heatmap(
  		# Set the appropriate x, y and z values
        z=penguin_corr.values.tolist(),
        x=penguin_corr.columns,
        y=penguin_corr.columns,
  		# Set the color scale,
        colorscale='rdylgn', 
  		# Set min and max values
        zmin=-1, zmax=1))

# Show the plot
fig.show()

# 2.2. Customizing Plots - Customizing hover information and legends
# Create the scatterplot
fig = px.scatter(
        data_frame=life_gdp, 
        x='Life expectancy', 
        y='GDP Per Capita', color='Continent')

# Create the legend
my_legend = {'x': 0.2, 'y': 0.95, 
            'bgcolor': 'rgb(60, 240, 201)', 'borderwidth': 5}

# Update the figure
fig.update_layout({'showlegend': True, 'legend': my_legend})

# Show the plot
fig.show()

# Create the scatterplot
fig = px.scatter(
  data_frame=life_gdp, 
  x='Life expectancy', 
  y='GDP Per Capita',
  color='Continent',
  # Add columns to the hover information
  hover_data=['Country'],
  # Add bold variable in hover information
  hover_name='Country'
)

# Show the plot
fig.show()
# 2.3. Customizing Plots - Adding annotations
# Create the first annotation
loss_annotation = {'x': 10, 'y': 400, 'showarrow': True, 'arrowhead': 4,
                    'font': {'color': 'black'}, 'text': 'Urgent House Repairs'}

# Create the second annotation
gain_annotation = {'x': 18, 'y':2500, 'showarrow': True, 'arrowhead': 4,
                    'font': {'color': 'black'}, 'text': 'New Job!'}

# Add annotations to the figure
fig.update_layout({'annotations': [loss_annotation, gain_annotation]})

# Show the plot!
fig.show()

# Get and format today's date
today = datetime.today().strftime('%A')

# Create the message_annotation
message_annotation = {
  # Set the correct coordinates
  'x': 0.5, 'y': 0.95, 'xref': 'paper', 'yref': 'paper',
  # Set format the text and box
  'text': f'Have a Happy {today} :)',
  'font': {'size': 20, 'color': 'white'},
  'bgcolor': 'rgb(237, 64, 200)', 'showarrow': False}

# Update the figure layout and show
fig.update_layout({'annotations': [message_annotation]})
fig.show()

# 2.4. Customizing Plots - Editing plot axes
# Create and show the plot
fig = px.scatter(
  data_frame=bball_data,
  x='PPG', 
  y='FGP',
  title='Field Goal Percentage vs. Points Per Game')
fig.show()

# Update the x_axis range
fig.update_layout({'xaxis': {'range': [0, bball_data['PPG'].max() + 5]}})
fig.show()

# Update the y_axis range
fig.update_layout({'yaxis': {'range' : [0, 100]}})
fig.show()

# Create timestamp
timestamp = datetime.now()

# Create plot
fig = px.bar(penguins, x='spec', y='av_flip_length', color="spec", title='Flipper Length (mm) by Species')

# Change the axis titles
fig.update_layout({'xaxis': {'title': {'text': 'Species'}},
                  'yaxis': {'title': {'text': 'Average Flipper Length (mm)'}}})

# Add an annotation and show
fig.update_layout({'annotations': [{
  "text": f"This graph was generated at {timestamp}", 
  "showarrow": False, "x": 0.5, "y": 1.1, "xref": "paper", "yref": "paper"}]})
fig.show()

# 3.1. Advanced Customization - Subplots
# Set up the subplots grid
fig = make_subplots(rows=2, cols=2, 
                    # Set the subplot titles
                    subplot_titles=['Tech', 'Professional Services', 'Retail', 'Oil'])

# Add the Tech trace
fig.add_trace(go.Box(x=df_tech.Revenue, name='', showlegend=False), row=1, col=1)
# Add the Professional Services trace
fig.add_trace(go.Box(x=df_prof_serve.Revenue, name='', showlegend=False), row=1, col=2)
# Add the Retail trace
fig.add_trace(go.Box(x=df_retail.Revenue, name='', showlegend=False), row=2, col=1)
# Add the Oil trace
fig.add_trace(go.Box(x=df_oil.Revenue, name='', showlegend=False), row=2, col=2)

# Add a title (and show)
fig.update_layout({'title': {'text': 'Box plots of company revenues', 'x': 0.5, 'y': 0.9}})
fig.show()

# Create the subplots
fig = make_subplots(rows=3, cols=1, shared_xaxes=True)

# Loop through the industries
row_num = 1
for industry in ['Tech', 'Retail', 'Professional Services']:
    df = revenues[revenues.Industry == industry]
    # Add a histogram using subsetted df
    fig.add_trace(go.Histogram(x=df['Revenue'], name=industry),
    # Position the trace
    row=row_num, col=1)
    row_num +=1

# Show the plot
fig.show()

# 3.2. Advanced Customization - Layering multiple plots
# Create the base figure
fig = go.Figure()

# Loop through the species
for species in ['Adelie', 'Chinstrap', 'Gentoo']:
  # Add a bar chart trace
  fig.add_trace(go.Bar(x=islands,
    # Set the appropriate y subset and name
    y=penguins_grouped[penguins_grouped.Species == species]['Count'],
    name=species))
# Show the figure
fig.show()

# Create the base figure
fig = go.Figure()

# Add the bar graph of daily temperatures
fig.add_trace(
  go.Bar(x=temp_syd['Date'], y=temp_syd['Temp'], name='Daily Max Temperature'))

# Add the monthly average line graph
fig.add_trace(
  go.Scatter(x=temp_syd_avg['Date'], y=temp_syd_avg['Average'], name='Average Monthly Temperature'))

# Show the plot
fig.show()

# 3.3. Advanced Customization - Time buttons
# Create the buttons
date_buttons = [
{'count': 4, 'label': "4WTD", 'step': "day", 'stepmode': "todate"},
{'count': 48, 'label': "48HR", 'step': "hour", 'stepmode': "todate"},
{'count': 1, 'label': "YTD", 'step': "year", 'stepmode': "todate"}]

# Create the basic line chart
fig = px.line(data_frame=rain, x='Date', y='Rainfall', 
              title="Rainfall (mm)")

# Add the buttons and show
fig.update_layout(
  	{'xaxis':
    {'rangeselector': {'buttons': date_buttons}}})
fig.show()

# Create the basic line chart
fig = px.line(data_frame=tesla, x='Date', y='Open', title="Tesla Opening Stock Prices")

# Create the financial buttons
fin_buttons = [
  {'count': 7, 'label': "1WTD", 'step': 'day', 'stepmode': 'todate'},
  {'count': 6, 'label': "6MTD", 'step': 'month', 'stepmode': 'todate'},
  {'count': 1, 'label': "YTD", 'step': 'year', 'stepmode': 'todate'}
]

# Create the date range buttons & show the plot
fig.update_layout({'xaxis': {'rangeselector': {'buttons': fin_buttons}}})
fig.show()

# 4.1. Advanced Interactivity - Custom buttons


# 4.2. Advanced Interactivity - Dropdowns
# 4.3. Advanced Interactivity - Sliders
