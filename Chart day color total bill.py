import plotly.express as Chart
import plotly.graph_objects as Graph
import os

os.system("color a")

data_frame=Chart.data.tips()

draw=Chart.scatter(data_frame,x='day',y='total_bill',color='total_bill',title='My chart')

print(draw)

draw.show()