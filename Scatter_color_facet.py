import plotly.express as Chart
import plotly.graph_objects as Graph
import os
os.system("color a")
data_frame=Chart.data.iris()
draw=Chart.scatter(data_frame,x='species',y='sepal_length',color='species',title='My Chart',facet_col='species',facet_row='species_id')

print(draw)

draw.show()