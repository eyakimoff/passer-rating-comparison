import pandas as pd
import streamlit as st
from utils.data_cleaning import get_dataframe
import plotly.express as px
import plotly.graph_objects as go

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
    title="Refined Passer Rating Top 25 Performances (1970-2016)",
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
    title="Refined Passer Rating Bottom 25 Performances (1970-2016)",
)
bottom25_fig = scatter_plot_update(fig=bottom25_fig, marker_colour="red")
st.plotly_chart(bottom25_fig)
df_comp = df
df_comp["Passer Rating Difference Absolute"] = abs(df["Passer Rating Difference"])
df_comp = df.nlargest(10, "Passer Rating Difference Absolute")
df_comp["Name and Date"] = (
    df_comp["Name"]
    + ", Year: "
    + df_comp["Year"].astype(str)
    + ", Week: "
    + df_comp["Week"].astype(str)
)

comp_fig = go.Figure(
    data=[
        go.Bar(
            name="Passer Rating", x=df_comp["Name and Date"], y=df_comp["Passer Rating"]
        ),
        go.Bar(
            name="Refined Passer Rating",
            x=df_comp["Name and Date"],
            y=df_comp["Refined Passer Rating"],
        ),
    ]
)

comp_fig.update_layout(
    title="Passer Rating vs Refined Passer Rating",
    barmode="group",  # Ensure bars and line don't stack
    template="plotly_white",  # Optional: clean white background
)

st.write(
    "The figure below highlights the differences between the traditional passer rating calculation and the refined formula. It displays the ten games with the largest discrepancies between the two formulas. The refined formula is notably harsher on poor performances."
)
st.plotly_chart(comp_fig)
