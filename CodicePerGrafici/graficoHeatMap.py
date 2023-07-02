import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

def replaceNaN(x):
    if x!=x:
        return ""
    return x


def heatMapGeneriGiochi():
    df = pd.read_csv("CodicePerGrafici/fileAggiornatoTags.csv")
    generi = ["Action","Racing","SexualContent","MMO","Sim","Casual","Strategy","Sport","RPG","CardGame","Survival","Horror","Rogue-Like","Platformer","Fighter","Fantasy","Shooter","MOBA","HackSlash"]
   
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

    fig.update_layout(
        title = 'Relazione con i generi',
        plot_bgcolor = '#ffffff',
        paper_bgcolor = '#c7d5e0',
        

        font=dict( 
            size=17, 
            color="#171a21" 
        )

    )

    fig.update_xaxes(
        showgrid=False,
        dtick = 1,

    )

    fig.update_yaxes(
        showgrid=False,
        zerolinecolor = '#ffffff',
    )

    colorscale = [[0, '#542788'], [0.25, '#998ec3'],[0.75,'#f1a340'], [1, '#b35806']]
    fig.update_traces(
        colorscale=colorscale,
        )
    fig.update_traces(colorbar=dict(
        tickvals=[0.4,-0.09],
        ticktext=["Forte Relazione","Relazione Debole"]
    ))
    fig.show()
    

heatMapGeneriGiochi()
