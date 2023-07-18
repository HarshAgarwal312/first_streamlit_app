import streamlit
import pandas 
import requests
import snowflake.connector
from urllib.error import URLError


my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title("My Parents New Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text("🥣 Omega 3 and Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#streamlit.dataframe(my_fruit_list)

#Put up a multiselect/ pick list for users to pick fruits they want
#streamlit.multiselect("Pick fruits of your choice: ",list(my_fruit_list['Fruit']))
#streamlit.multiselect("Pick fruits of your choice: ",list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_selected = streamlit.multiselect("Pick fruits of your choice: ",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#requests/api part
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get('https://fruityvice.com/api/fruit/'+ fruit_choice)
  #streamlit.text(fruityvice_response.json()) as data is now in df form
  fruityvice_normalize = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalize

#streamlit.write('User wants to know about: ',fruit_choice)
streamlit.header('FruityVice Fruit Advice')
try:
  fruit_choice = streamlit.text_input('Which fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:  
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
    
except URLError as e:
  streamlit.error()

#connecting to snowflake account and displaying account details
streamlit.header("The Fruit Load list contains:")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cnx:
    #my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
    my_cur.execute("select * from FRUIT_LOAD_LIST")
    return my_cur.fetchall()

#Adding a button to load fruit
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list
  #streamlit.text("Hello from Snowflake:")
  streamlit.dataframe(my_data_rows)

#Allow the end user to ad a fruit to list
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as  my_cnx:
    my_cur.execute('insert into FRUIT_LOAD_LIST values ('from streamlit')')
    return "Thanks for adding "+ new_fruit
add_fruit = streamlit.text_input('Which fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_fruit)
  streamlit.text(back_from_function)



#streamlit.write('Thanks for adding ',add_fruit)
#my_cur.execute("insert into FRUIT_LOAD_LIST values('from streamlit')")

#streamlit.subheader("Breakfast Menu")
#items = ['Omega 3 and Blueberry Oatmeal','Kale, Spinach & Rocket Smoothie','Hard-Boiled Free-Range Egg']
#streamlit.markdown("\n".join(items))
