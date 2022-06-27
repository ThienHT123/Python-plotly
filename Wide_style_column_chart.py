import plotly.express as Chart
import plotly.graph_objects as Graph
import os
os.system("color a")

Wide_style_column_chart=Chart.data.medals_wide()

Draw_Chart=Chart.bar(Wide_style_column_chart,x='nation',y=['gold','silver','bronze'],title="Wide style column chart")

print(Draw_Chart)

Draw_Chart.show()