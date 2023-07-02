import pandas as pd
import plotly.express as px
import numpy as np



def valoreOwnerStimato(x):
    a = x.split()
    return int((int(a[0]) + int(a[2]))/2)


def estitica(x):
    i = len(x)
    con=-1
    while (i>0):
        con+=1
        if (con%3==0):
            x=x[:i]+','+x[i:]
            con=0
        i-= 1
    return x[:-1]

def scatterOwnerPeakPerF2P():
    df = pd.read_csv('CodicePerGrafici/fileAggiornatoF2P.csv')
    df['Release date'] = df['Release date'].astype('datetime64[ns]')
    df['Estimated owners'] =  df.apply(lambda x:valoreOwnerStimato(x['Estimated owners']),axis=1)

    df['year'] = df['Release date'].apply(lambda x: x.year)
    df=df[df['F2P'] == True]
    df=df[df['Peak CCU'] > 50]
    df = df[['Estimated owners','Peak CCU']]

    df = df.reset_index()

    df= df.sort_values('Estimated owners')
    df['Estimated owners'] = df['Estimated owners'].astype('str')
    df['Estimated owners'] = df['Estimated owners'].apply(lambda x:estitica(x))

    fig = px.scatter(
        df, 
        x='Estimated owners',
        y='Peak CCU',
        color_discrete_sequence=['#d95f02']
        )

    fig.update_layout(
        title = "Estimated owner / Peak CCU",
        xaxis_title="Estimated owners",
        yaxis_title="Peak CCU",

        plot_bgcolor = '#ffffff',
        
        
        font=dict( 
            size=17, 
            color="#171a21" 
        ),

        xaxis=dict(
            tickmode='array',
        ),
    )
    
    fig.update_xaxes(
        range=(-0.5,11.5),
        showgrid=True,
        gridcolor='#000000',
    )

    fig.update_yaxes(
        range=(0,310000),
        showgrid=True,
        gridcolor='#000000',
        zerolinecolor = '#000000',
        zerolinewidth = 0.1,
    )
    fig.update_traces(marker={'size': 12})

    fig.show()

def scatterOwnerTimePerF2P():
    df = pd.read_csv('CodicePerGrafici/fileAggiornatoF2P.csv')
    df['Release date'] = df['Release date'].astype('datetime64[ns]')
    df['Estimated owners'] =  df.apply(lambda x:valoreOwnerStimato(x['Estimated owners']),axis=1)

    df=df[df['F2P'] == True]
    df=df[df['Average playtime forever'] > 0]

    df['Average playtime forever'] = df['Average playtime forever'].apply(lambda x: x/3600)
    df = df[['Estimated owners','Average playtime forever']]


    df = df.reset_index()
    
    df= df.sort_values('Estimated owners')
    df['Estimated owners'] = df['Estimated owners'].astype('str')
    df['Estimated owners'] = df['Estimated owners'].apply(lambda x:estitica(x))

    fig = px.scatter(
        df, 
        x='Estimated owners',
        y='Average playtime forever',
        color_discrete_sequence=['#d95f02']
        )

    fig.update_layout(
        title = "Estimated owners / PlayTime",
        xaxis_title="Estimated owners",
        yaxis_title="Ore di gioco",

        plot_bgcolor = '#ffffff',
        
        
        font=dict( 
            size=17, 
            color="#171a21" 
        ),

        xaxis=dict(
            tickmode='array',
        ),
    )
    
    fig.update_xaxes(
        range=(-0.5,10.5),
        showgrid=True,
        gridcolor='#000000',

    )

    fig.update_yaxes(
        range=(-0.5,10),
        showgrid=True,
        gridcolor='#000000',
        zerolinecolor = '#000000',
        zerolinewidth = 0.1,
    )
    fig.update_traces(marker={'size': 12})

    fig.show()

def assegnazione(x):
    if x >=80: return "Molto positive"
    if x >=60: return "Positive"
    if x >=40: return "Nella media"
    if x >=20: return "Negative"
    
    return "Estremamente negative"

def scatterQualita():
    df = pd.read_csv('CodicePerGrafici/fileAggiornatoF2P.csv')
    
    df['Estimated owners'] =  df.apply(lambda x:valoreOwnerStimato(x['Estimated owners']),axis=1)
    df['Valutazione'] = df['User score'].apply(lambda x: assegnazione(x))
    
    df = df[(df['Positive']+df['Negative']) > 20]
    df = df[df['User score']>0]


    df = df[['Estimated owners','Valutazione','User score']].value_counts()
    df = df.reset_index()
    df = df.rename(columns={0: 'Occorenze'})
    print(df)

    df['Size'] = df['Occorenze'] *20
    df = df.sort_values('Estimated owners')
    df['Estimated owners'] = df['Estimated owners'].astype('str')
    df['Estimated owners'] = df['Estimated owners'].apply(lambda x:estitica(x))

    

    fig = px.scatter(
            df, 
            x='User score',
            y='Estimated owners',
            color_discrete_sequence=['#2c7bb6','#abd9e9','#ffffbf','#fdae61','#d7191c'],
            color='Valutazione',
            size='Size',
            category_orders={'Valutazione': ["Molto positive","Positive","Nella media","Negative","Estremamente negative",]}
            )
    
    fig.update_layout(
        template = 'plotly_white',
        title = "Estimated owners / PlayTime",
        xaxis_title="Estimated owners",
        yaxis_title="Ore di gioco",

        
        font=dict( 
            size=17, 
            color="#171a21" 
        ),

        xaxis=dict(
            categoryorder='array', 
            categoryarray=["Estremamente negative","Negative","Nella media","Positive","Molto positive"]
        ),
    )
    
    fig.update_xaxes(
        range=(-1.5,101.5),

    )

    fig.update_yaxes(
        range=(-1.5,12.5),
        tickvals=np.arange(-1,13,1),
        ticktext=['0']
    )
    
    fig.show()

scatterQualita()
#scatterOwnerPeakPerF2P()
#scatterOwnerTimePerF2P()