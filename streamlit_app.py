import streamlit
import pandas 
import requests
import snowflake.connector


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
fruit_choice = streamlit.text_input('Which fruit would you like information about?','kiwi')
streamlit.write('User wants to know about: ',fruit_choice)

streamlit.header('FruityVice Fruit Advice')
fruityvice_response = requests.get('https://fruityvice.com/api/fruit/'+ fruit_choice)
#streamlit.text(fruityvice_response.json()) as data is now in df form
fruityvice_normalize = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalize)

#connecting to snowflake account and displaying account details
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
#streamlit.text("Hello from Snowflake:")
streamlit.header("The Fruit Load list contains:")
streamlit.dataframe(my_data_rows)

#streamlit.subheader("Breakfast Menu")
#items = ['Omega 3 and Blueberry Oatmeal','Kale, Spinach & Rocket Smoothie','Hard-Boiled Free-Range Egg']
#streamlit.markdown("\n".join(items))
