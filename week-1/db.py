import os
from dotenv import load_dotenv
import psycopg2


try:

    load_dotenv()

    conn = psycopg2.connect(
        database=os.getenv("DATABASE"),
        user=os.getenv("USER_DB"),
        password=os.getenv("PASSWORD_DB"),
        host=os.getenv("HOST_DB"),
        port=os.getenv("PORT_DB")
    )

    print("Conexão bem-sucedida!")

    # ... (código para interagir com o banco de dados)

except psycopg2.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
finally:
   if conn:
        conn.close() # Fechar a conexão ao final
        print("Conexão fechada.")

