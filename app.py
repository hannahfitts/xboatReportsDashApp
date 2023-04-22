import dash
from dash import html
from dash import dcc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

app = dash.Dash()

# get data

df = pd.read_csv("/Users/hfitts/Downloads/23-02-27-07-12-04_704D_XBoat_raw.csv")
df.columns = [col.strip() for col in df.columns]

# create a dropdown

app.layout = html.Div(id='parent', children=[
    html.H1(id='H1', children='Testing XBoat Dash App', style={'textAlign': 'center',
                                                                      'marginTop': 40, 'marginBottom': 40}),

    dcc.Dropdown(id='field_dropdown',
                 options=[
                     {'label': 'Acceleration', 'value': 'rawAcceleration'},
                     {'label': 'Starboard Force', 'value': 'starboardAdjustedForce'},
                     {'label': 'Starboard Angle', 'value': 'starboardOarAngle'},
                 ],
                 value='starboardOarAngle'),
    dcc.Graph(id='raw_plot')
])


# choose your field to plot // callback

@app.callback(Output(component_id='raw_plot', component_property='figure'),
              [Input(component_id='field_dropdown', component_property='value')])
# plot the data
def graph_update(dropdown_value):
    print(dropdown_value)
    fig = go.Figure([go.Scatter(x=df['recordTimeStamp'], y=df['{}'.format(dropdown_value)],
                                mode="lines", name=dropdown_value, connectgaps=True)
                     ])

    fig.update_layout(title='Raw Data over Session',
                      xaxis_title='Timestamps',
                      yaxis_title='Raw Data'
                      )
    return fig


if __name__ == '__main__':
    app.run_server()
