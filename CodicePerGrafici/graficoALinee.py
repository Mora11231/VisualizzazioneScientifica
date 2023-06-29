import pandas as pd
import plotly.graph_objs as go

def uscitePerMese():
    df = pd.read_csv('CodicePerGrafici/fileAggiornatoF2P.csv')
    df['Release date'] = df['Release date'].astype('datetime64[ns]')
    df['year'] = df['Release date'].apply(lambda x: x.year)
    df['month'] = df['Release date'].apply(lambda x: x.month)

    years =[2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
    fig = go.Figure()
    for i in years:
        df_year = df[df['year'] == i]
        series = df_year['month'].value_counts().sort_index()

        graph = go.Scatter(
            x=series.index,
            y=series,
            #fill='tozeroy',
            name = i
        )

        fig.add_trace(graph)
 
    fig.show() 

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

graficoGiochiPerAnno()
uscitePerMese()