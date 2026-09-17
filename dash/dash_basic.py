import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

df = pd.read_csv('Dash.csv')

app = Dash()
app.title = "interactive dashboard"

num_cols = df.select_dtypes(include='number').columns

app.layout = html.Div([
    html.H1("Interactive Dashboard with pie plot"),

    html.Label("Select a value to show the pie plot"),

    dcc.Dropdown(
        id='column-dropdown',
        options=[{'label': col, 'value': col} for col in num_cols],
        value=num_cols[0]
    ),

    dcc.Graph(id='pie-plot')
])


@app.callback(
    Output('pie-plot', 'figure'),
    Input('column-dropdown', 'value')
)
def update_pie(selected_col):

    grouped = df.groupby('Area')[selected_col].sum().reset_index()

    fig = px.pie(
        grouped,
        names='Area',
        values=selected_col,
        title=f'distribution of {selected_col} by Area',
        hole=0.3,
        color_discrete_sequence=px.colors.qualitative.Set3
    )

    return fig


if __name__ == '__main__':
    app.run(debug=True)