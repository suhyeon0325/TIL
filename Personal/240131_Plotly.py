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
# 3.2. Advanced Customization - Layering multiple plots
# 3.3. Advanced Customization - Time buttons

# 4.1. Advanced Interactivity - Custom buttons
# 4.2. Advanced Interactivity - Dropdowns
# 4.3. Advanced Interactivity - Sliders
