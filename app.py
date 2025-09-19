import streamlit as st
import numpy as numpy
import matplotlib.pyplot as pyplot
import seaborn as sns
import pandas as pd
import numpy as np
# st.title("Hello many worlds!")
#

# df = pd.DataFrame({"A":[1,2,3,4], "B":[5,6,7,8]})

# # st.write("st.write:")
# # st.write(df)

# # st.write("st.table:")
# # st.table(df)

# # st.write("st.dataframe:")
# # st.dataframe(df)

# chart_data = pd.DataFrame(
#     numpy.random.randn(20, 3),
#     columns=['a', 'b', 'c'])

# st.write("Chart data:")
# st.write(chart_data)

# st.write("st.line_chart:")
# st.line_chart(chart_data)

# st.write("st.area_chart:")
# st.area_chart(chart_data)

# st.write("st.bar_chart:")
# st.bar_chart(chart_data)


# map_data = pd.DataFrame(
#     numpy.random.randn(1000, 2) / [50, 50] + [52.52, 13.405],
#     columns=['lat', 'lon'])

# st.write("st.map:")
# st.map(map_data)

tabs = st.tabs(["charts", "help"])


with tabs[0]:

    st.header("Charts")
    st.write("This is the charts tab.")

    col1, col2 = st.columns(2)

    with col1:
        with st.expander("Function settings"):
            st.write("This is the sidebar")
            x = np.linspace(0, np.pi * 2, 100)

            t = st.slider("t", 0.0, 10.0, 1.0, key="frequency")

            x0 = st.slider("x0", 0.0, np.pi * 2, 0.0)

            y = np.sin(x*t+x0)

            function_name = st.selectbox("Function", ["sin", "cos", "tan"])
            function_dict = {"sin": np.sin, "cos": np.cos, "tan": np.tan}

    with col2:
        if st.checkbox("Show line chart", True):
            y = function_dict[function_name](x*t+x0)
            st.line_chart(pd.DataFrame({f"{function_name}(x*t+x0)": y},) )

with tabs[1]:
    st.header("Help")
    st.write("This is the help tab.")
    st.write("""
    This is a simple Streamlit app that demonstrates various features of Streamlit, including:
    - Displaying dataframes and charts
    - Using tabs and columns for layout
    - Adding interactivity with widgets like sliders, checkboxes, and select boxes
    - Creating expandable sections with expanders

    You can use the controls in the sidebar to adjust the parameters of the function being plotted in the charts tab.
    """)

st.write(st.session_state["frequency"])