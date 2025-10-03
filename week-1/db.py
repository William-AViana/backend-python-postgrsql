import os
from dotenv import load_dotenv
import psycopg2

def search_posts():

    try:
        load_dotenv()

        conn = psycopg2.connect(
            database=os.getenv("DATABASE"),
            user=os.getenv("USER_DB"),
            password=os.getenv("PASSWORD_DB"),
            host=os.getenv("HOST_DB"),
            port=os.getenv("PORT_DB")
        )

    # ... (código para interagir com o banco de dados)
        cur = conn.cursor()
        cur.execute("SELECT * FROM posts")
        posts = cur.fetchall()
                
        cur.close()
        conn.close()
        
        return posts
    
    except psycopg2.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    finally:
        if conn:
            conn.close()
        print("Conexão fechada.")

if __name__ == "__main__":
    search_posts()