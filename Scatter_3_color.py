import plotly.express as Chart
import plotly.graph_objects as Graph
import os

os.system("color a")

data_frame=Chart.data.iris()

draw=Chart.scatter(data_frame,x='petal_width',y='sepal_length',color='species',title='My chart')

print(draw)

draw.show()