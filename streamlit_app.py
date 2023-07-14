import streamlit
import pandas 


my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title("My Parents New Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text("🥣 Omega 3 and Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

streamlit.dataframe(my_fruit_list)
#Put up a multiselect/ pick list for users to pick fruits they want
#streamlit.multiselect("Pick fruits of your choice: ",list(my_fruit_list['Fruit']))
streamlit.multiselect("Pick fruits of your choice: ",list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_selected = streamlit.multiselect("Pick fruits of your choice: ",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#streamlit.subheader("Breakfast Menu")
#items = ['Omega 3 and Blueberry Oatmeal','Kale, Spinach & Rocket Smoothie','Hard-Boiled Free-Range Egg']
#streamlit.markdown("\n".join(items))
