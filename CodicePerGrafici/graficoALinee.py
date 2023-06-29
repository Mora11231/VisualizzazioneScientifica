import pandas as pd
import plotly.graph_objs as go
import scipy.stats as st



def graficoGiochiPerAnno():
    df = pd.read_csv('CodicePerGrafici/fileAggiornatoF2P.csv')
    df['Release date'] = df['Release date'].astype('datetime64[ns]')
    df['year'] = df['Release date'].apply(lambda x: x.year)
    
    giochiPerAnno= df['year'].value_counts().sort_index()
    giochiSum=giochiPerAnno.cumsum()

    giochiPerAnno[2013] =giochiSum[2013]
    
    graph1 = go.Scatter(
        x=giochiPerAnno.index[16:-1],
        y= giochiPerAnno[16:-1],
        mode="markers+lines"
        )

    fig = go.Figure()
    fig.add_trace(graph1)

    fig.show()

def graficoMediaPrezzoAnni():
    df = pd.read_csv('CodicePerGrafici/fileAggiornatoF2P.csv')
    df['Release date'] = df['Release date'].astype('datetime64[ns]')
    df['year'] = df['Release date'].apply(lambda x: x.year)
    df= df[df['year']>=2007]

    P2P = df[df['Price'] > 5]
    p2p_series= P2P[['year','Price']].groupby('year').mean()

    fig = go.Figure()

    graph = go.Scatter(
        x=p2p_series.index[:-1],
        y=p2p_series.Price[:-1],
        mode="markers+lines",
        name='Prezzo Medio Senza F2P'
    )

    series = df[['year','Price']].groupby('year').mean()
    graph1 = go.Scatter(
        x=series.index[:-1],
        y=series.Price[:-1],
        mode="markers+lines",
        name='Prezzo Medio CON F2P'
    )
   
    fig = fig.add_trace(graph)
    fig = fig.add_trace(graph1)
    fig.show()

graficoMediaPrezzoAnni()
#graficoGiochiPerAnno()
