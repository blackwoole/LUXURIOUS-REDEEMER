from colorama import Fore, Style, Back
import datetime
import json
import os ; os.system('cls')
import sys
import time
# WARNING : THIS IS NOT FOR SKIDS!
def format_current_time():
    __current_time = datetime.datetime.now()
    __formatted_time = __current_time.strftime("%H:%M:%S")
    return __formatted_time
def sprint(content: str):
    print(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}{format_current_time()}{Fore.LIGHTWHITE_EX}] {Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} -> {Fore.LIGHTCYAN_EX}{content}{Fore.RESET}{Style.RESET_ALL}")
def eprint(content: str):
    print(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}{format_current_time()}{Fore.LIGHTWHITE_EX}] {Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}-{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} -> {Fore.LIGHTCYAN_EX}{content}{Fore.RESET}{Style.RESET_ALL}")
def ssprint(content: str):
    print(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}{format_current_time()}{Fore.LIGHTWHITE_EX}] {Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLUE_EX}#{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} -> {Fore.LIGHTCYAN_EX}{content}{Fore.RESET}{Style.RESET_ALL}")
def wprint(content: str):
    print(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}{format_current_time()}{Fore.LIGHTWHITE_EX}] {Fore.LIGHTWHITE_EX}[{Fore.YELLOW}!{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} -> {Fore.LIGHTCYAN_EX}{content}{Fore.RESET}{Style.RESET_ALL}")
def aprint(content: str, delay=0.03):
    __loading_animation = f"{Style.BRIGHT}{Back.LIGHTGREEN_EX}[{format_current_time()}] [/] -> "
    for char in __loading_animation:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(f"{Fore.LIGHTWHITE_EX}{content}{Fore.RESET}{Style.RESET_ALL}")