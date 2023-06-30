import pandas as pd
import plotly.express as px

def divisioneFascieDiPrezzo():
    df = pd.read_csv('CodicePerGrafici/fileAggiornatoF2P.csv')
    df=df[df['Price'] <100]
    #df=df[df['Price'] >5]
    fig = px.histogram(
        df,
        x=df.Price,
        nbins=30,
        histnorm='probability density',
        color_discrete_sequence=['#2a475e']
        )
    
    fig.update_layout(
        xaxis=dict(
            dtick=5,
            title=dict(
                text="Frequenza dei Prezzi",
            )
    ),
        yaxis=dict(
            title=dict(
                text="Prezzi",
            )
    )
    )

    fig.update_layout(
        title = "Divisione delle fascie di prezzo ",
        xaxis_title="Fasce di prezzo",
        yaxis_title="Percentuale giochi(%)",

        plot_bgcolor = '#c7d5e0',
        paper_bgcolor = '#ffffff',
        
        
        font=dict( 
            size=17, 
            color="#171a21" 
        )
    )

    fig.update_yaxes(
            zerolinecolor = '#c7d5e0',
        )

    fig.update_layout(bargap=0.1)
    fig.show()
divisioneFascieDiPrezzo()
