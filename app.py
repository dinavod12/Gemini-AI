import streamlit as st
import mysql.connector

import google.generativeai as genai

genai.configure(api_key="AIzaSyB6kk3bj8hwinsukA18KLSQlXvCCtTatow")

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel("gemini-pro")
    response=model.generate_content([prompt[0],question])
    return response.text

def read_sql_query(sql,db):
    conn = mysql.connector.connect(
    host="localhost ",  
    user="root",  
    password="student",  
    database="shyder_bytes"  
    )
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


prompt=[
    ""
    You are an expert in converting English questions to SQL query!
    The SQL database has the name admin and has the following columns - server_id, name, 
    status \n\nFor example,\nExample 1 - Tell me all name?, 
    the SQL command will be something like this SELECT name FROM admin ;
    \nExample 2 - Tell me all the server_id?, 
    the SQL command will be something like this SELECT COUNT(*) FROM admin "; 
    also the sql code should not have ``` in beginning or end and sql word in output

    ""


]


st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")


if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"test.db")
    st.subheader("The REsponse is")
    for row in response:
        print(row)
        st.header(row)
        
        


        
        
        
        
