import mysql.connector
import os
from dotenv import load_dotenv

#faz conexao inicial com o banco
def conecta_banco():
    load_dotenv()

    conexao = mysql.connector.connect (
        host = os.getenv("HOST_ENV"),
        user = os.getenv("USER_ENV"),
        port = os.getenv("PORT_ENV"),
        password = os.getenv("PASSWORD_ENV"),
        database = os.getenv("DATABASE_ENV")
    )

    cursor = conexao.cursor()
    return cursor, conexao




def executa_DICT(command): # conseguiu pegar => elemento do banco
    cursor, conexao = conecta_banco()

    cursor.execute(command)
    columns = [col[0] for col in cursor.description]
    resultado = [dict(zip(columns, row)) for row in cursor.fetchall()]
    cursor.close()
    conexao.close()

    return resultado

def executa_DICT_ONE(command): # conseguiu pegar => elemento do banco
    cursor, conexao = conecta_banco()

    cursor.execute(command)
    columns = [col[0] for col in cursor.description]
    resultado = dict(zip(columns, cursor.fetchone()))
    cursor.close()
    conexao.close()

    return resultado

def executa_GET(command): # conseguiu pegar => elemento do banco
    cursor, conexao = conecta_banco()

    cursor.execute(command)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()

    return resultado

def executa_GET_BY_ID(command): # conseguiu pegar => elemento do banco
    cursor, conexao = conecta_banco()

    cursor.execute(command)
    resultado = cursor.fetchone()[0]
    cursor.close()
    conexao.close()

    return resultado

def executa_DEFAULT(command): # conseguiu alterar => 'sucesso'
    cursor, conexao = conecta_banco()

    cursor.execute(command)
    conexao.commit()
    cursor.close()
    conexao.close()

    return "sucesso"

########## FUNÇÃO PRINCIPAL (CHAMA AS FUNÇÕES ESPECIFICAS) ##########

def executar_comando(method, command):        
    match method:
        case "POST" | "PUT" | "DELETE":
            return executa_DEFAULT(command)
        
        case "GET":
            return executa_GET(command)
        
        case "GET_BY_ID":
            return executa_GET_BY_ID(command)

        case "GET_DICT":
            return executa_DICT(command)

        case "GET_DICT_ONE":
            return executa_DICT_ONE(command)
        
        case _:
            return "MÉTODO INVÁLIDO"


    

    print(f"Host: {host}")
    print(f"User: {user}")
    print(f"Port: {port}")
    print(f"Database: {database}")