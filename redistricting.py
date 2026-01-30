import geopandas as gpd

gdf = gpd.read_file("mn_2020_census_blocks_hennepin.geojson")

print(gdf.head())