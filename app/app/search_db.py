import pandas as pd 
import mysql.connector 
from dbfields import fields 


def SearchDB(statename): 

    statename = statename.upper()

    con = mysql.connector.connect(
    host = fields[0], # replace these with your own values
    user = fields[1], # replace these with your own values
    passwd = fields[2],   # replace these with your own values
    database = fields[3]) # replace these with your own values, make sure the animals database already exists

    if statename.isalpha() == False: 
        quoted = "'{0}'".format(statename)
        return "<h1 style='color: black;'>Sorry, {0} contains non alphanumeric characters.</h1>".format(quoted)

    frame = pd.read_sql("SELECT state, oT, name FROM species WHERE state='{0}'".format(statename), con) #places values from database into dataframe
    
    if frame.empty:
        return "<h1 style='color: black;'>Sorry, {0} is not a valid state initial.</h1>".format(statename)
    
    table_text = frame.head(200).to_html()  #converts dataframe into html table albeit an ugly one lol 
    return table_text 

