import pg8000

def connect_to_database():
    return pg8000.connect(
        host='localhost',
        port=5432,
        database='rule_engine_db',
        user='engine',
        password='Abhay@10'
    )

def execute_query(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    return cur.fetchall()

def close_connection(conn):
    conn.close()