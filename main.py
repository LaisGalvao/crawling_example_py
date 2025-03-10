from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Configurar o WebDriver (Chrome)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# URL da dashboard do Power BI
url = "https://app.powerbi.com/view?r=XXXXX"  # Substitua pelo link real
driver.get(url)

# 🔹 Aguarde o carregamento da página
time.sleep(5)

# 🔹 Localizar a tabela (Ajuste conforme necessário)
try:
    tabela = driver.find_element(By.CLASS_NAME, "visual-container")  # Ajuste para a classe correta da tabela
    
    # Extrair todas as linhas
    linhas = tabela.find_elements(By.TAG_NAME, "tr")
    
    # Extrair cabeçalhos (primeira linha)
    cabecalhos = [th.text for th in linhas[0].find_elements(By.TAG_NAME, "th")]

    # Extrair dados das linhas seguintes
    dados = []
    for linha in linhas[1:]:  # Pular a primeira linha (cabeçalhos)
        colunas = linha.find_elements(By.TAG_NAME, "td")
        dados.append([coluna.text for coluna in colunas])

    # Criar DataFrame do Pandas
    df = pd.DataFrame(dados, columns=cabecalhos)

    # Salvar em Excel com cabeçalhos
    df.to_excel("dados_dash.xlsx", index=False)

    print("📊 Dados extraídos e salvos em 'dados_dash.xlsx' com sucesso!")

except Exception as e:
    print("❌ Erro ao extrair tabela:", e)

# 🔹 Fechar navegador
driver.quit()
