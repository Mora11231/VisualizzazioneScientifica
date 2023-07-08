import re
import plotly.express as px
import plotly.graph_objs as go
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

def valoreOwnerStimato(x):
    a = x.split()
    return int((int(a[0]) + int(a[2]))/2)

def sunBurstPerCovidV2():
    df = pd.read_csv('CodicePerGrafici/fileAggiornatoF2P.csv')
    df = df[['Name','Release date','Categories','Estimated owners']]
    df['Estimated owners'] =  df.apply(lambda x:valoreOwnerStimato(x['Estimated owners']),axis=1)
    df = df[df['Estimated owners'] > 100]

    df['Release date'] = df['Release date'].astype('datetime64[ns]')
    df['Categories'] = df['Categories'].apply(lambda x: replaceNaN(x))

    df['Multi'] = df['Categories'].apply(lambda x: checkMultiplayer(x))
    df['Single'] = df['Categories'].apply(lambda x: checkSingleplayer(x))
    df['Coop'] = df['Categories'].apply(lambda x: checkCoop(x))


    pre = date(2020,1,1)
    post = date(2022,1,1)

    #pre_covid = df[df['Release date'].dt.date < pre]
    pre_covid = df[df['Release date'].dt.date < pre][df['Release date'].dt.date > date(2018,1,1)]
    covid = df[(df['Release date'].dt.date >= pre) & (df['Release date'].dt.date < post) ]
    post_covid = df[df['Release date'].dt.date >= post]

    pre_covid = pre_covid[['Estimated owners','Single','Multi','Coop']].groupby(['Single','Multi','Coop']).sum()
    pre_covid = pre_covid.reset_index()
    pre_covid['Estimated owners'] = pre_covid['Estimated owners'] / sum(pre_covid['Estimated owners'])*100
    
    covid = covid[['Estimated owners','Single','Multi','Coop']].groupby(['Single','Multi','Coop']).sum()
    covid = covid.reset_index()
    covid['Estimated owners'] = covid['Estimated owners'] / sum(covid['Estimated owners'])*100
   
    post_covid = post_covid[['Estimated owners','Single','Multi','Coop']].groupby(['Single','Multi','Coop']).sum()
    post_covid = post_covid.reset_index()
    post_covid['Estimated owners'] = post_covid['Estimated owners'] / sum(post_covid['Estimated owners'])*100

    print(post_covid)



    data = dict(
        labels = ['Pre-Covid', 'DuranteCovid', 'Post-Covid',
                  'SiglePlayer '+str(round(pre_covid[(pre_covid.Single == True) & (pre_covid.Coop == False)]['Estimated owners'].sum(),2))+"%",'Multiplayer '+str(round(pre_covid[(pre_covid.Multi == True) &(pre_covid.Coop == False)]['Estimated owners'].sum(),2))+"%",   'Coop '+str(round(pre_covid[pre_covid.Coop == True]['Estimated owners'].sum(),2))+"%",
                  'SiglePlayer '+str(round(covid[(covid.Single == True) & (covid.Coop == False)]['Estimated owners'].sum(),2))+"%",'Multiplayer '+str(round(covid[(covid.Multi == True) & (covid.Coop == False)]['Estimated owners'].sum(),2))+"%",           'Coop '+str(round(covid[covid.Coop == True]['Estimated owners'].sum(),2))+"%",
                  'SiglePlayer '+str(round(post_covid[(post_covid.Single == True) & (post_covid.Coop == False)]['Estimated owners'].sum(),2))+"%",  'Multiplayer '+str(round(post_covid[(post_covid.Multi == True) & (post_covid.Coop == False)]['Estimated owners'].sum(),2))+"%", 'Coop '+str(round(post_covid[post_covid.Coop == True]['Estimated owners'].sum(),2))+"%"],
        periodo=['','','','Pre-Covid','Pre-Covid','Pre-Covid','DuranteCovid','DuranteCovid','DuranteCovid', 'Post-Covid','Post-Covid','Post-Covid'],
    
        value = [0,0,0, sum(pre_covid[(pre_covid.Single == True) & (pre_covid.Coop == False)]['Estimated owners']),sum(pre_covid[(pre_covid.Multi == True) &  (pre_covid.Coop == False)]['Estimated owners']),sum(pre_covid[pre_covid.Coop == True]['Estimated owners']),
                        sum(covid[(covid.Single == True) & (covid.Coop == False)]['Estimated owners']),sum(covid[(covid.Multi == True) & (covid.Coop == False)]['Estimated owners']),sum(covid[covid.Coop == True]['Estimated owners']),
                        sum(post_covid[(post_covid.Single == True) & (post_covid.Coop == False)]['Estimated owners']),sum(post_covid[(post_covid.Multi == True) & (post_covid.Coop == False)]['Estimated owners']),sum(post_covid[post_covid.Coop == True]['Estimated owners'])],
    )
    fig = go.Figure(go.Sunburst(
    labels=data['labels'],
    parents=data['periodo'],
    values=data['value'],
    marker=dict(colors=['#648FFF', '#FFB000', '#DC267F']),
    ))
    
    fig.update_traces(textfont=dict(color='white', size=30))

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        font_family="Calibri",
        template="plotly_white",
    )
    
    fig.show()
sunBurstPerCovidV2()  