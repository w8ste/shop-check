import plotly.express as px
from .sql import fetch_data

def plot_purchases(config):
    df = fetch_data(config)

    fig = px.line(df, x="created_at", y="number", title=f"Current budget: {config.default_budget}", markers=True)
    fig.update_xaxes(title_text="Timestamp", tickangle=-45)
    fig.update_yaxes(title_text="price")

    return fig
