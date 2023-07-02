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
        font_family="Calibri",
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
        font_family="Calibri",
        template="plotly_white",
        title = "Divisione delle fascie di prezzo ",
        xaxis_title="Fasce di prezzo",
        yaxis_title="Percentuale giochi(%)",
        
        
        font=dict( 
            size=17, 
            color="#000000" 
        )
    )
    fig.update_yaxes(
       showgrid=True,
        gridwidth=2,
        linewidth=2,
        linecolor="black"
    )

    fig.update_xaxes(
        showgrid=True,
        gridwidth=2,
        linewidth=2,
        linecolor="black"

    )

    fig.update_layout(bargap=0.1)
    fig.show()
divisioneFascieDiPrezzo()
