import mysql.connector

def connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Actowiz",
        database="flipkart"
    )
    return conn, conn.cursor()


def create_db():
    conn, cur = connection()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS urls(
            u_id INT AUTO_INCREMENT PRIMARY KEY,
            url TEXT,
            status VARCHAR(255) DEFAULT 'pending'
        )
    """)
    conn.commit()
    conn.close()


def insert_urls(row):
    conn, cur = connection()
    cur.executemany("INSERT INTO urls(url) VALUES(%s)", row)
    conn.commit()
    conn.close()


def update_status(row):
    conn, cur = connection()
    cur.executemany("UPDATE urls SET status = %s WHERE url = %s", row)
    conn.commit()
    conn.close()


def create_product_db():
    conn, cur = connection()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS product_urls(
            u_id INT AUTO_INCREMENT PRIMARY KEY,
            url TEXT,
            status VARCHAR(255) DEFAULT 'pending'
        )
    """)
    conn.commit()
    conn.close()


def insert_product_urls(row):
    clean_row = [(r[0],) for r in row if isinstance(r, tuple) and len(r) == 1 and isinstance(r[0], str)]

    if not clean_row:
        print("No valid data to insert")
        return

    conn, cur = connection()
    cur.executemany("INSERT INTO product_urls(url) VALUES(%s)", clean_row)
    conn.commit()
    conn.close()

    print("*"*20)
    print(f"{len(clean_row)} rows inserted")
    print("*" * 20)


def update_product_status(row):
    conn, cur = connection()
    cur.executemany("UPDATE product_urls SET status = %s WHERE url = %s", row)
    conn.commit()
    conn.close()