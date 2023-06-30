import re
import plotly.express as px
import pandas as pd
from datetime import date


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

def checkMultiSingle(x):
    return (checkMultiplayer(x) & checkSingleplayer(x))

def sunBurstPerCovid():
    df = pd.read_csv('CodicePerGrafici/fileAggiornatoF2P.csv')
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
        periodo=['Pre-Covid','Pre-Covid','Pre-Covid','DuranteCovid','DuranteCovid','DuranteCovid', 'Covid','Covid','Covid'],
        generi=['SiglePlayer','Multiplayer','Coop','SiglePlayer','Multiplayer','Coop','SiglePlayer','Multiplayer','Coop'],
        value = [sum(pre_covid.Single),sum(pre_covid.Multi),sum(pre_covid.Coop),sum(covid.Single),sum(covid.Multi),sum(covid.Coop),sum(post_covid.Single),sum(post_covid.Multi),sum(post_covid.Coop)],
        
    )
    color_discrete_sequence=['#542788', '#998ec3', '#d8daeb', '#fee0b6','#f1a340','#b35806','#fee0b6','#f1a340','#b35806']
    fig = px.sunburst(
        data,
        path=['periodo','generi'],
        values='value'
    )
    
    fig.show()


def sunBurstPerCovidV2():
    df = pd.read_csv('CodicePerGrafici/fileAggiornatoF2P.csv')
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
        labels = ['Pre-Covid', 'DuranteCovid', 'Post-Covid','SiglePlayer','Multiplayer','Coop','SiglePlayer ','Multiplayer ','Coop ',' SiglePlayer',' Multiplayer',' Coop'],
        periodo=['','','','Pre-Covid','Pre-Covid','Pre-Covid','DuranteCovid','DuranteCovid','DuranteCovid', 'Post-Covid','Post-Covid','Post-Covid'],
        value = [0,0,0,sum(pre_covid.Single),sum(pre_covid.Multi),sum(pre_covid.Coop),sum(covid.Single),sum(covid.Multi),sum(covid.Coop),sum(post_covid.Single),sum(post_covid.Multi),sum(post_covid.Coop)],
        
    )
    fig = px.sunburst(
        names =data['labels'],
        parents=data['periodo'],
        values=data['value'],
        color_discrete_sequence=['#1b7837', '#998ec3', '#7fbf7b'],
    )
    
    fig.update_traces(textfont=dict(color='white'))

    fig.update_layout(
        title = "Divisione dei giochi in periodi di covid",

        plot_bgcolor = '#ffffff',

        legend=dict(
            title = 'Leggenda:',
            bgcolor='white' 
        ),
        
        font=dict( 
            size=17, 
            color="#171a21" 
        ),
        
    )
    
    fig.show()
sunBurstPerCovidV2()  