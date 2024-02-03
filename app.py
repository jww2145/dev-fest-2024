from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Name Pending', style={'textAlign':'center'}),
    html.Div(children='Write Here', className = 'form', contentEditable='true'),

])



if __name__ == '__main__':
    app.run(debug=True)