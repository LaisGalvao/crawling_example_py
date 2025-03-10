from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Configuração do WebDriver (Chrome)
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--headless")  # Executar em modo headless (sem interface gráfica)

# Inicializando o WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL da página
url = "SUA_URL_AQUI"

# Acessando a URL
driver.get(url)

# Esperar a tabela carregar (ajuste o tempo conforme necessário)
driver.implicitly_wait(10)

# Localizar a tabela com o XPath fornecido
tabela = driver.find_element(By.XPATH, "/html/body/div[1]/report-embed/div/div/div[1]/div/div/div/exploration-container/div/div/docking-container/div/div/div/div/exploration-host/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[7]/transform/div/div[3]/div/div/visual-modern/div/div/div[2]/div[1]/div[2]/div")

# Extrair as linhas da tabela
linhas = tabela.find_elements(By.XPATH, ".//div[contains(@class, 'visual-row')]")

# Criar uma lista para armazenar os dados
dados = []

# Iterar sobre as linhas da tabela e extrair os dados das células
for linha in linhas:
    celulas = linha.find_elements(By.XPATH, ".//div[contains(@class, 'visual-cell')]")
    dados_linha = [celula.text for celula in celulas]
    dados.append(dados_linha)

# Criar um DataFrame com os dados extraídos
df = pd.DataFrame(dados)

# Salvar os dados em um arquivo Excel
caminho_arquivo = "dados_dash.xlsx"
df.to_excel(caminho_arquivo, index=False)

print(f"Dados extraídos e salvos em {caminho_arquivo}")

# Fechar o navegador
driver.quit()
