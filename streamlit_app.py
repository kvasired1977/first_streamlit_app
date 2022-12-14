import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My parents healthy diner')
streamlit.header('πHeader')
streamlit.text('test for text')
streamlit.header('ππ₯­ Build Your Own Fruit Smoothie π₯π')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Banana'])
# Display the table on the page.
#streamlit.dataframe(my_fruit_list)

fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)


#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())
 

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

#create a new function
def get_fruitywise_data(this_fruit_choice):
 fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
 # write your own comment - display the api result in dataframe/table format
 fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
 return fruityvice_normalized
  
streamlit.header('Fruit Advice from Fruityvise')
try:
 fruit_choice = streamlit.text_input('What fruit would you like information about?')
 if not fruit_choice:
   streamlit.error("please select a fruit to get info.")
 else:
   #streamlit.write('The user entered ', fruit_choice)
   back_from_function = get_fruitywise_data(fruit_choice)
   streamlit.dataframe(back_from_function)
except URLError as e:
  strealit.error()

  





streamlit.header("View our Fruit list - Add your favs:")
#snowflake related functions
def get_fruit_load_list():
 with my_cnx.cursor() as my_cur:
  my_cur.execute("SELECT * from fruit_load_list")
  return my_cur.fetchall()

#add a button to load the fruit
if streamlit.button('get fruit load list'):
 my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
 my_data_rows = get_fruit_load_list()
 streamlit.dataframe(my_data_rows)

 #Troubleshooting  
#streamlit.stop()

def insert_row_snowflake(new_fruit):
 with my_cnx.cursor() as my_cur:
  my_cur.execute("insert into fruit_load_list values('" + new_fruit +"')")
  return "thanks for adding " + new_fruit
 
add_fruit = streamlit.text_input('enter another fruit?','test')
if streamlit.button('Add a fruit to the list'):
 my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
 bacxk_from_function = insert_row_snowflake(add_fruit)
 streamlit.text(back_from_function)
streamlit.write('The user entered ', add_fruit)
##

