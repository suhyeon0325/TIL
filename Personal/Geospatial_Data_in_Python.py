# Introduction to geospatial vector data

  # Import pandas and matplotlib
  import pandas as pd
  import matplotlib.pyplot as plt
  
  # Read the restaurants csv file
  restaurants = pd.read_csv("paris_restaurants.csv")
  
  # Inspect the first rows of restaurants
  print(restaurants.head())
  
  # Make a plot of all points
  fig, ax = plt.subplots()
  ax.plot(restaurants['x'], restaurants['y'], 'o')
  plt.show()

# ----------------------------------------------------
  # 레스토랑 데이터 CSV 파일을 읽어옵니다.
  레스토랑 = pd.read_csv("paris_restaurants.csv")
  
  # contextily 패키지를 가져옵니다.
  import contextily
  
  # 배경을 가진 모든 레스토랑 위치를 표시하는 그림을 만듭니다.
  fig, ax = plt.subplots()
  ax.plot(레스토랑['x'], 레스토랑['y'], 'o', markersize=1)
  contextily.add_basemap(ax)
  plt.show()
# ----------------------------------------------------
  # Import GeoPandas
  import geopandas
  
  # Read the Paris districts dataset
  districts = geopandas.read_file('paris_districts.gpkg')
  
  # Inspect the first rows
  print(districts.head())
  
  # Make a quick visualization of the districts
  districts.plot()
  plt.show()
# ----------------------------------------------------
  # Check what kind of object districts is
  print(type(districts))
  
  # Check the type of the geometry attribute
  print(type(districts.geometry))
  
  # Inspect the first rows of the geometry
  print(districts.geometry.head())
  
  # Inspect the area of the districts
  print(districts.area)
# ----------------------------------------------------
  # Read the restaurants csv file into a DataFrame
  df = pd.read_csv("paris_restaurants.csv")

  # Convert it to a GeoDataFrame
  restaurants = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.x, df.y))
  
  # Inspect the first rows of the restaurants GeoDataFrame
  print(restaurants.head())
  
  # Make a plot of the restaurants
  ax = restaurants.plot(markersize=1)
  import contextily
  contextily.add_basemap(ax)
  plt.show()
# ----------------------------------------------------
  # Inspect the first rows of the districts dataset
  print(districts.head())
  
  # Inspect the area of the districts
  print(districts.geometry.area)
  
  # Add a population density column
  districts['population_density'] = districts['population'] / districts.geometry.area * 10**6
  
  # Make a plot of the districts colored by the population density
  districts.plot(column='population_density', legend=True)
  plt.show()
# ----------------------------------------------------
  # Load the restaurants data
  restaurants = geopandas.read_file("paris_restaurants.geosjon")
  
  # Calculate the number of restaurants of each type
  type_counts = restaurants.groupby('type').size()
  
  # Print the result
  print(type_counts)
# ----------------------------------------------------
  # Load the restaurants dataset
  restaurants = geopandas.read_file("paris_restaurants.geosjon")
  
  # Take a subset of the African restaurants
  african_restaurants = restaurants[restaurants['type'] == 'African restaurant']
  
  # Make a multi-layered plot
  fig, ax = plt.subplots(figsize=(10, 10))
  restaurants.plot(ax=ax, color='grey')
  african_restaurants.plot(ax=ax, color='red')
  # Remove the box, ticks and labels
  ax.set_axis_off()
  plt.show()

# Spatial relationships

  # Import the Point geometry
  from shapely.geometry import Point
  
  # Construct a point object for the Eiffel Tower
  eiffel_tower = Point(255422.6, 6250868.9)
  
  # Print the result
  print(eiffel_tower)
# ----------------------------------------------------
  # Accessing the Montparnasse geometry (Polygon) and restaurant
  district_montparnasse = districts.loc[52, 'geometry']
  resto = restaurants.loc[956, 'geometry']
  
  # Is the Eiffel Tower located within the Montparnasse district?
  print(eiffel_tower.within(district_montparnasse))
  
  # Does the Montparnasse district contains the restaurant?
  print(district_montparnasse.contains(resto))
  
  # The distance between the Eiffel Tower and the restaurant?
  print(eiffel_tower.distance(resto))
# ----------------------------------------------------
  # Construct a point object for the Eiffel Tower
  eiffel_tower = Point(255422.6, 6250868.9)
  
  # Create a boolean Series
  mask = districts.contains(eiffel_tower)
  
  # Print the boolean Series
  print(mask.head())
  
  # Filter the districts with the boolean mask
  print(districts[mask])
# ----------------------------------------------------
  # The distance from each restaurant to the Eiffel Tower
  dist_eiffel = restaurants.distance(eiffel_tower)
  
  # The distance to the closest restaurant
  print(dist_eiffel.min())
  
  # Filter the restaurants for closer than 1 km
  restaurants_eiffel = restaurants[dist_eiffel < 1000]
  
  # Make a plot of the close-by restaurants
  ax = restaurants_eiffel.plot()
  geopandas.GeoSeries([eiffel_tower]).plot(ax=ax, color='red')
  contextily.add_basemap(ax)
  ax.set_axis_off()
  plt.show()
# ----------------------------------------------------
  # Read the trees and districts data
  trees = geopandas.read_file("paris_trees.gpkg")
  districts = geopandas.read_file("paris_districts_utm.geojson")
  
  # Spatial join of the trees and districts datasets
  joined = geopandas.sjoin(trees, districts, op='within')
  
  # Calculate the number of trees in each district
  trees_by_district = joined.groupby('district_name').size()
  
  # Convert the series to a DataFrame and specify column name
  trees_by_district = trees_by_district.to_frame(name='n_trees')
  
  # Inspect the result
  print(trees_by_district.head())
# ----------------------------------------------------
  # Merge the 'districts' and 'trees_by_district' dataframes
  districts_trees = pd.merge(districts, trees_by_district, on='district_name')
  
  # Add a column with the tree density
  districts_trees['n_trees_per_area'] = districts_trees['n_trees'] / districts_trees.geometry.area
  
  # Make of map of the districts colored by 'n_trees_per_area'
  districts_trees.plot(column='n_trees_per_area')
  plt.show()
# ----------------------------------------------------
  # Print the first rows of the tree density dataset
  print(districts_trees.head())
  
  # Make a choropleth of the number of trees 
  districts_trees.plot(column='n_trees', legend=True)
  plt.show()
  
  # Make a choropleth of the number of trees per area
  districts_trees.plot(column='n_trees_per_area', legend=True)
  plt.show()
  
  # Make a choropleth of the number of trees 
  districts_trees.plot(column='n_trees_per_area', scheme='equal_interval', legend=True)
  plt.show()
# ----------------------------------------------------
  # Generate the choropleth and store the axis
  ax = districts_trees.plot(column='n_trees_per_area', scheme='Quantiles',
                            k=7, cmap='YlGn', legend=True)
  
  # Remove frames, ticks and tick labels from the axis
  ax.set_axis_off()
  plt.show()
# ----------------------------------------------------
  # Set up figure and subplots
  fig, axes = plt.subplots(nrows=2)
  
  # Plot equal interval map
  districts_trees.plot('n_trees_per_area', scheme = 'equal_interval', k=5, legend=True, ax=axes[0])
  axes[0].set_title('Equal Interval')
  axes[0].set_axis_off()
  
  # Plot quantiles map
  districts_trees.plot('n_trees_per_area', scheme = 'Quantiles', k=5, legend=True, ax=axes[1])
  axes[1].set_title('Quantiles')
  axes[1].set_axis_off()
  
  # Display maps
  plt.show()


# Projecting and transforming geometries

  # Import the districts dataset
  districts = geopandas.read_file("paris_districts.geojson")
  
  # Print the CRS information
  print(districts.crs)
  
  # Print the first rows of the GeoDataFrame
  print(districts.head())
# ----------------------------------------------------
  # Print the CRS information
  print(districts.crs)
  
  # Plot the districts dataset
  districts.plot()
  plt.show()
  
  # Convert the districts to the RGF93 reference system
  districts_RGF93 = districts.to_crs(epsg=2154)
  
  # Plot the districts dataset again
  districts_RGF93.plot()
  plt.show()
# ----------------------------------------------------
