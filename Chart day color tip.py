import plotly.express as Chart
import plotly.graph_objects as Graph
import os

os.system("color a")

data_frame=Chart.data.tips()

Chart=Chart.scatter(data_frame,x='day',y='total_bill',color='tip',title='My chart')

print(Chart)

Chart.show()