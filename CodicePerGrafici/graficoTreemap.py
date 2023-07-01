import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go



def valoreOwnerStimato(x):
    a = x.split()
    return int((int(a[0]) + int(a[2]))/2)

def treeMapEstimatedOwner():

    df = pd.read_csv('CodicePerGrafici/FileAggiornatoTags.csv')
    df['Estimated owners'] =  df.apply(lambda x:valoreOwnerStimato(x['Estimated owners']),axis=1)
    
    generi = ["Estimated owners","Action","Racing","SexualContent","MMO","Sim","Casual","Strategy","Sport","RPG","CardGame","Survival","Horror","Rogue-Like","Platformer","Fighter","Fantasy","Shooter","MOBA","HackSlash"]

    df = df[generi]

    for i in generi[1:]:
         df[i] = df [i] * df["Estimated owners"]
    
    df['Estimated owners'] = df['Estimated owners'].astype('str')
    
    df = df.sum()[1:]
    
  

    name = ["Tags per Estimated user"]
    parent = [""]
    val = [0]

    for j in df.index:
            name.append(j)
            parent.append("Tags per Estimated user")
            val.append(df[j])

    fig = go.Figure(go.Treemap(
        labels=name,
        parents=parent,
        values=val,
        marker=dict(
            colors=[]
        )

        ))
    fig.show()

def treeMapPeak():

    df = pd.read_csv('CodicePerGrafici/FileAggiornatoTags.csv')
    
    generi = ["Peak CCU","Action","Racing","SexualContent","MMO","Sim","Casual","Strategy","Sport","RPG","CardGame","Survival","Horror","Rogue-Like","Platformer","Fighter","Fantasy","Shooter","MOBA","HackSlash"]

    df = df[generi]

    for i in generi[1:]:
         df[i] = df [i] * df["Peak CCU"]
    
    df['Peak CCU'] = df['Peak CCU'].astype('str')
    
    df = df.sum()[1:]
    
  
    name = ["Tags per Peak CCU"]
    parent = [""]
    val = [0]

    for j in df.index:
            name.append(j)
            parent.append("Tags per Peak CCU")
            val.append(df[j])
    fig = go.Figure(go.Treemap(
        labels=name,
        parents=parent,
        values=val,
        marker=dict(
            colors=[]
        )

        ))
    fig.show()

def treeMapAvgTime():

    df = pd.read_csv('CodicePerGrafici/FileAggiornatoTags.csv')
    
    generi = ["Average playtime forever","Action","Racing","SexualContent","MMO","Sim","Casual","Strategy","Sport","RPG","CardGame","Survival","Horror","Rogue-Like","Platformer","Fighter","Fantasy","Shooter","MOBA","HackSlash"]

    df = df[generi]

    for i in generi[1:]:
         df[i] = df [i] * df["Average playtime forever"]
    
    df['Average playtime forever'] = df['Average playtime forever'].astype('str')
    
    df = df.sum()[1:]
    

    name = ["Tags per Average playtime forever"]
    parent = [""]
    val = [0]

    for j in df.index:
            name.append(j)
            parent.append("Tags per Average playtime forever")
            val.append(df[j])
    fig = go.Figure(go.Treemap(
        labels=name,
        parents=parent,
        values=val,
        marker=dict(
            colors=[]
        )

        ))
    fig.show()




treeMapEstimatedOwner()
treeMapPeak()
treeMapAvgTime()