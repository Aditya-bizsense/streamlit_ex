import streamlit as st

# st.header('st.button')

# if st.button('Click me!'):
#     st.write('Button clicked!')
# else:
#     st.write('Goodbye!')

# import numpy as np
# import altair as alt
# import pandas as pd
# import streamlit as st

# st.header('st.write')

# # Example 1

# st.write('Hello, *World!* :sunglasses:')

# # Example 2

# st.write(1234)

# # Example 3

# df = pd.DataFrame({
#      'first column': [1, 2, 3, 4],
#      'second column': [10, 20, 30, 40]
#      })
# st.write(df)

# # Example 4

# st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# # Example 5

# df2 = pd.DataFrame(
#      np.random.randn(200, 3),
#      columns=['a', 'b', 'c'])
# c = alt.Chart(df2).mark_circle().encode(
#      x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
# st.write(c)

# import streamlit as st
# from datetime import datetime, time

# st.header('st.slider')

# # example 1

# st.subheader('Slider')
# age = st.slider('How old are you?', 0, 130, 25)
# st.write("I'm ", age, ' years old.')

# # example 2

# st.subheader('Range slider')
# values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
# st.write('Values:', values)

# # example 3

# st.subheader('Range time slider')
# wake = st.slider('When do you wake up?', time(6, 0), time(12, 0), time(8, 0))
# st.write('You wake up at: ', wake)

# # example 4

# st.subheader('Datetime slider')
# start_time = st.slider('When do you start?', value=datetime(2021, 1, 1, 9, 30)
#     , format="MM/DD/YYYY - hh:mm")
# st.write('Start time:', start_time)



# # import streamlit as st

# # st.header('st.multiselect')

# # options = st.multiselect(
# #      'What are your favorite colors',
# #      ['Green', 'Yellow', 'Red', 'Blue'],
# #      ['Yellow', 'Red'])

# # st.write('You selected:', options)




# st.header('st.checkbox')

# st.write ('What would you like to order?')

# icecream = st.checkbox('Ice cream')
# coffee = st.checkbox('Coffee')
# cola = st.checkbox('Cola')
# burger = st.checkbox('Burger')

# if icecream:
#      st.write("Great! Here's some more 🍦")

# if coffee: 
#      st.write("Okay, here's some coffee ☕")

# if cola:
#      st.write("Here you go 🥤")

# if burger:
#      st.write("Here's your burger 😍")



# import pandas as pd
# from ydata_profiling import ProfileReport
# from streamlit_pandas_profiling import st_profile_report

# st.header('`streamlit_pandas_profiling`')

# df = pd.read_csv('TB_Burden_Country.csv')

# pr = ProfileReport(df, explorative=True, minimal=True)
# st_profile_report(pr)



st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")
number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)