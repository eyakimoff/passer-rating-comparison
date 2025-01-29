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
# streamlit session state to track whether the extensive data view is active
if "extensive" not in st.session_state:
    st.session_state.extensive = False

# toggle button to switch between extensive and simplified data views
if st.button("Toggle Extensive Data"):
    st.session_state.extensive = not st.session_state.extensive

# display either the simplified or extensive table based on user selection
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


# function to customize the appearance of scatter plots
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


# dataframe with top 25 performances based on Refined Passer Rating
df_top25 = df.nlargest(25, "Refined Passer Rating")

# scatter plot for top 25 performances
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

# select bottom 25 performances based on Refined Passer Rating
df_bottom25 = df.nsmallest(25, "Refined Passer Rating")

# scatter plot for bottom 25 performances
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

# create a new dataframe for comparisons
df_comp = df.copy()

# create an absolute difference column for sorting purposes
df_comp["Passer Rating Difference Absolute"] = abs(df["Passer Rating Difference"])

# select the top 10 games with the largest difference between traditional and refined passer rating
df_comp = df.nlargest(10, "Passer Rating Difference Absolute")

# create a new column concatenating Name, Year, and Week for better visualization
df_comp["Name and Date"] = (
    df_comp["Name"]
    + ", Year: "
    + df_comp["Year"].astype(str)
    + ", Week: "
    + df_comp["Week"].astype(str)
)

# create a grouped bar chart comparing Passer Rating vs Refined Passer Rating
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

# improve layout for readability
comp_fig.update_layout(
    title="Passer Rating vs Refined Passer Rating",
    barmode="group",  # ensure bars don't overlap
    template="plotly_white",  # clean white background for better visualization
)

st.write(
    "The figure below highlights the differences between the traditional passer rating calculation and the refined formula. "
    "It displays the ten games with the largest discrepancies between the two formulas. "
    "The refined formula is notably harsher on poor performances."
)
st.plotly_chart(comp_fig)
