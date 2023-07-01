import pandas as pd
import plotly.graph_objs as go
import numpy as np



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
            mode="markers+lines",
            marker=dict(
                color='#2a475e',
                size = 17
            )
        )

    fig = go.Figure()
    fig.add_trace(graph1)

    fig.update_layout(
        xaxis_title = 'Anno',
        yaxis_title = 'Numero di Giochi',
        title = 'Numero di giochi per anno',
        plot_bgcolor = '#ffffff',
        xaxis=dict(
            tickmode='array',
            tickvals=giochiPerAnno.index[16:-1],
            ticktext=[">=2013",2014,2015,2016,2017,2018,2019,2020,2021,2022]
        ),
        yaxis=dict(
            range=(0,11000)
        ),

        font=dict( 
            size=17, 
            color="#171a21" 
        )

    )

    fig.update_xaxes(
        showgrid=False,
        dtick = 1,

    )

    fig.update_yaxes(
        showgrid=True,
        dtick = 1000,
        gridcolor='#000000',
        zerolinecolor = '#000000',
        zerolinewidth = 0.1,
    )

    fig.show()

def graficoMediaPrezzoAnni():
    df = pd.read_csv('CodicePerGrafici/fileAggiornatoF2P.csv')
    df['Release date'] = df['Release date'].astype('datetime64[ns]')
    df['year'] = df['Release date'].apply(lambda x: x.year)
    df= df[df['year']>=2007]

    ser = pd.Series([6.5801,6.3455,6.3011,6.1364,6.0428,6.0313,6.2425,6.1468,6.4631,6.6657,6.7571,6.8168,7.2808,7.1186,7.0784,7.0181], index=[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022])

    P2P = df[df['Price'] > 5]
    p2p_series= P2P[['year','Price']].groupby('year').mean()

    fig = go.Figure()

    graph = go.Scatter(
        x=p2p_series.index[:-1],
        y=p2p_series.Price[:-1],
        mode="markers+lines",
        name='Prezzo Medio Senza F2P',
        marker=dict(
                color='#993404' 
            )
    )

    series = df[['year','Price']].groupby('year').mean()
    graph1 = go.Scatter(
        x=series.index[:-1],
        y=series.Price[:-1],
        mode="markers+lines",
        name='Prezzo Medio CON F2P',
        marker=dict(
                color='#d95f0e' 
            )
    )

    graph2 = go.Scatter(
        x=ser.index,
        y=ser,
        mode="markers+lines",
        name='income (/10 000)',
        marker=dict(
                color='#fe9929',
               
            )
    )
   
    fig = fig.add_trace(graph)
    fig = fig.add_trace(graph1)
    fig = fig.add_trace(graph2)

    fig.update_layout(
        xaxis_title = 'Anno',
        yaxis_title = '$',
        title = 'Prezzo medio dei giochi negli anni con stipendio medio(USA)',
        plot_bgcolor = '#ffffff',
        xaxis=dict(
            range=(2006.9,2022.1),
            tickmode='array',
            tickvals=series.index[:-1],
            ticktext=[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
        ),
        yaxis=dict(
            range=(5,17),
            tickmode='array',
            tickvals=np.arange(5.5,17,0.5),
            ticktext=np.arange(5.5,17,0.5)
        ),

        legend=dict(
            title = 'Leggenda:',
            bgcolor='white' 
        ),

        font=dict( 
            size=17, 
            color="#171a21" 
        )

    )

    fig.update_xaxes(
        showgrid=True,
        dtick = 1,
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor='#000000',
        zerolinecolor = '#000000',
        zerolinewidth = 0.1,
    )


    fig.show()

graficoMediaPrezzoAnni()
graficoGiochiPerAnno()
