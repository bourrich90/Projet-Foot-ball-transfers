# Import des packages
import mysql.connector
from mysql.connector import errorcode
import pandas as pd


# creating a connection to the database
mysql_url = "localhost"
mysql_user = 'root'
mysql_password = 'admin'
database_name = 'Football_Transfers'

def insert_data():

# importer le jeu de données 
  transfers_dataframe = pd.read_csv("top250-00-19.csv")
  transfers_dataframe.head()
 
# repalce  nan values by 0 in  Market_value column
  transfers_dataframe.Market_value = transfers_dataframe.Market_value.fillna(0)

  try:
    cnx = mysql.connector.connect(user=mysql_user, password=mysql_password,
                              host= mysql_url,
                              database=database_name)

  
    cursor = cnx.cursor()

# create a list of  dataframe  columns 
    cols = "`,`".join([str(i) for i in transfers_dataframe.columns.tolist()])

# insert dataframe line by line 
    for i,row in transfers_dataframe.iterrows():
      insert_query = ("INSERT INTO `Football_Transfers` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)") 
      cursor.execute(insert_query, tuple(row))
      cnx.commit()

    print("la table Football_Transfers vient d'étre peuplée avec le fichier csv ")
# verify database and  login/pwd
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  else:
    cnx.close()
