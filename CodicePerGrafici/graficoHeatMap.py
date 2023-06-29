import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

def replaceNaN(x):
    if x!=x:
        return ""
    return x

def heatMapGeneriGiochi():
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
heatMapGeneriGiochi()
