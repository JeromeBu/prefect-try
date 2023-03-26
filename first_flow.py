import requests
from prefect import flow, task

@task
def call_api(url: str):
    response = requests.get(url)
    print(response.status_code)
    return response.json()

@flow
def my_subflow():
    yo = "yolo"
    return yo

@flow
def api_flow(url: str):
    fact_json = call_api(url)
    yo = my_subflow()
    if(yo == "yolo"):
        print("was yolo")
    else:
        print("was not yolo")
    return fact_json

if __name__ == "__main__":
    api_flow("https://catfact.ninja/fact")