import requests
import pandas as pd

base_url = "https://clubecasadesign.com.br/api/stores"  # Substitua pela URL real
page = 1
has_next_page = True
all_data = []

while has_next_page:
    url = f"{base_url}?page={page}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()

        # Supondo que os dados desejados estão dentro de 'items'
        all_data.extend(data['data'])

        # Verifique se há mais páginas
        if 'next_page' in data and data['next_page']:
            page += 1
        else:
            has_next_page = False
    else:
        print(f"Erro na requisição da página {page}: {response.status_code}")
        break

# Converter os dados em um DataFrame do Pandas
df = pd.DataFrame(all_data)

# Salvar os dados em uma planilha Excel (ou CSV)
df.to_excel('dados.xlsx', index=False)  # Salvar como Excel
# df.to_csv('dados.csv', index=False)  # Ou salvar como CSV
