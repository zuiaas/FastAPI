import time
import sys
from colorama import Style, Fore, init
init(autoreset=True)

# Entrada do usuário
host = input(Fore.LIGHTCYAN_EX + "\nNome do host: " + Fore.RESET)
root = input(Fore.LIGHTCYAN_EX + "Usuário do banco: " + Fore.RESET)
password = input(Fore.LIGHTCYAN_EX + "Senha do banco: " + Fore.RESET)
database = input(Fore.LIGHTCYAN_EX + "Nome do banco: " + Fore.RESET)
port = input(Fore.LIGHTCYAN_EX + "Porta do banco: " + Fore.RESET)
filename = input(Fore.LIGHTCYAN_EX + "Nome do arquivo: " + Fore.RESET)

# Conteúdo dos arquivos
main = """import mysql.connector
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from env import HOST, USER, PASSWORD, DATABASE, PORT

app = FastAPI()

def connection():
    return mysql.connector.connect(
        host = HOST,
        user = USER,
        password = PASSWORD,
        database = DATABASE,
        port = PORT
    )"""

env = f"""# Database configuration for the application

HOST={host}
USER={root}
PASSWORD={password}
DATABASE={database}
PORT={port}"""

# Função de barra animada
def animar_barra(titulo, largura=40, delay=0.04):
    for i in range(largura):
        antes = Fore.RED + "━" * i
        ponteiro = Fore.LIGHTBLACK_EX + "╺"
        depois = Fore.LIGHTBLACK_EX + "━" * (largura - i - 1)
        
        barra = f"\r{antes}{ponteiro}{depois}{Style.RESET_ALL} [{titulo}]"
        sys.stdout.write(barra)
        sys.stdout.flush()
        time.sleep(delay)
    print()

print(Fore.RED + "\nCriando arquivos...")

with open(".env", "w", encoding="utf-8") as env_file:
    env_file.write(env)
animar_barra(".env")

with open(f"{filename}.py", "w", encoding="utf-8") as arquivo:
    arquivo.write(main)
animar_barra(f"{filename}.py")

print(Fore.GREEN + f"""
\ past
│
├─ .env
└─ {filename}.py
""")
print()