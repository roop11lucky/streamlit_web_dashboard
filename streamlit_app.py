import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Count': [10, 20, 15, 30]
})

# Create a bar chart function
def create_bar_chart(data):
    fig = px.bar(data, x='Category', y='Count')
    return fig

# Create a pie chart function
def create_pie_chart(data):
    fig = px.pie(data, values='Count', names='Category')
    return fig

# Set the title of the dashboard
st.title('Interactive Dashboard')

# Create the pie chart
pie_chart = create_pie_chart(data)
pie_clicked = st.plotly_chart(pie_chart)

# Handle click events on the pie chart
selected_category = None
if pie_clicked:
    clicked_data = pie_clicked.expand_data()
    if clicked_data and 'points' in clicked_data[0]:
        selected_category = clicked_data[0]['points'][0]['label']

# Apply filters to the data based on the selected category
if selected_category:
    filtered_data = data[data['Category'] == selected_category]
else:
    filtered_data = data

# Create the bar chart with the filtered data
bar_chart = create_bar_chart(filtered_data)
st.plotly_chart(bar_chart)
