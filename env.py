from dotenv import load_dotenv; load_dotenv()
import os
from colorama import Fore, Style, init; init(autoreset=True)

HOST = os.getenv("HOST")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")
PORT = os.getenv("PORT")

print(
f"""
{Fore.LIGHTCYAN_EX + "Seu host:"          + Fore.RESET} {HOST}
{Fore.LIGHTCYAN_EX + "Seu usuário:"       + Fore.RESET} {USER}
{Fore.LIGHTCYAN_EX + "Sua senha:"         + Fore.RESET} {PASSWORD}
{Fore.LIGHTCYAN_EX + "Nome do seu banco:" + Fore.RESET} {DATABASE}
{Fore.LIGHTCYAN_EX + "Sua porta:"         + Fore.RESET} {PORT}
"""
)