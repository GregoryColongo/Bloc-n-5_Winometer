import requests 

response = requests.post("http://127.0.0.1:5000/predict", json={ "input": [[7.0, 0.6, 0.36, 60.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]] }) 

print(response.json()) 