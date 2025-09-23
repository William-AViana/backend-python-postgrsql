import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

try:
    # Parâmetros de conexão
    conn = psycopg2.connect(
        database=os.getenv("DATABASE"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        host=os.getenv("HOST"),
        port=os.getenv("PORT")
    )

    print("Conexão bem-sucedida!")

    # ... (código para interagir com o banco de dados)

except psycopg2.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
finally:
    if conn:
        conn.close() # Fechar a conexão ao final
        print("Conexão fechada.")

