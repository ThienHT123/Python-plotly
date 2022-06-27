import plotly.express as Chart
import plotly.graph_objects as Graph
import os

os.system("color a")

Long_style_data_frame=Chart.data.medals_long()

Draw_Chart=Chart.bar(Long_style_data_frame,x='nation',y='count',color='medal',title='Long style column chart')

print(Draw_Chart)

Draw_Chart.show()