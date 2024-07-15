
# YACTA.py
import os
import subprocess
import tkinter as tk
from tkinter import ttk
import time
import csv
from PIL import Image, ImageDraw
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
import io
import ctypes
from ctypes import wintypes
from ctypes import windll


#region tray icon
def create_tray_icon():
    # Função para mostrar a janela
    def show_window(icon, item):
        icon.stop()
        create_window()

    # Função para sair da aplicação
    def quit_app(icon, item):
        icon.stop()

    # Cria uma imagem para o ícone
    width = 64
    height = 64
    with open("icons/tray_icon.png", "rb") as image_file:
        image = Image.open(image_file)
        image = image.convert("RGBA")  # Converte para RGBA se necessário
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 4, height // 4, 3 * width // 4, 3 * height // 4),
        fill="black")

    # Cria o menu do ícone na bandeja
    menu = (item('Show', show_window), item('Quit', quit_app))

    # Cria o ícone na bandeja do sistema
    icon = pystray.Icon("test_icon", image, "Test Icon", menu)
    icon.run()




#endregion


def get_user_processes():
    try:
        # Definir o tipo de função de callback corretamente
        EnumWindowsProc = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)

        # Lista para armazenar os títulos das janelas visíveis
        window_titles = []

        # Função callback para processar cada janela encontrada
        def enum_windows_callback(hwnd, lParam):
            if ctypes.windll.user32.IsWindowVisible(hwnd):
                try:
                    # Função para obter o título da janela
                    length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
                    if length == 0:
                        return True  # Continue a enumeração se o comprimento do título for 0

                    buff = ctypes.create_unicode_buffer(length + 1)
                    ctypes.windll.user32.GetWindowTextW(hwnd, buff, length + 1)

                    # Adicionar o título da janela à lista
                    window_titles.append(buff.value)
                except Exception as e:
                    print(f"Error getting window title: {e}")

            return True

        # Converter a função de callback para o tipo apropriado
        callback_func = EnumWindowsProc(enum_windows_callback)

        # Enumerar todas as janelas no desktop atual
        if not ctypes.windll.user32.EnumDesktopWindows(None, callback_func, 0):
            raise ValueError("EnumDesktopWindows failed")

        # Imprimir os títulos das janelas encontradas
        for title in window_titles:
            print(title)

    except Exception as e:
        print(f"Error: {e}")






#region event open or close window




#endregion








#region create window
# Função para criar uma janela tkinter
def create_window():
    # Inicializar a janela principal
    root = tk.Tk()
    root.title("YACTA-Yet Another Calendar Tracking App")

    # Criar um frame para organizar widgets
    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(padx=20, pady=20)

    # Adicionar um rótulo para o dropdown
    label = tk.Label(frame, text="Select a program:")
    label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    # Criar o dropdown para selecionar programas
    programs = ["Programa 1", "Programa 2", "Programa 3", "Programa 4"]  # Lista de programas
    selected_program = tk.StringVar(value=programs[0])
    dropdown = ttk.Combobox(frame, textvariable=selected_program, values=programs, width=30)
    dropdown.grid(row=0, column=1, padx=5, pady=5)

    # Adicionar um rótulo para a lista de programas
    list_label = tk.Label(frame, text="Programas Selecionados:")
    list_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    # Criar uma lista para exibir os nomes dos programas
    listbox = tk.Listbox(frame, width=50, height=10)
    listbox.grid(row=1, column=1, padx=5, pady=5)

    # Função para atualizar a lista de programas selecionados
    def track_program():
        program_name = selected_program.get()
        if program_name not in listbox.get(0, tk.END):
            listbox.insert(tk.END, program_name)

    # Botão para rastrear o programa selecionado
    track_button = tk.Button(frame, text="Track it!", command=track_program)
    track_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Iniciar o loop principal da interface
    root.mainloop()

#endregion









get_user_processes()



if __name__ == "__main__":
    create_tray_icon()
    while True:
        time.sleep(1)












'''
import time
import os
import subprocess
import tkinter as tk

# Cria a janela principal
root = tk.Tk()
root.title("Janela com duas caixas de texto")

# Cria a primeira caixa de texto
textbox1 = tk.Entry(root, width=50)
textbox1.pack(pady=10)

# Cria a segunda caixa de texto
textbox2 = tk.Entry(root, width=50)
textbox2.pack(pady=10)

# Executa a aplicação
root.mainloop()


print("inicio")

current_user = os.getlogin()
print("current user:["+current_user+"]")
# Execute o comando tasklist para obter os processos em execução
result = subprocess.run(['tasklist', '/FI', f'USERNAME eq {current_user}'], capture_output=True, text=True)
if result.returncode != 0:
    print(f"Erro ao executar 'tasklist': {result.stderr}")
    exit(1)
print("meio2")
# Captura a saída do comando
output_lines = result.stdout.splitlines()

# Exibe apenas os processos do usuário atual
for line in output_lines[3:]:  # Ignora as três primeiras linhas de cabeçalho
    if line.strip():  # Ignora linhas em branco
        print(line)


print("Fim")

'''