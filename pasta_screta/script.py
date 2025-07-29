import subprocess
import sys
import time
import os
print()
subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
subprocess.call("cls", shell=True)

from pathlib import Path
past = Path(__file__).parent.resolve()
pastName = os.path.basename(os.getcwd())

from colorama import Style, Fore, init
init(autoreset=True)

def limpar_ultima_linha():
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    sys.stdout.flush()

# Input com substituição visual
def newInput(mensagem):
    resposta = input(Fore.LIGHTCYAN_EX + mensagem + Fore.RESET)
    limpar_ultima_linha()
    return resposta

print("┌────────────────────────────┐")
print("│ Conectar Python ao", Fore.LIGHTCYAN_EX + "FastAPI", "│")
print("├────────────────────────────┘")

# Entrada do usuário
host = newInput(Fore.RESET + "└─ " + Fore.LIGHTCYAN_EX + "Nome do host: " + Fore.RESET)
root = newInput(Fore.RESET + "└─ " + Fore.LIGHTCYAN_EX + "Usuário do banco: " + Fore.RESET)
password = newInput(Fore.RESET + "└─ " + Fore.LIGHTCYAN_EX + "Senha do banco: " + Fore.RESET)
database = newInput(Fore.RESET + "└─ " + Fore.LIGHTCYAN_EX + "Nome do banco: " + Fore.RESET)
port = newInput(Fore.RESET + "└─ " + Fore.LIGHTCYAN_EX + "Porta do banco: " + Fore.RESET)
filename = newInput(Fore.RESET + "└─ " + Fore.LIGHTCYAN_EX + "Nome do arquivo: " + Fore.RESET)

pacotes = [
    "dotenv",
    "fastapi",
    "uvicorn",
    "mysql-connector-python"
]

# Pergunta ao usuário
dependencias = newInput(Fore.RESET + "└─ " + Fore.LIGHTCYAN_EX + "Deseja instalar as dependências? (S/N): " + Fore.RESET).upper()

def barra_progresso(atual, total, largura, nome):
    progresso = int((atual / total) * largura)
    antes = Fore.GREEN + "━" * progresso
    depois = Fore.LIGHTBLACK_EX + "━" * (largura - progresso)
    print(f"\r   {antes}{depois}{Style.RESET_ALL} [{nome}]", end="")
    time.sleep(0.5)

def instalar_dependencias(pacotes):
    print(Fore.RESET + "└─ " + Fore.YELLOW + "Instalando dependências...")

    largura = 30
    for i, pacote in enumerate(pacotes, 1):
        barra_progresso(i, len(pacotes), largura, pacote)
        
        # Executa o pip silenciosamente (ocultando stdout e stderr)
        subprocess.run(
            [sys.executable, "-m", "pip", "install", pacote],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

if dependencias == "S":
    instalar_dependencias(pacotes)
else:
    print(Fore.RED + "\nInstalação cancelada.\n")

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
def animar_barra(titulo, largura=35, delay=0.04):
    for i in range(largura):
        antes = Fore.RED + "━" * i
        ponteiro = Fore.LIGHTBLACK_EX + "╺"
        depois = Fore.LIGHTBLACK_EX + "━" * (largura - i - 1)
        
        barra = f"\r   {antes}{ponteiro}{depois}{Style.RESET_ALL} [{titulo}]"
        sys.stdout.write(barra)
        sys.stdout.flush()
        time.sleep(delay)

print(Fore.YELLOW + "\n   Criando arquivos...")

with open(past / ".env", "w", encoding="utf-8") as env_file:
    env_file.write(env)
animar_barra(".env")

with open(past / f"{filename}.py", "w", encoding="utf-8") as arquivo:
    arquivo.write(main)
animar_barra(f"{filename}.py")

modulo = filename.split(".")[0]
os.chdir(past)
iniciar = newInput("\n\n   Deseja iniciar o servidor? (S/N): ").upper()

if iniciar == "S":
    subprocess.call("cls", shell=True)
    subprocess.run([
        sys.executable,
        "-m", "uvicorn",
        f"{modulo}:app",
        "--host", "0.0.0.0",
        "--port", "8000"
    ])
else:
    print(Fore.RED + "\nAdeus...\n")
    exit()