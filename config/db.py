import psycopg2

def conect_db():
    try:
        conn = psycopg2.connect(
            dbname='hospital',
            user='postgres',
            password='admin',
            host='localhost',
            port='5432',
        )
        return conn
    except Exception as e:
        print(e)