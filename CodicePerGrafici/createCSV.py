from datetime import datetime
import pandas as pd
import re
def checkPerData(x):
    if len(x) == 8:
        x = x[:4] + "1" + x[3:]
    return x
def valoreOwnerInt(x):
    a = x.split()
    return int(int(a[0]) + int(a[2]))/2

def valoreOwnerStimato(x,y):
    a = x.split()
    return int(int(a[0]) + int(a[2]))/2 + y

def creazioneCSVCorretto():
    df = pd.read_csv("CodicePerGrafici/games.csv",usecols=['Name','Release date','Tags','Estimated owners','Peak CCU','Price','DLC count','Supported languages','Windows','Mac','Linux','Metacritic score','User score','Positive','Negative','Achievements','Recommendations','Average playtime forever','Average playtime two weeks','Median playtime forever','Median playtime two weeks','Developers','Publishers','Categories','Genres','Tags'])
    #df= df[df['Estimated owners'] != '0 - 20000']
    df= df[df['Estimated owners'] != '0 - 0']

    df['Release date'] = df['Release date'].apply(lambda x : x.replace(",",""))
    df['Release date'] = df['Release date'].apply(lambda x : checkPerData(x))
    df['Release date'] = df['Release date'].apply(lambda x : datetime.strptime(x, "%b %d %Y"))

    df.to_csv("CodicePerGrafici/fileAggiornato.csv",index=False)


def checkF2P(x):
    if x != x:
        return False
    return bool(re.search(r'\b(?:\w+,\s)?Free to Play(?:,\s\w+)?\b', x))

def replaceNan(x):
    if x != x:
        return 0
    return x

def creazioneCSVConF2P():
    df = pd.read_csv('CodicePerGrafici/fileAggiornato.csv')
    f2p = df[df['Price'] == 0]
    f2p['F2P'] = True

    liar = df[df['Price'] != 0]
    liar['F2P'] = liar.Tags.apply(lambda x: checkF2P(x))

    elaborato_df = pd.concat([f2p,liar]).sort_index()

    elaborato_df['Positive'] = elaborato_df['Positive'].astype('int64')
    elaborato_df['Negative'] = elaborato_df['Negative'].astype('int64')

    elaborato_df['User score'] = elaborato_df['Positive']/(elaborato_df['Positive']+elaborato_df['Negative'])*100

    elaborato_df['User score'] = elaborato_df['User score'].apply(lambda x: replaceNan(x))
    elaborato_df['User score'] = elaborato_df['User score'].apply(lambda x: int(x))
    
    elaborato_df.to_csv("CodicePerGrafici/fileAggiornatoF2P.csv",index=False)
creazioneCSVConF2P()



def replaceNaN(x):
    if x!=x:
        return ""
    return x


def inserireTag(x,i):
    for t in i:
        if x.find(t) != -1:
            return True
    return False
def EstrazioneGeneri():
    generi = ["Action","Racing","SexualContent","MMO","Sim","Casual","Strategy","Sport","RPG","CardGame","Survival","Horror","Rogue-Like","Platformer","Fighter","Fantasy","Shooter","MOBA","HackSlash"]
    keyword = [["Action"],['Racing','Driving'],['Sexual Content','Hentai','Nudity'],['Massively Multiplayer','MMORPG'],['Simulation','Sim'],['Casual'],['Strategy'],['Sports'],['RPG'],['Trading Card Game','Card Game','Card'],['Survival'],['Horror','Thriller'],['Rogue'],['Platformer'],['Fighter','Fighting'],['Fantasy'],['FPS','Shooter','Shoot'],['MOBA'],['Hack and Slash']]

    df = pd.read_csv('CodicePerGrafici/fileAggiornatoF2P.csv')
    df=df[['Name','Estimated owners','Peak CCU','Average playtime forever','Tags','User score']]

    df['Tags'] = df['Tags'].apply(lambda x: replaceNaN(x))
    for i in range(len(generi)):
        df[generi[i]] = df['Tags'].apply(lambda x: inserireTag(x,keyword[i]))
    df.to_csv('CodicePerGrafici/fileAggiornatoTags.csv',index=False)


   

#creazioneCSVCorretto()
#creazioneCSVConF2P()
EstrazioneGeneri()