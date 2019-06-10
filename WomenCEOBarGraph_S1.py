import pandas as pd
from plotly.offline import  plot
import plotly.graph_objs as go
import plotly.io as pio

#Importing the Data
df = pd.read_excel('wo.xlsx', sheet_name = 'women_CEOs')





trace = go.Bar(x= df['Year'], 
               y=df['Percentages'],
              )
                
layout = go.Layout(
                   #Title of the Graph
                   title = 'Share of CEOs',
                   
                   #Name of the X-axis
                   xaxis=go.layout.XAxis(
                            title=go.layout.xaxis.Title(
                            text='Year'
                            
                        )
                    ),
                  
                   #Name of Y-axis 
                   yaxis=go.layout.YAxis(
                            title=go.layout.yaxis.Title(
                            text='Percentages'
                        )
                    )
                  )


fig = go.Figure(data=[trace], layout=layout)


plot(fig)

pio.write_image(fig, 'images/fig1.jpeg')


