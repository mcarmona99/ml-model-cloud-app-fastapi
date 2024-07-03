import requests

url = "https://ml-model-cloud-app-fastapi.onrender.com"
endpoint = "/predict"

data_test = {
    "age": 36,
    "workclass": "Private",
    "fnlgt": 484024,
    "education": "HS-grad",
    "education-num": 9,
    "marital-status": "Divorced",
    "occupation": "Machine-op-inspct",
    "relationship": "Unmarried",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States"
}

response = requests.post(f"{url}{endpoint}", json=data_test)
print(f"Prediction for\n\n{data_test}:\n")
print(f"Predicion: {response.json()['prediction']}\n")
print("·0 - <=50K\n·1 - >50K")
