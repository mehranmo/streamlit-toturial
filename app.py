import streamlit as st
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Simple Streamlit App",
    page_icon="🚀",
    layout="wide"
)

# Main title
st.title("🚀 Simple Streamlit Tutorial App")

# Welcome message
st.write("Welcome to this simple Streamlit application!")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a section:", ["Home", "Data Visualization", "Interactive Widgets"])

if page == "Home":
    st.header("Welcome to the Home Page")
    st.write("""
    This is a simple Streamlit application created as a tutorial example.
    
    **Features included:**
    - Basic text and markdown rendering
    - Interactive widgets
    - Data visualization
    - Sidebar navigation
    """)
    
    # Display some basic info
    st.info("This app demonstrates basic Streamlit functionality!")

elif page == "Data Visualization":
    st.header("📊 Data Visualization")
    
    # Generate sample data
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Column A', 'Column B', 'Column C']
    )
    
    st.subheader("Sample Line Chart")
    st.line_chart(chart_data)
    
    st.subheader("Sample Bar Chart")
    st.bar_chart(chart_data)
    
    # Display the data table
    st.subheader("Sample Data Table")
    st.dataframe(chart_data)

elif page == "Interactive Widgets":
    st.header("🎛️ Interactive Widgets")
    
    # Text input
    name = st.text_input("Enter your name:", "")
    if name:
        st.write(f"Hello, {name}! 👋")
    
    # Slider
    age = st.slider("Select your age:", 0, 100, 25)
    st.write(f"Your age: {age}")
    
    # Selectbox
    color = st.selectbox("Choose your favorite color:", ["Red", "Green", "Blue", "Yellow"])
    st.write(f"Your favorite color is: {color}")
    
    # Checkbox
    if st.checkbox("Show celebration"):
        st.balloons()
        st.success("🎉 Celebration mode activated!")
    
    # Button
    if st.button("Click me!"):
        st.write("Button was clicked! ✨")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")