import pandas as pd
import requests
import pandas
import json
import plotly.express as pl
def get_covid(country):
    return requests.get(
    'https://api.coronavirus.data.gov.uk/v1/data?'
    f'filters=areaType=nation;areaName={country}&'
    'structure={"date":"date",newCasesByPublishDate}')
    data = request.json()
    data_frame = pd.DataFrame(data["data"])
    graph = pl.line(data_frame,x="date",y="deathRate")
    graph.show()
def get_covid_spec(url,country):
    request = requests.get(url)
    data = request.json()
    data_frame = pd.DataFrame(data["data"])
    graph = pl.line(data_frame,x="date",y="deathRate")
    graph.show()

def get_covid(country):
    return requests.get(
        'https://api.coronavirus.data.gov.uk/v1/data?'
        f'filters=areaType=nation;areaName={country}&'
        'structure={"date":"date","newCases":"newCasesByPublishDate"}'
    )

def getcorona():
    eng = get_covid("england").json()["data"]
    scot = get_covid("scotland").json()["data"]
    wales = get_covid("wales").json()["data"]
    dataframe = pd.DataFrame(eng)
    dataframe["scotland"] = pd.DataFrame(scot)["newCases"]
    dataframe["wales"] = pd.DataFrame(scot)["newCases"]
    graph = pl.line(dataframe, x="date",y=["england","scotland","wales"])
    graph.show()
    graph.write_image("graph_covid.png")

getcorona()