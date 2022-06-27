import plotly.express as Chart
import plotly.graph_objects as Graph
import os

os.system("color a")

data_frame=Chart.data.iris()

draw=Chart.scatter(data_frame,x='sepal_width',y='sepal_length',facet_col='species',facet_row='species_id',title='My chart')

print(draw)

draw.show()