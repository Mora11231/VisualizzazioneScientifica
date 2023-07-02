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
        )

    fig = go.Figure()
    fig.add_trace(graph1)

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        template="plotly_white",
        xaxis_title = 'Anno',
        yaxis_title = 'Numero di rilasci',
        xaxis=dict(
            tickmode='array',
            tickvals=giochiPerAnno.index[16:-1],
            ticktext=["<= 2013",2014,2015,2016,2017,2018,2019,2020,2021,2022]
        ),
        yaxis=dict(
            range=(0,11000)
        ),

        font=dict( 
            size=15, 
        )

    )


    fig.update_xaxes(
        showgrid=True,
        gridwidth=2,
        linewidth=2,
        linecolor="black"
        
    )

    fig.update_yaxes(
        showgrid=True,
        gridwidth=2,
        linewidth=2,
        linecolor="black"
    )


    fig.update_traces(
        line={'width': 4, 'color':'#648FFF'},
        marker=dict(
            size=12,
            line={'width':2, 'color':'#648FFF'},
            color='white'
        )
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
        name='Prezzo Medio VG, esclusi F2P ($)',
        line={'width': 4, 'color':'#648FFF'},
        marker=dict(
                size=8,
                line={'width':2, 'color':'#648FFF'},
                color='white'
            )
    )

    series = df[['year','Price']].groupby('year').mean()
    graph1 = go.Scatter(
        x=series.index[:-1],
        y=series.Price[:-1],
        mode="markers+lines",
        name='Prezzo Medio VG ($)',
        line={'width': 4, 'color':'#785EF0'},
        marker=dict(
            size=8,
            line={'width':2, 'color':'#785EF0'},
            color='white'
        )
    )

    graph2 = go.Scatter(
        x=ser.index,
        y=ser,
        mode="markers+lines",
        name='Reddito mediano (10k$)',
        line={'width': 4, 'color':'#DC267F'},
        marker=dict(
            size=8,
            line={'width':2, 'color':'#DC267F'},
            color='white'
        )
        
    )
   
    fig = fig.add_trace(graph)
    fig = fig.add_trace(graph1)
    fig = fig.add_trace(graph2)

    fig.update_layout(
        template="plotly_white",
        font_family="Calibri",
        xaxis_title = 'Anno',
        yaxis_title = '($)',
        xaxis=dict(
            range=(2006.9,2022.1),
            tickmode='array',
            tickvals=series.index[:-1],
            ticktext=[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
        ),
        yaxis=dict(
            range=(5,17),
            tickmode='array',
            tickvals=np.arange(0,17,1),
            ticktext=np.arange(0,17,1)
        ),

        legend=dict(
            title = 'Legenda:'
        ),

        font=dict( 
            size=15, 
            color="black"
        )

    )

    fig.update_xaxes(
        showgrid=True,
        gridwidth=2,
        linewidth=2,
        linecolor="black"
        
    )

    fig.update_yaxes(
        dtick=1,
        showgrid=True,
        gridwidth=2,
        linewidth=2,
        linecolor="black"
    )
    fig.update_traces(
        line={'width': 5}
    )
    fig.show()

graficoMediaPrezzoAnni()
graficoGiochiPerAnno()