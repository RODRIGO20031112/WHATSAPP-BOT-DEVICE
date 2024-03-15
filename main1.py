from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from tkinter import filedialog
import tkinter as tk
import pandas as pd
import time

root = tk.Tk()

root.withdraw()

caminho_arquivo = filedialog.askopenfilename(title="Selecione um arquivo Selenium")

df = pd.read_csv(caminho_arquivo)

chrome_options = uc.ChromeOptions()

driver = uc.Chrome(options=chrome_options)

driver.get('https://web.whatsapp.com/')

time.sleep(30)

conteudo = "👋 Olá! Eu sou o Rodrigo Bianco de Carvalho! 🤗 Sou desenvolvedor de softwares e acabei esbarrando na sua loja de produtos alimentícios! 🍔🍕🍱 Achei incrível o que você faz! 🌟 Estou aqui com uma proposta: que tal expandir ainda mais o alcance dos seus deliciosos produtos? 💻🛒 Estou pensando em criar um site e-commerce para você! 🌐📲 Isso facilitaria muito para os clientes fazerem suas compras online de maneira prática e segura! 👨‍💻 Vamos criar uma plataforma que vai levar seus produtos diretamente para a casa dos seus clientes! 🏠✨ Estou empolgado com a ideia e acredito que podemos fazer algo incrível juntos! ⚡️ Estou à disposição para discutirmos mais detalhes e para transformarmos essa ideia em realidade! 🚀 O que acha? Vamos embarcar nessa jornada juntos? 💪😊 Além disso, o site sai por apenas 99,99 reais! 💰 Temos diversos modelos e tipos de negócio para atender às suas necessidades! 🎉 Aguardo ansiosamente por sua resposta! 📩"

for numero in df['numero_celular']:

    script_js = f"window.location.href = 'https://web.whatsapp.com/send?phone={numero}&text={conteudo}'"

    driver.execute_script(script_js)

    time.sleep(50)

    try:

        button_locator = (By.XPATH, '//button[@data-tab="11" and @aria-label="Enviar"]')

        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(button_locator))

        button.click()

        time.sleep(5)

    except Exception as e: 
        
        print("Erro na execução", e)

time.sleep(600)

driver.quit() 
