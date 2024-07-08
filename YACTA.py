
import tkinter as tk
from PIL import Image, ImageDraw
import pystray
from pystray import MenuItem as item

# Função para criar uma janela tkinter
def create_window():
    root = tk.Tk()
    root.title("Janela com duas caixas de texto")
    
    textbox1 = tk.Entry(root, width=50)
    textbox1.pack(pady=10)

    textbox2 = tk.Entry(root, width=50)
    textbox2.pack(pady=10)
    
    root.mainloop()

# Função para criar um ícone na bandeja do sistema
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
    image = Image.new('RGB', (width, height), (255, 255, 255))
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 4, height // 4, 3 * width // 4, 3 * height // 4),
        fill="black")

    # Cria o menu do ícone na bandeja
    menu = (item('Show', show_window), item('Quit', quit_app))

    # Cria o ícone na bandeja do sistema
    icon = pystray.Icon("test_icon", image, "Test Icon", menu)
    icon.run()

# Executa a função para criar o ícone na bandeja do sistema
if __name__ == "__main__":
    create_tray_icon()















# YACTA.py
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