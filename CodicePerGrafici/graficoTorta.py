import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
def graficoTortaF2PvsP2P():
    df = pd.read_csv('CodicePerGrafici/fileAggiornatoF2P.csv')
 
    serie = df.F2P.value_counts()
    
    fig = px.pie(values=serie,names=['P2P','F2P'],color_discrete_sequence=['#FFB000','#785EF0'])

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        font_family="Calibri",
        template="plotly_white",
        
        legend_title = "Legenda:",
        
        font=dict( 
            color='white',
            size=25, 
        )
    )


    fig.show()


def checkSoftware(x):
    if x.find('Software') != -1:
        return True
    return False

def replaceNaN(x):
    if x!=x:
        return ""
    return x

def graficoTortaAppEGiochi():
    df = pd.read_csv('CodicePerGrafici/fileAggiornatoF2P.csv')
    df['Genres'] = df['Genres'].apply(lambda x: replaceNaN(x))
    df['App'] = df['Genres'].apply(lambda x: checkSoftware(x))
    n_app = sum(df['App'])
    n_giochi = len(df)-n_app

    fig = px.pie(values=(n_app,n_giochi),names=['APP','Giochi'],color_discrete_sequence=['#785EF0','#FFB000'])

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        font_family="Calibri",
        template="plotly_white",
        
        legend_title = "Legenda:",
        
        font=dict( 
            size=25,
            color='white'
        )
    )

    fig.show()

def transizioneDaP2PaF2P():
    anno2010=[20,80]
    anno2015=[50,50]
    anno2020=[75,25]

    label=['In-game purchases','Game purchases']

    fig = make_subplots(rows=1, cols=3, specs=[[{"type": "pie"}, {"type": "pie"}, {"type": "pie"}]])

    fig.add_trace (go.Pie(values=anno2010,hole=0.5,title=2010, labels=['Revenue from In-Game Purchases','Revenue from Premium Games']), row=1, col=1)


    fig.add_trace (go.Pie(values=anno2015,hole=0.5, title=2015, labels=['Revenue from In-Game Purchases','Revenue from Premium Games']), row=1, col=2)


    fig.add_trace (go.Pie(values=anno2020,hole=0.5, title=2020, labels=['Revenue from In-Game Purchases','Revenue from Premium Games']), row=1, col=3)

    fig.update_traces(marker=dict(colors=['#785EF0','#FFB000']))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        font_family="Calibri",
        template="plotly_white",
        title_x=0.5,
        legend_x=0.35,
        legend_y=1.2,
        font=dict( 
            size=25,
            color='white'
        )
    )
    fig.show()

#graficoTortaAppEGiochi()
#graficoTortaF2PvsP2P()
transizioneDaP2PaF2P()