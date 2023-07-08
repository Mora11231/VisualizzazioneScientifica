import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import re



def valoreOwnerStimatoD(x,y):
    a = x.split()
    return int(int(a[0]) + int(a[2]))/2 + y

def graficoBarrePerEstimated():
    df = pd.read_csv('CodicePerGrafici/fileAggiornato.csv')
    df['Estimated owners'] =  df.apply(lambda x:valoreOwnerStimatoD(x['Estimated owners'],x['Peak CCU']),axis=1)
    df['Release date'] = df['Release date'].astype('datetime64[ns]')
    df['year'] = df['Release date'].apply(lambda x: x.year)

    df = df[['Estimated owners','year']].groupby('year').sum()
    df = df['Estimated owners']

    sum_df = df.cumsum()
    df[2003] = sum_df[2003]

    fig = go.Figure()

    graph1 = go.Bar(
        x=df.index[6:-1],
        y=df[6:-1],
        marker=dict(
            color='#785EF0' 
            ),
        name ="Numero di owner"
        )
    
    graph2 = go.Scatter(
        x=sum_df.index[6:-1],
        y= sum_df[6:-1],
        line={'width': 4, 'color':'#648FFF'},
        marker=dict(
                size=12,
                line={'width': 2, 'color':'#648FFF'},
                color='white' 

            ),
        mode="markers+lines",
        name ="Numero di Acqusiti cumulativa"
        )
    

    fig.add_trace(graph1)
    fig.add_trace(graph2)

    fig.update_layout(
        template="plotly_white",
        font_family="Calibri",
        xaxis_title="Anni",
        yaxis_title="Numero di Acquisti",

        xaxis=dict(
            tickmode='array',
            tickvals=df.index[6:-1],
            ticktext=["<=2003",2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
        ),

        legend=dict(
            title = 'Legenda:',
        ),
        
        font=dict( 
            size=15, 
        ),
        yaxis=dict(
            dtick=500000000,
            range=(0,7100000000)
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

    fig.show()

def replaceNanNum(x):
    if x != x:
        return 0
    return x

def diagrammaBarreF2PvsP2P():
    df = pd.read_csv('CodicePerGrafici/fileAggiornatoF2P.csv')
    df['Release date'] = df['Release date'].astype('datetime64[ns]')

    df['year'] = df['Release date'].apply(lambda x: x.year)

    P2P = df[df['F2P'] == False]
    F2P = df[df['F2P'] == True]



    series_P2P = P2P[['year']].value_counts().sort_index()
    series_F2P = F2P[['year']].value_counts().sort_index()

    series_F2P.apply(lambda x : replaceNanNum(x))
    series_P2P.apply(lambda x : replaceNanNum(x))



    sum_p2p = series_P2P.cumsum().sort_index()
    series_P2P[2008] = sum_p2p[2008]
    series_P2P = series_P2P[11:-1]

    sum_f2p = series_F2P.cumsum().sort_index()
    series_F2P[2008] = sum_f2p[2008]
    series_F2P = series_F2P.loc[2008:]          #ci sono dei vuoti negli anni
    

    df = pd.DataFrame(columns = ['P2P', 'F2P'])
    df['P2P'] = round(series_P2P/(series_P2P+series_F2P)*100,1)
    df['F2P'] = round(series_F2P/(series_P2P+series_F2P)*100,1)

    df.reset_index(inplace=True)
    fig = px.bar(df, x=['P2P','F2P'], y='year',
            barmode='stack',
            orientation='h',
            text_auto=True,
            color_discrete_map={'P2P': '#FFB000', 'F2P': '#785EF0'}
            )
    fig.update_traces(textposition="inside")


    fig.update_layout(
        template="plotly_white",
        font_family="Calibri",
        xaxis_title="Estimated Users (%)",
        yaxis_title="Anni",
        legend=dict(
            orientation="h",
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ),

        legend_title = "Categoria",
        font=dict( 
            size=15, 
            color="#000000" 
        ),
        xaxis=dict(
            tickmode='array',
            range = (-5,105),
            tickvals=np.arange(0,101,5),
            ticktext=np.arange(0,101,5),
        ),

        yaxis=dict(
            tickmode='array',
            tickvals=np.arange(2008,2023,1),
            ticktext=np.arange(2008,2023,1)
        ),
    )
    
    
    fig.show()


def uscitePerMese():
    df = pd.read_csv('CodicePerGrafici/fileAggiornatoF2P.csv')
    df['Release date'] = df['Release date'].astype('datetime64[ns]')
    df['month'] = df['Release date'].apply(lambda x: x.month)


    fig = go.Figure()
    series = df['month'].value_counts(normalize=True).sort_index()

    graph = go.Bar(
            x=series.index,
            y=series,
            marker=dict(
                color='#785EF0' 
            )
            
        )
    
    fig.add_trace(graph)

    fig.update_layout(
        font_family="Calibri",
        template='simple_white',
        yaxis_title="Frequenza Relativa",
        xaxis=dict(
            tickmode='array',
            tickvals=series.index,
            ticktext=["Gen","Feb","Mar","Apr","Mag","Giu","Lug","Ago","Set","Ott","Nov","Dic"]
        ),
        
        font=dict( 
            size=15
        )
    )


    fig.update_xaxes(

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
    fig.show() 


def valoreOwnerStimato(x):
    a = x.split()
    return int((int(a[0]) + int(a[2]))/2)

def diagrammaBarreF2PvsP2PAvgTime():
    df = pd.read_csv('CodicePerGrafici/fileAggiornatoF2P.csv')
    df['Release date'] = df['Release date'].astype('datetime64[ns]')

    df['Estimated owners'] =  df.apply(lambda x:valoreOwnerStimato(x['Estimated owners']),axis=1)
    
    df['year'] = df['Release date'].apply(lambda x: x.year)

    P2P = df[df['F2P'] == False]
    F2P = df[df['F2P'] == True]

    P2P['Average playtime forever'] = P2P['Average playtime forever'] * P2P['Estimated owners']
    F2P['Average playtime forever'] = F2P['Average playtime forever'] * F2P['Estimated owners']

    series_P2P = P2P[['year','Average playtime forever']].groupby('year').sum().sort_index()
    series_F2P = F2P[['year','Average playtime forever']].groupby('year').sum().sort_index()

    sum_p2p = series_P2P.cumsum().sort_index()
    series_P2P.loc[2008] = sum_p2p.loc[2008]
    series_P2P = series_P2P[11:-1]

    sum_f2p = series_F2P.cumsum().sort_index()
    series_F2P.loc[2008] = sum_f2p.loc[2008]
    series_F2P = series_F2P.loc[2008:]          #ci sono dei vuoti negli anni
    

    df = pd.DataFrame(columns = ['P2P', 'F2P'])
    df['P2P'] = round(series_P2P/(series_P2P+series_F2P)*100,2)
    df['F2P'] = round(series_F2P/(series_P2P+series_F2P)*100,2)

    df.reset_index(inplace=True)
    fig = px.bar(df, x=['P2P','F2P'], y='year',
            barmode='stack',
            orientation='h',
            text_auto=True,
            color_discrete_map={'P2P': '#FFB000', 'F2P': '#785EF0'}
            )
    fig.update_traces(textposition="inside")


    fig.update_layout(
        template="plotly_white",
        font_family="Calibri",
        xaxis_title="Total Play Time (%)",
        yaxis_title="Anni",
        legend=dict(
            orientation="h",
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ),

        legend_title = "Categoria",
        font=dict( 
            size=15, 
            color="#000000" 
        ),
        xaxis=dict(
            tickmode='array',
            range = (-5,105),
            tickvals=np.arange(0,101,5),
            ticktext=np.arange(0,101,5),
        ),

        yaxis=dict(
            tickmode='array',
            tickvals=np.arange(2008,2023,1),
            ticktext=np.arange(2008,2023,1)
        ),
    )
    
    
    fig.show()

def diagrammaBarreF2PvsP2PPeakCCU():
    df = pd.read_csv('CodicePerGrafici/fileAggiornatoF2P.csv')
    df['Release date'] = df['Release date'].astype('datetime64[ns]')

    df['year'] = df['Release date'].apply(lambda x: x.year)

    P2P = df[df['F2P'] == False]
    F2P = df[df['F2P'] == True]

    series_P2P = P2P[['year','Peak CCU']].groupby('year').sum().sort_index()
    series_F2P = F2P[['year','Peak CCU']].groupby('year').sum().sort_index()

    sum_p2p = series_P2P.cumsum().sort_index()
    series_P2P.loc[2008] = sum_p2p.loc[2008]
    series_P2P = series_P2P[11:-1]

    sum_f2p = series_F2P.cumsum().sort_index()
    series_F2P.loc[2008] = sum_f2p.loc[2008]
    series_F2P = series_F2P.loc[2008:]          #ci sono dei vuoti negli anni
    

    df = pd.DataFrame(columns = ['P2P', 'F2P'])
    df['P2P'] = round(series_P2P/(series_P2P+series_F2P)*100,2)
    df['F2P'] = round(series_F2P/(series_P2P+series_F2P)*100,2)

    df.reset_index(inplace=True)
    fig = px.bar(df, x=['P2P','F2P'], y='year',
            barmode='stack',
            orientation='h',
            text_auto=True,
            color_discrete_map={'P2P': '#FFB000', 'F2P': '#785EF0'}
            )
    fig.update_traces(textposition="inside")


    fig.update_layout(
        template='plotly_white',
        font_family="Calibri",
        xaxis_title="Peak CCU (%)",
        yaxis_title="Anni",
        legend=dict(
            orientation="h",
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ),
        legend_title = "Categoria",
        font=dict( 
            size=15, 
        ),
        xaxis=dict(
            tickmode='array',
            range = (-5,105),
            tickvals=np.arange(0,101,5),
            ticktext=np.arange(0,101,5),
        ),

        yaxis=dict(
            tickmode='array',
            tickvals=np.arange(2008,2023,1),
            ticktext=np.arange(2008,2023,1)
        ),
    )
    
    
    fig.show()

def replaceNaN(x):
    if x!=x:
        return ""
    return x
def checkMultiplayer(x):
    return bool(re.search(r'\b(?:\w+,\s)?Multi-player(?:,\s\w+)?\b', x))

def checkSingleplayer(x):
    return bool(re.search(r'\b(?:\w+,\s)?Single-player(?:,\s\w+)?\b', x)) & (not checkMultiplayer(x))

def checkCoop(x):
    return bool(re.search(r'\b(?:\w+,\s)?Co-op(?:,\s\w+)?\b', x))


def graficoBarreSingleMultiCoop():
    df = pd.read_csv('CodicePerGrafici/fileAggiornatoF2P.csv')
    df = df[['Name','Categories','Estimated owners','Peak CCU','User score']]
    
    df['Estimated owners'] =  df.apply(lambda x:valoreOwnerStimato(x['Estimated owners']),axis=1)
    df = df[df['Estimated owners'] > 100]
    df['Categories'] = df['Categories'].apply(lambda x: replaceNaN(x))

    df['Multi'] = df['Categories'].apply(lambda x: checkMultiplayer(x) & (not checkCoop(x)))
    df['Single'] = df['Categories'].apply(lambda x: checkSingleplayer(x) & (not checkCoop(x)))
    df['Coop'] = df['Categories'].apply(lambda x: checkCoop(x))

    eu = df[['Estimated owners','Single','Multi','Coop']].groupby(['Single','Multi','Coop']).sum()
    eu = eu.reset_index()
    eu['Estimated owners'] = eu['Estimated owners'] / sum(eu['Estimated owners'])*100

    peakCCU = df[['Peak CCU','Single','Multi','Coop']].groupby(['Single','Multi','Coop']).sum()
    peakCCU = peakCCU.reset_index()
    peakCCU['Peak CCU'] = peakCCU['Peak CCU'] / sum(peakCCU['Peak CCU'])*100

    userScore = df[['User score','Single','Multi','Coop']].groupby(['Single','Multi','Coop']).sum()
    userScore = userScore.reset_index()
    userScore['User score'] = userScore['User score'] / sum(userScore['User score'])*100

    data = {
        'Tipo' : ['Estimated owner','Estimated owner','Estimated owner','Peak CCU','Peak CCU','Peak CCU','User scores','User scores','User scores'],
        'Categoria' : ['Single','Multi','Coop','Single','Multi','Coop','Single','Multi','Coop'],
        'val' : [sum(eu[eu['Single'] == True]['Estimated owners']),sum(eu[eu['Multi'] == True]['Estimated owners']),sum(eu[eu['Coop'] == True]['Estimated owners']),
                 sum(peakCCU[peakCCU['Single'] == True]['Peak CCU']),sum(peakCCU[peakCCU['Multi'] == True]['Peak CCU']),sum(peakCCU[peakCCU['Coop'] == True]['Peak CCU']),
                 sum(userScore[userScore['Single'] == True]['User score']),sum(userScore[userScore['Multi'] == True]['User score']),sum(userScore[userScore['Coop'] == True]['User score'])
                ]
    }

    data = pd.DataFrame(data)


    fig = px.bar(data[data['Tipo']=='Estimated owner'], x='Tipo',y='val',color='Categoria',color_discrete_map={'Single': '#648FFF', 'Multi': '#FFB000','Coop': '#DC267F'})

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        template='plotly_white',
        font_family="Calibri",
        xaxis_title="Indici ",
        yaxis_title="(%)",
        legend_title = "legenda",
        font=dict( 
            size=15, 
        ),
        
     )
    
    fig.update_traces(textposition="inside", width = 0.25)

    fig.show()
        
    
    
    
    

graficoBarreSingleMultiCoop()
#graficoBarrePerEstimated()
#diagrammaBarreF2PvsP2P()
#uscitePerMese()
#diagrammaBarreF2PvsP2PAvgTime()
#diagrammaBarreF2PvsP2PPeakCCU()

