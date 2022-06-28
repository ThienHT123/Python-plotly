import plotly.express as Chart
import plotly.graph_objects as Graph
import os

os.system("color a")

data_frame=Chart.data.tips()

draw=Chart.scatter(data_frame,x='sex',y='total_bill',color='tip',title='My chart')

print(draw)

draw.show()