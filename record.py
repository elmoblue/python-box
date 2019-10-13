import psycopg2
# from  psycopg2 import Error

class Record:
        def __init__(self):
            pass

        host = "127.0.0.1"
        user = "postgres"
        password = ""
        port = "5432"
        database = "bdot"

        @staticmethod
        def checkConnection():
            try:
                connection = psycopg2.connect(user = Record.user,
                password = "",
                host = Record.host,
                port = Record.port,
                database = Record.database)

                cursor = connection.cursor()
                create_table_query = '''CREATE TABLE mobile (ID INT PRIMARY KEY NOT NULL, MODEL TEXT NOT NULL, PRICE REAL); '''
                cursor.execute(create_table_query)
                connection.commit()
                print("Table created successfully in PostgreSQL ")

            except (Exception, psycopg2.DatabaseError) as error:
                print ("Error while creating PostgreSQL table", error)
            finally:
            # closing database connection.
                if connection:
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")

        @staticmethod
        def runQuery(sql):
            try:
                connection = psycopg2.connect(user = Record.user,
                password = "",
                host = Record.host,
                port = Record.port,
                database = Record.database)

                cursor = connection.cursor()
                query = '''{}'''.format(sql)
                cursor.execute(query)
                connection.commit()

            except (Exception, psycopg2.DatabaseError) as error:
                print (error)
            finally:
            # closing database connection.
                if connection:
                    cursor.close()
                    connection.close()

        @staticmethod
        def fetchAllRecord(sql):
            try:
                connection = psycopg2.connect(user=Record.user,
                password="",
                host=Record.host,
                port=Record.port,
                database=Record.database)

                cursor = connection.cursor()
                query = '''{}'''.format(sql)
                cursor.execute(query)
                record = cursor.fetchall()
                connection.commit()

                return record

            except (Exception, psycopg2.DatabaseError) as error:
                print (error)
            finally:
            # closing database connection.
                if connection:
                    cursor.close()
                    connection.close()

        @staticmethod
        def fetchSingleRecord(sql):
            try:
                connection = psycopg2.connect(user=Record.user,
                password="",
                host=Record.host,
                port=Record.port,
                database=Record.database)

                cursor = connection.cursor()
                query = '''{}'''.format(sql)
                cursor.execute(query)
                record = cursor.fetchone()
                connection.commit()

                return record

            except (Exception, psycopg2.DatabaseError) as error:
                print (error)
            finally:
                # closing database connection.
                if connection:
                    cursor.close()
                    connection.close()



