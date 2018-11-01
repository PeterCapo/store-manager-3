import psycopg2
import os

url = "dbname='store_manager' host='localhost' port='5432' user='postgres' password='postgres'"

db_url = os.getenv('DATABASE_URL')


def connection():
    conn = psycopg2.connect(url)
    conn.autocommit = True
    return conn

def create_tables():
    curr=connection().cursor()
    queries = tables()
    for query in queries:
        curr.execute(query)


def destroy_tables():
    pass


def tables():
    db1 = """CREATE TABLE IF NOT EXISTS products (
        product_id serial PRIMARY KEY NOT NULL,
        productName character varying(1000) NOT NULL,
        category TEXT,
        price numeric NOT NULL,
        stockBalance numeric NOT NULL
        );"""

    db2 = """CREATE TABLE IF NOT EXISTS sales (
        sales_id serial PRIMARY KEY NOT NULL,
        productid numeric NOT NULL,
        quantity numeric NOT NULL,
        attendant TEXT
        );"""

    db3 = """CREATE TABLE IF NOT EXISTS users (
        id serial PRIMARY KEY,
        email  VARCHAR NOT NULL,
        password VARCHAR NOT NULL,
        admin BOOLEAN NOT NULL
        );"""

    queries = [db1, db2, db3]
    return queries
