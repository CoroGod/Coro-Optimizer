import os
import shutil
import ctypes
from colorama import Fore, Style, init
import itertools
import time

# Inicializa colorama
init(autoreset=True)


def limpiar_cache():
    """Función para eliminar archivos temporales del usuario."""
    temp_folder = os.getenv('TEMP')
    try:
        files = os.listdir(temp_folder)
        for file in files:
            file_path = os.path.join(temp_folder, file)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                pass  # Ignorar errores para archivos en uso
        print(Fore.GREEN + "[✔] Caché del usuario limpiada.")
    except Exception as e:
        print(Fore.RED + "[✘] No se pudo limpiar la caché.")


def limpiar_papelera():
    """Función para vaciar la papelera de reciclaje (solo Windows)."""
    try:
        result = ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 0)
        if result == 0:
            print(Fore.GREEN + "[✔] Papelera de reciclaje vaciada.")
        else:
            print(Fore.RED + "[✘] No se pudo vaciar la papelera de reciclaje.")
    except Exception as e:
        print(Fore.RED + "[✘] Función no soportada en este sistema operativo.")


def limpiar_archivos_temporales_sistema():
    """Función para limpiar los archivos temporales del sistema."""
    temp_system_folder = "C:\\Windows\\Temp"
    try:
        files = os.listdir(temp_system_folder)
        for file in files:
            file_path = os.path.join(temp_system_folder, file)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                pass  # Ignorar errores para archivos en uso
        print(Fore.GREEN + "[✔] Archivos temporales del sistema limpiados.")
    except Exception as e:
        print(Fore.RED + "[✘] No se pudo limpiar los archivos temporales del sistema.")


def mostrar_ascii_art():
    """Función para mostrar arte ASCII con colores en arcoíris."""
    ascii_art = ("\n"
                 " ░▒▓██████▓▒░  ░▒▓██████▓▒░   ░▒▓█████▓▒░  ░▒▓██████▓▒░     ░▒▓██████▓▒░  ░▒▓██████▓▒  ▒▓███████▓▒░     \n"
                 "░▒▓█▓▒░░▒▓█▓▒ ░▒▓█▓▒   ▒▓█▓▒ ░▒▓██████▓▒░ ░▒▓█▓▒  ▒▓█▓▒░   ░▒▓█▓▒ ░▒▓█▓▒ ░▒▓█▓▒  ▒▓█▓▒ ▒▓█▓▒  ▓█▓▒░    \n"
                 "░▒▓█▓▒░       ░▒▓█▓▒   ▒▓█▓▒ ░▒▓█▓▒░      ░▒▓█▓▒  ▒▓█▓▒░   ░▒▓█▓▒        ░▒▓█▓▒  ▒▓█▓▒ ▒▓█▓▒  ▒▓█▓▒░     \n"
                 "░▒▓█▓▒░       ░▒▓█▓▒   ▒▓█▓▒ ░▒▓█▓▒░      ░▒▓█▓▒  ▒▓█▓▒░   ░▒▓█▓▒ ▓███▓▒ ░▒▓█▓▒  ▒▓█▓▒ ▒▓█▓▒  ▒▓█▓▒░     \n"
                 "░▒▓█▓▒░       ░▒▓█▓▒   ▒▓█▓▒ ░▒▓█▓▒░      ░▒▓█▓▒  ▒▓█▓▒░   ░▒▓█▓▒  ▒▓█▓▒ ░▒▓█▓▒  ▒▓█▓▒ ▒▓█▓▒  ▒▓█▓▒░     \n"
                 "░▒▓█▓▒░░▒▓█▓▒ ░▒▓█▓▒   ▒▓█▓▒ ░▒▓█▓▒░      ░▒▓█▓▒  ▒▓█▓▒░   ░▒▓█▓▒  ▒▓█▓▒ ░▒▓█▓▒  ▒▓█▓▒ ▒▓█▓▒  ▒▓█▓▒░    \n"
                 " ░▒▓██████▓▒░  ░▒▓██████▓▒░  ░▒▓█▓▒░       ░▒▓██████▓▒░     ░▒▓██████▓▒░  ░▒▓██████▓▒  ▒▓███████▓▒░       \n"
                 "\n")
    # Lista de colores en arcoíris
    rainbow_colors = [
        Fore.LIGHTRED_EX,
        Fore.LIGHTYELLOW_EX ,
        Fore.LIGHTGREEN_EX,
        Fore.LIGHTCYAN_EX,
        Fore.LIGHTBLUE_EX,
        Fore.LIGHTMAGENTA_EX,
    ]

    # Divide el arte ASCII en líneas
    lines = ascii_art.splitlines()

    # Cicla los colores del arcoíris
    color_cycle = itertools.cycle(rainbow_colors)

    for line in lines:
        # Imprime cada línea con un color diferente
        print(next(color_cycle) + line)
        time.sleep(0.1)  # Pequeño retraso para un efecto visual


def menu_principal():
    """Función para ejecutar el programa."""
    mostrar_ascii_art()
    print(Fore.LIGHTCYAN_EX + "   ¡Bienvenido a Coro God! Este es un proyecto libre para la Optimización de tu PC ;)")
    print(Fore.LIGHTGREEN_EX + "   [1] Limpiar caché del usuario")
    print(Fore.LIGHTGREEN_EX + "   [2] Vaciar papelera")
    print(Fore.LIGHTGREEN_EX + "   [3] Limpiar archivos temporales del sistema")
    print(Fore.LIGHTGREEN_EX + "   [4] Optimizar todo ;)")
    print(Fore.LIGHTRED_EX + "   [0] Salir")

    opcion = input(Fore.LIGHTCYAN_EX +   "   Seleccione una opción: ")

    if opcion == "1":
        limpiar_cache()
    elif opcion == "2":
        limpiar_papelera()
    elif opcion == "3":
        limpiar_archivos_temporales_sistema()
    elif opcion == "4":
        limpiar_cache()
        limpiar_papelera()
        limpiar_archivos_temporales_sistema()
        print(Fore.GREEN + "[✔] Optimización completa realizada.")
    elif opcion == "0":
        print(Fore.CYAN + "Saliendo del programa...")
    else:
        print(Fore.RED + "Opción inválida.")

    input(Fore.CYAN + "\nPresione Enter para salir...")


if __name__ == "__main__":
    menu_principal()
