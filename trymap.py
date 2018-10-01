# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np

#df=pd.read_csv()
df=pd.DataFrame(['2012','2013','2014','2015','2016','2017'], columns=['pctRentChange'])
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Lindsay Moore'),
    dcc.Dropdown(id='id-dropdown',options = [{'label':i}
        for i in df['pctRentChange'].values],
        multi=True,value=[]
        ),
    html.Div(children='''
        311 Report Bias as a proxy for demographic change: A correction on NYC rental price predictions.
    '''),

    html.Iframe(srcDoc = open('Graffiti_2017_map.html', 'r').read(), style={'border': 'none', 'width': '50%', 'height': 700}),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)