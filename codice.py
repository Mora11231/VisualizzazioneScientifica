import pandas as pd 
from datetime import datetime 
import plotly.express as px
import plotly.graph_objs as go
import re
from datetime import date

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
    #df= df[df['Estimated owners'] != '0 - 20000']
    df= df[df['Estimated owners'] != '0 - 0']

    df['Release date'] = df['Release date'].apply(lambda x : x.replace(",",""))
    df['Release date'] = df['Release date'].apply(lambda x : checkPerData(x))
    df['Release date'] = df['Release date'].apply(lambda x : datetime.strptime(x, "%b %d %Y"))

    df.to_csv("fileAggiornato.csv",index=False)
#aggiornaFile()

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
#prova()

def tryTree():
    x = [0.5,0.25,0.10,0.15]
    y = ['primo','secondo','terzo','quarto']
    
    d = {'val':x,'title':y}
    
    df = pd.DataFrame(d)
    
    fig = px.treemap(df, path=['title'], values='val')
   
    fig.update_layout(
        treemapcolorway = ['#67001f','#b2182b','#d6604d','#f4a582'],
        margin = dict(t=50, l=25, r=25, b=25),   
    )
    fig.show()
#tryTree()

def trySunBurst():
    data = dict(

    Generi=["Indie", "FPS", "MMO","Indie", "FPS", "MMO","Indie", "FPS", "MMO","Indie", "FPS", "MMO"],
    Anni = ['2017','2017','2017', '2018','2018','2018','2019','2019','2019','2020','2020','2020'],
    value=[0.7, 0.15, 0.15,0.5,0.35,0.15,0.25,0.35,0.40,0.10,0.70,0.20],
    
    )
    fig = px.sunburst(
    data,
    path=['Generi','Anni'],
    values='value',
    )
    fig.show()
#trySunBurst()

def checkF2P(x):
    if x != x:
        return False
    return bool(re.search(r'\b(?:\w+,\s)?Free to Play(?:,\s\w+)?\b', x))
   
    
def graficoTortaAppEGiochi():
    df = pd.read_csv('fileAggiornato.csv')
    df=df.Tags.dropna()
    df=df.apply(lambda x: checkF2P(x))
    f2p = (sum(df))
    p2p = len(df)-(f2p)

    fig = px.pie(values=[f2p,p2p],names=['F2P','P2P'])
    fig.show()

def graficoTortaAppEGiochiCrocetta():
    df = pd.read_csv('fileAggiornato.csv')
    f2p = df[df['Price'] == 0]
    f2p['F2P'] = True

    liar = df[df['Price'] != 0]
    liar['F2P'] = liar.Tags.apply(lambda x: checkF2P(x))

    n_f2p = (len(f2p)) + sum(liar.F2P)

    n_p2p = len(df)-(n_f2p)

    fig = px.pie(values=[n_f2p,n_p2p],names=['F2P','P2P'])
    fig.show()
    elaborato_df = pd.concat([f2p,liar]).sort_index()
    elaborato_df.to_csv("fileAggiornatoF2P.csv",index=False)
#graficoTortaAppEGiochiCrocetta()

def graficoBarrePerAnno():
    df = pd.read_csv('fileAggiornatoF2P.csv')
    df['Release date'] = df['Release date'].astype('datetime64[ns]')
    df['year'] = df['Release date'].apply(lambda x: x.year)
    
    giochiPerAnno= df['year'].value_counts().sort_index()
    giochiSum=giochiPerAnno.cumsum()

    giochiPerAnno[2013] =giochiSum[2013]
    print(giochiPerAnno)

    graph1 = go.Scatter(
        x=giochiPerAnno.index[16:-1],
        y= giochiPerAnno[16:-1],
        mode="markers+lines"
        )

    fig = go.Figure()
    fig.add_trace(graph1)

    fig.show()
#graficoBarrePerAnno()

def graficoBarrePerEstimated():
    df = pd.read_csv('fileAggiornato.csv')
    df['Estimated owners'] =  df.apply(lambda x:valoreOwnerStimato(x['Estimated owners'],x['Peak CCU']),axis=1)
    df['Release date'] = df['Release date'].astype('datetime64[ns]')
    df['year'] = df['Release date'].apply(lambda x: x.year)

    df = df[['Estimated owners','year']].groupby('year').sum()
    df = df['Estimated owners']

    sum_df = df.cumsum()
    df[2003] = sum_df[2003]

    fig = go.Figure()

    graph1 = go.Bar(
        x=df.index[6:-1],
        y=df[6:-1]  
        )
    
    graph2 = go.Scatter(
        x=sum_df.index[6:-1],
        y= sum_df[6:-1],
        mode="markers+lines"
        )
    
    fig.add_trace(graph1)
    fig.add_trace(graph2)
    fig.show()
#graficoBarrePerEstimated()

def uscitePerMese():
    df = pd.read_csv('fileAggiornatoF2P.csv')
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
#uscitePerMese()

def replaceNaN(x):
    if x!=x:
        return ""
    return x

def inserireGenere(x,i):
    if x.find(i) != -1:
        return True
    else:
        return False

def EstrazioneGeneri():
    df = pd.read_csv('fileAggiornatoF2P.csv')
    df['Genres'] = df['Genres'].apply(lambda x: replaceNaN(x))
    generi=set()

    for x in df['Genres']:
        if x == '':
            continue
        s = x.split(',')
        for i in s:
            generi.add(i)

    for i in generi:
        df[i] = df['Genres'].apply(lambda x: inserireGenere(x,i))
    #df.to_csv('fileAggiornatoGeneri.csv',index=False)

    print(df['Indie'].corr(df['Casual']))
#EstrazioneGeneri()


def checkMultiplayer(x):
    return bool(re.search(r'\b(?:\w+,\s)?Multi-player(?:,\s\w+)?\b', x))

def checkSingleplayer(x):
    return bool(re.search(r'\b(?:\w+,\s)?Single-player(?:,\s\w+)?\b', x))

def checkCoop(x):
    return bool(re.search(r'\b(?:\w+,\s)?Co-op(?:,\s\w+)?\b', x))

def checkMultiSingle(x):
    return (checkMultiplayer(x) & checkSingleplayer(x))

def sunBurstPerCovid():
    df = pd.read_csv('fileAggiornatoF2P.csv')
    df = df[['Name','Release date','Categories']]

    df['Release date'] = df['Release date'].astype('datetime64[ns]')
    df['Categories'] = df['Categories'].apply(lambda x: replaceNaN(x))

    df['Multi'] = df['Categories'].apply(lambda x: checkMultiplayer(x))
    df['Single'] = df['Categories'].apply(lambda x: checkSingleplayer(x))
    df['Coop'] = df['Categories'].apply(lambda x: checkCoop(x))
    df['MultiSingle'] = df['Categories'].apply(lambda x: checkMultiSingle(x))


    pre = date(2020,1,1)
    post = date(2022,1,1)

    pre_covid = df[df['Release date'].dt.date < pre]
    covid = df[(df['Release date'].dt.date >= pre) & (df['Release date'].dt.date < post) ]
    post_covid = df[df['Release date'].dt.date >= post]

    data = dict(
        periodo=['Pre-Covid','Pre-Covid','Pre-Covid','Pre-Covid','DuranteCovid','DuranteCovid','DuranteCovid','DuranteCovid', 'Covid','Covid','Covid','Covid'],
        generi=['SiglePlayer','Multiplayer','Coop','MultiSingle','SiglePlayer','Multiplayer','Coop','MultiSingle','SiglePlayer','Multiplayer','Coop','MultiSingle'],
        value = [sum(pre_covid.Single),sum(pre_covid.Multi),sum(pre_covid.Coop),sum(pre_covid.MultiSingle),sum(covid.Single),sum(covid.Multi),sum(covid.Coop),sum(covid.MultiSingle),sum(post_covid.Single),sum(post_covid.Multi),sum(post_covid.Coop),sum(post_covid.MultiSingle)]
    )

    fig = px.sunburst(
    data,
    path=['periodo','generi'],
    values='value',
    )
    fig.show()
#sunBurstPerCovid()

def replaceNanNum(x):
    if x != x:
        return 0
    return x
def diagrammaBarreF2PvsP2P():
    df = pd.read_csv('fileAggiornatoF2P.csv')
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
    df['P2P'] = series_P2P
    df['F2P'] = series_F2P

    df.reset_index(inplace=True)
    fig = px.bar(df, x='year', y=['P2P','F2P'],
            barmode='group',
            )
    fig.show()

#diagrammaBarreF2PvsP2P()