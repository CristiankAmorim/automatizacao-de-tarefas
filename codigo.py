# Passo 1: Entrar no site da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer login
# Passo 3: Importar a base de dados
# Passo 4: Repetir para todos os produtos

import pyautogui
import time

# Pausa entre comandos
pyautogui.PAUSE = 0.3

# ==== Passo 1 ====
# Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# ===== Passo 2 ====
pyautogui.click(x=712, y=370)
pyautogui.write("cristian.amorim@gmail.com")
pyautogui.press("tab")
pyautogui.write("ckas232013")
pyautogui.click(x=955, y=534)
time.sleep(3)

# ==== Passo 3 ====
import pandas as pd
tabel = pd.read_csv("produtos.csv")
print(tabel)

# ==== Passo 4 ====
for line in tabel.index:
    pyautogui.click(x=841, y=257)
    codigo = tabel.loc[line, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    pyautogui.write(str(tabel.loc[line, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabel.loc[line, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabel.loc[line, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabel.loc[line, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabel.loc[line, "custo"]))
    pyautogui.press("tab")

    obs = tabel.loc[line, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabel.loc[line, "obs"]))
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(5000)