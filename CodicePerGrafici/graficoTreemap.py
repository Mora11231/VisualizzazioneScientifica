import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go



def valoreOwnerStimato(x):
    a = x.split()
    return int((int(a[0]) + int(a[2]))/2)

def treeMapEstimatedOwner():

    df = pd.read_csv('CodicePerGrafici/FileAggiornatoTags.csv')
    df=df[df['User score']>=80]
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
            colors=['#ffffff','#1E88E5','#FFC107','#004D40','#DA5B62','#D1A395','#511070','#86E42B','#49A67E','#793FDD','#8A597C','#EB4AF5','#F4E2F0','#F1118E','#758D0C','#D2674B','#B07363','#585B26','#AE6E8B']
        )

        ))
    
    fig.update_layout(
        font_family="Calibri",  
        title = "Categoria di giochi piu popolari per Estimated User",
        template="plotly_white",

        font=dict( 
            size=15, 
            color="#000000" 
        ),
       
    )
    fig.show()

def treeMapPeak():

    df = pd.read_csv('CodicePerGrafici/FileAggiornatoTags.csv')
    df=df[df['User score']>=80]
    
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
            colors=['#ffffff','#1E88E5','#FFC107','#004D40','#DA5B62','#D1A395','#511070','#86E42B','#49A67E','#793FDD','#8A597C','#EB4AF5','#F4E2F0','#F1118E','#758D0C','#D2674B','#B07363','#585B26','#AE6E8B']
        )

        ))
    
    fig.update_layout(
        font_family="Calibri",
        title = "Categoria di giochi piu popolari per Peak CCU",
        template="plotly_white",

        font=dict( 
            size=15,
        ),
       
    )
    fig.show()

def treeMapAvgTime():

    df = pd.read_csv('CodicePerGrafici/FileAggiornatoTags.csv')
    df=df[df['User score']>=80]
    
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
            colors=['#ffffff','#1E88E5','#FFC107','#004D40','#DA5B62','#D1A395','#511070','#86E42B','#49A67E','#793FDD','#8A597C','#EB4AF5','#F4E2F0','#F1118E','#758D0C','#D2674B','#B07363','#585B26','#AE6E8B']
        )
        ))
    
    fig.update_layout(
        font_family="Calibri",
        title = "Categoria di giochi piu popolari per Avg Time",
        template="plotly_white",
        
        font=dict( 
            size=15, 
        ),
       
    )
    fig.show()




#treeMapEstimatedOwner()
#treeMapPeak()
treeMapAvgTime()