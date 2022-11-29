import streamlit
import pandas
streamlit.title('My parents healthy diner')
streamlit.header('😀Header')
streamlit.text('test for text')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
