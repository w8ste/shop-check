import plotly.express as px
from .sql import fetch_data

def plot_purchases():
    df = fetch_data()

    fig = px.line(df, x="created_at", y="number", title="Number Over Time", markers=True)
    fig.update_xaxes(title_text="Timestamp", tickangle=-45)
    fig.update_yaxes(title_text="Number")

    return fig