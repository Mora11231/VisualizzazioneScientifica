import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

def replaceNaN(x):
    if x!=x:
        return ""
    return x

def heatMapGeneriGiochiOutDate():
    df = pd.read_csv("CodicePerGrafici/fileAggiornatoGeneri.csv")

    df['Genres'] = df['Genres'].apply(lambda x: replaceNaN(x))
    generi=set()

    for x in df['Genres']:
        if x == '':
            continue
        s = x.split(',')
        for i in s:
            generi.add(i)
            
    data=[[]]

    for i in generi:
        lista=[]
        for j in generi:
            if i==j:
                lista.append(0)
            else:
                lista.append(df[i].corr(df[j]))
        data.append(lista)

    data=data[1:]

    fig = px.imshow(data,
                labels=dict(x="Genere", y="Genere", color="Productivity"),
                x=list(generi),
                y=list(generi)
               )
    fig.show()
    
    '''generi = list(generi)
    fig = go.Figure()
    heat = go.Heatmap(
        data,
        x=generi,
        y=generi
    )
    fig.add_trace(heat)
    fig.show()'''

def heatMapGeneriGiochi():
    df = pd.read_csv("CodicePerGrafici/fileAggiornatoTags.csv")

 
    generi = ["Action","Racing","SexualContent","MMO","Sim","Casual","Strategy","Sport","RPG","CardGame","Survival","Horror","Rouge","Platformer","Fighter","Fantasy","Shotter","MOBA","HackSlash"]

    print(df.columns)

    data=[[]]

    for i in generi:
        lista=[]
        for j in generi:
            if i==j:
                lista.append(float("nan"))
            else:
                lista.append(df[i].corr(df[j]))
        data.append(lista)

    data=data[1:]

    
    '''fig = px.imshow(data,
                labels=dict(x="Genere", y="Genere", color="Productivity"),
                x=generi,
                y=generi,
                )'''
    
    layout = go.Layout(
        title = 'indice di correlazione tra generi',
        xaxis = dict(
            tickmode = 'linear'
        )
    )
    
    heat = go.Heatmap(
        z=data,
        x=generi,
        y=generi,
        xgap = 5,
        ygap = 5,
    )
    
    fig = go.Figure(data=heat, layout=layout)
    fig.show()
    

heatMapGeneriGiochi()
