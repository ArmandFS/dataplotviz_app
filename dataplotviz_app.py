#import libraties
import plotly.express as px
import streamlit as st
import pandas as pd

#generate dataframe
df = px.data.gapminder()

#streamlit widgets
st.title("📊Animated Plotly Visualization Project📊")
st.write(df)

#have dataframe into list
year_options = df['year'].unique().tolist()
st.write("Select year via scrollbar to view scatter plot", font="large")

#create scatterplot
fig = px.scatter(df, x="gdpPercap", y ="lifeExp", 
                 size="pop",
                 color ="continent",
                 hover_name="continent",
                 log_x=True, 
                 size_max=60,
                 range_x=[100, 100000],
                 range_y=[25,90],
                 animation_frame="year",
                 animation_group="country")

#updating layout and plotly customizing
fig.update_layout(
    title="Life Expectancy vs. GDP per Capita",
    xaxis_title="GDP per Capita (log scale)",
    yaxis_title="Life Expectancy",
    width=1200, height=700,
    showlegend=True,
    legend_title="Continent",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

#Custom color palette
fig.update_traces(marker=dict(line=dict(width=0.5, color='DarkSlateGrey')), selector=dict(mode='markers'))

#Add interactivity and tooltips
fig.update_traces(hoverinfo="text+name", hovertext="Country: %{hovertext}<br>GDP per Capita: %{x:.2f}<br>Life Expectancy: %{y:.2f}<extra></extra>")

#annotations
fig.add_annotation(x=50000, y=80, text="High GDP, High Life Expectancy", showarrow=True, arrowhead=1)
fig.add_annotation(x=300, y=30, text="Low GDP, Low Life Expectancy", showarrow=True, arrowhead=1)


# Show the plot
st.plotly_chart(fig)

