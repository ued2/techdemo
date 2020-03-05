#!/usr/bin/python
import psycopg2
import sys
from config import config

#First, read database connection parameters from the database.ini file.
#Next, create a new database connection by calling the connect() function.
#Then, create a new cursor and execute an SQL statement to get the PostgreSQL database version.
#After that, read the result set by calling the  fetchone() method of the cursor object.
#Finally, close the communication with the database server by calling the close() method of the cursor and connection objects.
 
# def connect():
#     """ Connect to the PostgreSQL database server """
#     conn = None
#     try:
#         # read connection parameters
#         params = config()
 
#         # connect to the PostgreSQL server
#         print('Connecting to the PostgreSQL database...')
#         conn = psycopg2.connect(**params)
      
#         # create a cursor
#         cur = conn.cursor()
        
#    # execute a statement
#         print('PostgreSQL database version:')
#         cur.execute('SELECT version()')
 
#         # display the PostgreSQL database server version
#         db_version = cur.fetchone()
#         print(db_version)
       
#        # close the communication with the PostgreSQL
#         #cur.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#             print('Database connection closed.')

# def create_tables():
#     """ create tables in the PostgreSQL database"""
#     commands = (
#         """
#         CREATE TABLE projectTest (
            
#         )
#         """
#         )
#     conn = None
#     try:
#         # read the connection parameters
#         params = config()
#         # connect to the PostgreSQL server
#         conn = psycopg2.connect(**params)
#         cur = conn.cursor()
#         # create table one by one
#         for command in commands:
#             cur.execute(command)
#         # close communication with the PostgreSQL database server
#         #cur.close()
#         # commit the changes
#         conn.commit()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
 

#file_path = '/home/stavros/Documents/capstone/OSSMatching/TrashCode/JabRefCounts.csv'
#table_name = 'test_table'

def pg_load_table(file_path, table_name):
    '''
    This function upload csv to a target table
    '''
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        print("Connecting to Database")
        cur = conn.cursor()
        f = open(file_path, "r")
        # Truncate the table first
        cur.execute("Truncate {} Cascade;".format(table_name))
        print("Truncated {}".format(table_name))
        # Load table from the file with header
        cur.copy_expert("copy {} from STDIN CSV HEADER QUOTE '\"'".format(table_name), f)
        cur.execute("commit;")
        print("Loaded data into {}".format(table_name))
        conn.close()
        print("DB connection closed.")

    except Exception as e:
        print("Error: {}".format(str(e)))
        sys.exit(1)


if __name__ == '__main__':
    # connect()
    #create_tables()
   pg_load_table(file_path, table_name)