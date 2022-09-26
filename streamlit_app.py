import streamlit 
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast menu')
streamlit.text('Omega 3 and blueberry oatmeal')
streamlit.text('Kale, Spinach and Rock smoothie')
streamlit.text('Hard-Boiled Free-range egg')
streamlit.text('Avacado Toast')
streamlit.title('Build your own smoothie')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list= my_fruit_list.set_index('Fruit')

#multiselect option from list 
fruits_selected= streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show=my_fruit_list.loc[fruits_selected]
                       
#adding display table on page 
streamlit.dataframe(fruit_to_show)
