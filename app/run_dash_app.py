import os

import pandas as pd
import plotly
import plotly.express as px
import pdb

import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly_layout import layout
from dash.dependencies import Input, Output, State


print(os.listdir('./app'))


# Data
df = pd.read_csv('./app/data/data.csv')
df_kpi = pd.read_csv('./app/data/data_kpi.csv')

default_kpi_option = df_kpi.columns[2]
default_df_option = df.columns[2]


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.config['suppress_callback_exceptions'] = True

style={'backgroundColor':'blue'}
app.layout = html.Div([

                # First component
                html.Div([
                    html.H1('QS', style={"text-align": "center",
                                         "font-size": "55px",
                                         "font-family": 'Signika',
                                         "color": '#70098a',
                                         'backgroundColor': '#ffffff'}),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Label('KPI',
                                            style={"text-align": "right",
                                                 'margin-right': '1em',
                                                 "font-size": "20px",
                                                 "font-family": 'Signika',
                                                 "color": '#70098a',
                                                 'backgroundColor': '#ffffff'}),

                                    html.H6(style={'margin-right': '16em', 'backgroundColor': '#70088a', 'title':'ciao'})
                                ],
                            ),

                            dcc.Dropdown(
                                id='option_selected_kpi',
                                options=[{'label': x, 'value': x} for x in df_kpi.columns],
                                value=[default_kpi_option],
                                multi=True,
                                style=dict(
                                    width='70%',
                                    verticalAlign="middle",
                                )
                            )
                        ],
                        style=dict(display='flex', style={'textAlign': 'middle', 'backgroundColor': '#70088a'}),
                    ),
                    dcc.Graph(id='our_graph_kpi')
                ],
                    style=dict(style={'backgroundColor': '#70088a'})
                ),

                # Space
                html.Br(),
                html.Br(),

                # Second component
                html.Div([
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Label('ALL',
                                               style={"text-align": "right",
                                                      'margin-right': '1em',
                                                      "font-size": "20px",
                                                      "font-family": 'Signika',
                                                      "color": '#70098a',
                                                      'backgroundColor': '#ffffff'}),

                                    html.H6(style={'margin-right': '16em', 'backgroundColor':'#70088a'})
                                ],
                            ),

                            dcc.Dropdown(
                                id='option_selected',
                                options=[{'label':x, 'value': x} for x in df.columns],
                                value=[default_df_option],
                                multi=False,
                                style=dict(
                                    width='70%',
                                    verticalAlign="middle",
                                )
                            )
                        ],
                        style=dict(display='flex', style={'textAlign': 'middle', 'backgroundColor':'#70088a'}),
                    ),
                dcc.Graph(id='our_graph')
                ],
                style=dict(style={'backgroundColor':'#70088a'})
                ),
])


@app.callback(
    dash.dependencies.Output('our_graph', 'figure'),
    [dash.dependencies.Input('option_selected', 'value')])
def update_output(option_selected):
    print(option_selected)
    df_sper = df.copy()
    df_sper = df_sper.set_index('day')
    df_sper = df_sper[option_selected].dropna()
    df_sper = df_sper.reset_index()

    # container = 'You have selected "{}"'.format(option_selected)

    fig = px.line(df_sper, x="day", y=option_selected)
    fig.update_layout(**layout)
    fig.update_traces(line_color='#70088a', mode='lines+markers')

    return fig


@app.callback(
    dash.dependencies.Output('our_graph_kpi', 'figure'),
    [dash.dependencies.Input('option_selected_kpi', 'value')])
def update_output(option_selected):
    print(option_selected)
    df_sper = df_kpi.copy()
    df_sper = df_sper.set_index('day')
    df_sper = df_sper[option_selected].dropna()
    df_sper = df_sper.reset_index()

    fig = px.line(df_sper, x="day", y=option_selected, color_discrete_map={'H':'royalblue','M':'orange','L':'firebrick'})
    fig.update_layout(**layout)
    fig.update_traces(mode='lines+markers', marker=dict(color="MediumPurple"))

    return fig



if __name__ == '__main__':
    app.run_server(debug=True)
