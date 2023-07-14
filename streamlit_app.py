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

# Display the pie chart and capture click events
clicked = st.plotly_chart(pie_chart)

# Handle click events on the pie chart
selected_category = None
if st.session_state.get('click_data') and st.session_state['click_data']['points']:
    selected_category = st.session_state['click_data']['points'][0]['label']

# Store click event data in session state
if clicked:
    st.session_state['click_data'] = clicked.event_data

# Apply filters to the data based on the selected category
if selected_category:
    filtered_data = data[data['Category'] == selected_category]
else:
    filtered_data = data

# Create the bar chart with the filtered data
bar_chart = create_bar_chart(filtered_data)
st.plotly_chart(bar_chart)
