import pandas as pd
import plotly.express as px

def graficoTortaF2PvsP2P():
    df = pd.read_csv('CodicePerGrafici/fileAggiornatoF2P.csv')
 
    serie = df.F2P.value_counts()
    
    fig = px.pie(values=serie,names=['P2P','F2P'],color_discrete_sequence=['#785EF0','#FFB000'])

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        font_family="Calibri",
        template="plotly_white",
        
        legend_title = "Legenda:",
        
        font=dict( 
            size=15, 
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


#graficoTortaAppEGiochi()
graficoTortaF2PvsP2P()