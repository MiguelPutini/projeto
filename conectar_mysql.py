import mysql.connector

# Configuração de conexão com o banco de dados
db_config = {
    'host': 'localhost',  # Ou o endereço do seu servidor MySQL
    'user': 'root',       # Seu nome de usuário MySQL
    'password': 'admin',  # Sua senha MySQL
    'database': 'sistemavingadores'  # O banco de dados que você quer acessar
}

# Conectar ao banco de dados
try:
    conn = mysql.connector.connect(**db_config)
    if conn.is_connected():
        print("Conectado ao MySQL com sucesso!")

    # Criar um cursor e realizar uma consulta
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    database = cursor.fetchone()
    print(f"Você está conectado ao banco de dados: {database[0]}")

except mysql.connector.Error as err:
    print(f"Erro: {err}")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexão encerrada.")
