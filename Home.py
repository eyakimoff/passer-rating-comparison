import pandas as pd
import streamlit as st
from utils.data_cleaning import get_dataframe
import plotly.express as px

df = get_dataframe()

st.title("Quarterback Refined Passer Rating Database")
st.subheader("Overview")
st.write(
    "Welcome to the homepage. Below is a table showing the refined passer rating leaderboards. You can toggle between a table which shows extensive game Details, and a simplified table with less game data. This showcases the difference between the traditional passer rating formula and the refined version."
)

if "extensive" not in st.session_state:
    st.session_state.extensive = False

if st.button("Toggle Extensive Data"):
    st.session_state.extensive = not st.session_state.extensive

if st.session_state.extensive:
    st.dataframe(
        df[
            [
                "Name",
                "Year",
                "Season",
                "Week",
                "Opponent",
                "Outcome",
                "Passer Rating",
                "Refined Passer Rating",
                "Passer Rating Difference",
            ]
        ]
    )
else:
    st.dataframe(df)


# Customize the layout of scatter plots
def scatter_plot_update(fig, marker_colour="black"):
    fig.update_traces(
        marker=dict(
            size=1, color=marker_colour, line=dict(width=2, color=marker_colour)
        )
    )
    fig.update_layout(
        hoverlabel=dict(bgcolor=marker_colour, font_size=12, font_family="sans serif"),
        xaxis_title="Year",
        yaxis_title="Refined Passer Rating",
        title_font_size=20,
    )
    return fig


# dataframe with top 25 performances
df_top25 = df.nlargest(25, "Refined Passer Rating")

top25_fig = px.scatter(
    df_top25,
    x=df_top25["Year"],
    y=df_top25["Refined Passer Rating"],
    text=df_top25["Name"],
    hover_data={
        "Refined Passer Rating": True,
        "Year": True,
        "Week": True,
    },
    title="Refined Passer Rating Top 25 Performances",
)

top25_fig = scatter_plot_update(fig=top25_fig, marker_colour="green")
st.plotly_chart(top25_fig)

df_bottom25 = df.nsmallest(25, "Refined Passer Rating")
bottom25_fig = px.scatter(
    df_bottom25,
    x=df_bottom25["Year"],
    y=df_bottom25["Refined Passer Rating"],
    text=df_bottom25["Name"],
    hover_data={
        "Refined Passer Rating": True,
        "Year": True,
        "Week": True,
    },
    title="Refined Passer Rating Bottom 25 Performances",
)
bottom25_fig = scatter_plot_update(fig=bottom25_fig, marker_colour="red")
st.plotly_chart(bottom25_fig)
