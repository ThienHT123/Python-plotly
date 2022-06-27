import plotly.express as Chart
import plotly.graph_objects as Graph
import os
os.system("color a")

Data_frame=Chart.data.iris()
Draw_Chart=Chart.bar(Data_frame,x='sepal_width',y='sepal_length',title="My column chart")

print(Draw_Chart)

Draw_Chart.show()