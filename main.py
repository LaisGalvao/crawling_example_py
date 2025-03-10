import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuração do WebDriver (Chrome)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--headless")  # Executar em modo headless (sem interface gráfica)

# Inicializando o WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL da dashboard do Power BI
url = "https://app.powerbi.com/view?r=eyJrIjoiZmU3NDAwZDAtNGIzZi00YjhkLWEzNmYtODdkNjZjNjhiZDBiIiwidCI6IjI2OTQyYmU5LThiODMtNGI1OC04OTBmLWQ5NGJkNDAwNzhlMiJ9"

# Acessando a URL
driver.get(url)

# Aguardar até que os visuais estejam presentes na página
try:
    visuais = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "visualContainer"))
    )

    # Extrair os dados de cada visual (Exemplo)
    data = []
    for visual in visuais:
        # Aqui você pode adicionar a extração dos dados que você deseja do visual
        # Exemplo fictício: data.append({"id": visual.get_attribute("id"), "texto": visual.text})
        data.append({"id": visual.get_attribute("id"), "texto": visual.text})

    # Criar um DataFrame do pandas
    df = pd.DataFrame(data)

    # Salvar no Excel na raiz do projeto
    file_path = "dados_extraidos.xlsx"  # Caminho do arquivo Excel
    df.to_excel(file_path, index=False)

    print(f"📊 Dados extraídos e salvos com sucesso em {file_path}")

except Exception as e:
    print(f"❌ Erro ao extrair dados: {e}")

# Fechar o navegador
driver.quit()
