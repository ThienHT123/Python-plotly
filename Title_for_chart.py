import plotly.express as Chart

x=[1,2,3,4,5,6]
y=[1,2,3,4,5,6]
Draw_line=Chart.line(x=x,y=y,title='My Chart')

print(Draw_line)

Draw_line.show()