# Import des packages
import mysql.connector
from mysql.connector import errorcode

# creating a connection to the database
mysql_url = "mysql"
mysql_user = 'test'
mysql_password = 'test_pass'
database_name = 'Football_Transfers'

def create_table():
  try:
    cnx = mysql.connector.connect(user=mysql_user, password=mysql_password,
                              host= mysql_url,
                              database=database_name)
    cursor = cnx.cursor()

# create  Football_Transfers table
    table_query = (
      "CREATE TABLE IF NOT EXISTS Football_Transfers( "
      "Id_transfert INT(11) NOT NULL AUTO_INCREMENT , "
      "Name varchar(40) NOT NULL, "
      "Position varchar(40) NOT NULL, "
      "Age integer NOT NULL, "
      "Team_from varchar(40) NOT NULL, "
      "League_from varchar(40) NOT NULL, "
      "Team_to varchar(40) NOT NULL, "
      "League_to varchar(40) NOT NULL, "
      "Season varchar(40) NOT NULL, "
      "Market_value DOUBLE , "
      "Transfer_fee DOUBLE, "
      "PRIMARY KEY (Id_transfert)); "
                )
    cursor.execute(table_query)
  
    cnx.commit()
    
    print("la table Football_Transfers vient d'étre crée ")
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