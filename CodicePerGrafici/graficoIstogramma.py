import pandas as pd
import plotly.express as px
import numpy as np

def divisionefasceDiPrezzo():
    df = pd.read_csv('CodicePerGrafici/fileAggiornatoF2P.csv')
    df=df[df['Price'] <100]
    #df=df[df['Price'] >5]
    fig = px.histogram(
        df,
        x=df.Price,
        nbins=20,
        histnorm='probability density',
        color_discrete_sequence=['#785EF0']
        )
    

    fig.update_layout(
        font_family="Calibri",
        template="plotly_white",
        xaxis_title="Fasce di prezzo",
        yaxis_title="Frequenza Relativa",
        xaxis=dict(
            tickmode='array',
            tickvals=np.arange(0,105,5),
            ticktext=['4.99','9.99','14.99','19.99','24.99','29.99','34.99','39.99','44.99','49.99','54.99','59.99','64.99','69.99','74.99','79.99','84.99','89.99','94.99','99.99','>=100']
        ),
        
        font=dict( 
            size=15, 
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
divisionefasceDiPrezzo()
