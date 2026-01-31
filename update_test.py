import requests

url = "https://inversionapp-backend.onrender.com/update-portfolio"
headers = {"secret_key": "tu_clave_segura"}  # reemplaza con tu SECRET_KEY real

response = requests.post(url, headers=headers)
print(response.json())
