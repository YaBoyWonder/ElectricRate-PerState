import folium
import pandas as pd
import os

states = os.path.join('data', 'us-states.json')

m = folium.Map(location=[48, -102], zoom_start=3)

m.choropleth(
    geo_data=states,
    name='choropleth',
    data=state_data,
    columns=['State', '%'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.6,
    line_opacity=0.3,
    legend_name='Electric Rate Usage %'
)

folium.LayerControl().add_to(m)

m.save('electricRate.html')
