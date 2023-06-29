import pandas as pd
import plotly.express as px

def graficoTortaAppEGiochi():
    df = pd.read_csv('CodicePerGrafici/fileAggiornatoF2P.csv')
 
    serie = df.F2P.value_counts()

    fig = px.pie(values=serie,names=['F2P','P2P'])
    fig.show()
graficoTortaAppEGiochi()