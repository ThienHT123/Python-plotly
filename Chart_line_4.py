import plotly.express as Chart
import plotly.graph_objects as Graph
data_frame=Chart.data.iris().head(20)

Draw_Chart=Chart.line(data_frame,x='sepal_width',y='sepal_length',color='sepal_length')

print(Draw_Chart)

Draw_Chart.show()