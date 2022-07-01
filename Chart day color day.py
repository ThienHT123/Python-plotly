import plotly.express as Chart
import plotly.graph_objects as Graph
import os

os.system("color a")

data_frame=Chart.data.tips()

plot=Chart.scatter(data_frame,x='day',y='total_bill',color='day',title='My chart')

print(plot)

plot.show()