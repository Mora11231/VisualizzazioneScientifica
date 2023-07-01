import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def graficoWordGeneri():
    df = pd.read_csv('CodicePerGrafici/fileAggiornatoTags.csv')
    df = df[["Action","Racing","SexualContent","MMO","Sim","Casual","Strategy","Sport","RPG","CardGame","Survival","Horror","Rogue-Like","Platformer","Fighter","Fantasy","Shooter","MOBA","HackSlash"]]

    df = df.sum()
    

    wc = WordCloud(width = 1920, height = 1080,background_color = 'white').generate_from_frequencies(df)

    
    plt.axis("off")
    plt.imshow(wc, interpolation = "bilinear")
    plt.show()

graficoWordGeneri()