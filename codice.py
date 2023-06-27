import pandas as pd 
from datetime import datetime 
import plotly.express as px
import plotly.graph_objs as go

def checkPerData(x):
    if len(x) == 8:
        x = x[:4] + "1" + x[3:]
    return x
def valoreOwnerInt(x):
    a = x.split()
    return int(int(a[0]) + int(a[2]))/2

def valoreOwnerStimato(x,y):
    a = x.split()
    return int(int(a[0]) + int(a[2]))/2 + y

def aggiornaFile():
    df = pd.read_csv("games.csv",usecols=['Name','Release date','Tags','Estimated owners','Peak CCU','Price','DLC count','Supported languages','Windows','Mac','Linux','Metacritic score','User score','Positive','Negative','Achievements','Recommendations','Average playtime forever','Average playtime two weeks','Median playtime forever','Median playtime two weeks','Developers','Publishers','Categories','Genres','Tags'])
    df= df[df['Estimated owners'] != '0 - 20000']
    df= df[df['Estimated owners'] != '0 - 0']

    df['Release date'] = df['Release date'].apply(lambda x : x.replace(",",""))
    df['Release date'] = df['Release date'].apply(lambda x : checkPerData(x))
    df['Release date'] = df['Release date'].apply(lambda x : datetime.strptime(x, "%b %d %Y"))

    df.to_csv("fileAggiornato.csv",index=False)

def prova():
    df = pd.read_csv('fileAggiornato.csv')
    df['Estimated owners'] =  df.apply(lambda x:valoreOwnerStimato(x['Estimated owners'],x['Peak CCU']),axis=1)
    df['Gain'] = df['Estimated owners'] * df['Price']
    df = df.sort_values(by='Gain',ascending=False)
    layout = go.Layout(
        title='Ricavi dei primi x giochi',
        xaxis=dict(title='Gioco'),
        yaxis=dict(title='Guadagno'),
    )
    trace_gain = go.Bar(
        x=df['Name'].head(20),
        y=df['Gain'].head(20),
        name='Ricavo'
    )
    fig = go.Figure(data=[trace_gain],layout=layout)
    
    #fig = px.bar(df.head(20),'Name','Gain')
    
    fig.show()
    
    df = df.sort_values(by='Estimated owners',ascending=False)
    
    layout = go.Layout(
        title='Ricavi dei primi x giochi',
        xaxis=dict(title='Gioco'),
        yaxis=dict(title='Giocatori'),
    )
    trace_gain = go.Bar(
        x=df['Name'].head(20),
        y=df['Estimated owners'].head(20),
        name='Giocatori'
    )
    fig = go.Figure(data=[trace_gain],layout=layout)
    fig.show()

prova()