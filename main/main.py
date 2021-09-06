import uvicorn
from fastapi import  FastAPI
import mysql.connector
from mysql.connector import errorcode
from Football_Transfers_Class import Football_transfert
import  Create_table as c
import insert_data as i

# creating a FastAPI server
app = FastAPI(title='Api Base De Données')

# creating a connection to the database
mysql_url = "mysql"
mysql_user = 'test'
mysql_password = 'test_pass'
database_name = 'Football_Transfers'

# create  Football_Transfers table
c.create_table()

#insert dataframe in database 
i.insert_data()

@app.get('/status')
async def get_status():
    """Renvoie 1 si API UP
    """
    return {
        'status': 1
    }


@app.post('/insert_bdd_elemets')

async def insert_bdd_elemets(ft:Football_transfert ):

    """Insert une ligne  dans la base de données 
    """

    # data to insert in data base
    data_to_insert = (ft.Name, ft.Position, ft.Age, ft.Team_from, ft.League_from, ft.Team_to, ft.League_to ,
    ft.Season , ft.Market_value , ft.Transfer_fee)
    

    try:
        cnx = mysql.connector.connect(user=mysql_user, password=mysql_password,
                              host= mysql_url, database=database_name)

        cursor = cnx.cursor()

        insert_query = ("INSERT INTO Football_Transfers "
        "(Name, Position, Age, Team_from, League_from, Team_to, League_to, Season, Market_value, Transfer_fee) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)") 
        
        cursor.execute(insert_query, data_to_insert)
        
        cnx.commit()
        
        return {'Voila la ligne que vous avez insérer dans la base de données ' : data_to_insert}

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()

@app.get('/show_bdd_elemets')
async def show_bdd_elemets():
    """Renvoie les 10 premieres lignes de la base de données 
    """
    try:
        cnx = mysql.connector.connect(user=mysql_user, password=mysql_password,
                              host= mysql_url, database=database_name)
                              
        cursor = cnx.cursor()
        sql = "SELECT * FROM `Football_Transfers` LIMIT 10"
        cursor.execute(sql)
        # Fetch all the records
        result = cursor.fetchall()
        bdd_elemets =[]
        for i in result:
            bdd_elemets.append(i)
        
        return {'Voila les 10 premiéres lignes de  la base de données ' : bdd_elemets}

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()
    
    

# Run the API with uvicorn
# Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)