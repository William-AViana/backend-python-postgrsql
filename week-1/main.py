from fastapi import FastAPI
import psycopg2
from dotenv import load_dotenv
import os

load_dotent()

try:
    # Parâmetros de conexão
    conn = psycopg2.connect(
        database=os.getenv("DATABASE"),
        user="seu_usuario",
        password="sua_senha",
        host="localhost",  # Ou o endereço do seu servidor
        port="5432"        # Porta padrão do PostgreSQL
    )

    print("Conexão bem-sucedida!")

    # ... (código para interagir com o banco de dados)

except psycopg2.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
finally:
    if conn:
        conn.close() # Fechar a conexão ao final
        print("Conexão fechada.")



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
