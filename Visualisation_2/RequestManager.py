# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 20:01:14 2020

@author: Evann
"""

import pandas as pd
from pyvis.network import Network
import networkx as nx

class RequestManager:
    def __init__(self):
        self.df_aut= pd.read_csv("data/author.csv",sep=";")
        self.df_pub_Aut= pd.read_csv("data/publication_author.csv",sep=";")
        self.df_ven= pd.read_csv("data/venue.csv",sep=";")
        self.df_key= pd.read_csv("data/keyword.csv",sep=";")
        self.df_pub_key= pd.read_csv("data/publication_keywords.csv",sep=";")
        self.df_pub_year= pd.read_csv("data/publication_year.csv",sep=";")
        self.df_year= pd.read_csv("data/year.csv",sep=";")
        self.df_pub= pd.read_csv("data/publication.csv",sep=";")
        self.df_pub_venu= pd.read_csv("data/publication_venue.csv",sep=";",error_bad_lines=False)
        
        self.result = Network(height="750px", width="100%", bgcolor="#222222", font_color="white");
        self.result_df = None;
        
        self.maxLimit = 100
    
    # les infos sous forme de string 
    def getInfoAuteur(self,idAuteur):
        df = self.df_aut.loc[self.df_aut.author == idAuteur]
        if df.empty :
            return "Auteur non trouvé"
        else :
            df = df.iloc[0]
            return "Auteur"+"\n/nom: "+df['author']+"\n/nombre de publication: "+str(df['nbr_publication'])
    
    def getInfoKeyword(self,keyword):
        df = self.df_key.loc[self.df_key.keyword == keyword]
        if df.empty :
            return 
        else :
            df = df.iloc[0]
            return "Mot clé '"+df['keyword']+"'\nutilisé: "+str(df['nbr_utilisation'])
    
    def getInfoVenue(self,idVenu):
        df = self.df_ven.loc[self.df_ven.id_venue == idVenu]
        if df.empty :
            return
        else :
            df = df.iloc[0]
            return "Venue \n id: "+df['id_venue']+"\n nom: "+df['name_venue']+"\n type: "+df['type_venue']
    
    def getInfoPublication(self,idPub):
        df = self.df_pub.loc[self.df_pub.id_publication == idPub]
        if df.empty :
            return 
        else :
            df = df.iloc[0]
            return "Publication \n id: "+df['id_publication']+"\n/date publication: "+df['date_pub']+"\n/nombre auteur: "+str(df['nbr_authors']) +"\n titre article: "+df['article_title']+"\n categorie: "+df['categorie']
    
    def getAuteurIdFromName(self, nameAuteur):
        foundAutor = self.df_aut.loc[self.df_aut.author == nameAuteur].head(1)
        return foundAutor['author'].iloc[0]
    
    def getTitle_from_pub(self,idpub):
        df = self.df_pub.loc[self.df_pub.id_publication == idpub]
        if df.empty :
            return
        else :
            return str(df.iloc[0]["article_title"])
        
        
        
    def getTreeKeyword(self,keyword):
        dfTree = pd.merge(self.df_key.loc[self.df_key.keyword==keyword],  self.df_pub_key, left_on='keyword',          right_on='keyword',             how='left')
        dfTree = pd.merge(dfTree,                               self.df_pub,     left_on='id_publication',   right_on='id_publication',      how='left')
        dfTree = pd.merge(dfTree,                               self.df_pub_Aut, left_on='id_publication',   right_on='id_publication',      how='left')
        dfTree = pd.merge(dfTree,                               self.df_pub_venu,left_on='id_publication',   right_on='id_publication',      how='left')
        dfTree = pd.merge(dfTree,                               self.df_pub_year,left_on='id_publication',   right_on='id_publication',      how='left')
        dfTree = pd.merge(dfTree,                               self.df_aut,     left_on='author',        right_on='author',           how='left')    
        dfTree = pd.merge(dfTree,                               self.df_ven,     left_on='id_venue',         right_on='id_venue',            how='left')
        return dfTree

    # récupérer toute l'arborescence d'une publication    
    def getTreePublication(self,idPublication):
        dfTree = pd.merge(self.df_pub[self.df_pub.id_publication==idPublication], self.df_pub_key, left_on='id_publication',   right_on='id_publication',      how='left')
        dfTree = pd.merge(dfTree,                                       self.df_pub_Aut, left_on='id_publication',   right_on='id_publication',      how='left')
        dfTree = pd.merge(dfTree,                                       self.df_pub_venu,left_on='id_publication',   right_on='id_publication',      how='left')
        dfTree = pd.merge(dfTree,                                       self.df_pub_year,left_on='id_publication',   right_on='id_publication',      how='left')
        dfTree = pd.merge(dfTree,                                       self.df_aut,     left_on='author',        right_on='author',           how='left')    
        dfTree = pd.merge(dfTree,                                       self.df_ven,     left_on='id_venue',         right_on='id_venue',            how='left')
        dfTree = pd.merge(dfTree,                                       self.df_key,     left_on='keyword',          right_on='keyword',             how='left')
        return dfTree
    
    def getCoAuteurFromAuteur(self,idAuteur):
        #selectionner les publications de l'auteur rechrché 
        df_pub_auteur = self.df_pub_Aut.loc[self.df_pub_Aut.author == idAuteur]
        #selectionner les autres auteurs ayant les publciation de l'auteur recherché
        is_co_auteur = self.df_pub_Aut.id_publication.isin(df_pub_auteur.id_publication)
        # jointure entre le deux tables pour avoir les noms des auteurs 
        df_co_auteur=pd.merge(self.df_pub_Aut[is_co_auteur],self.df_aut, left_on='author', right_on='author',suffixes=('_inner', '_right'), how='inner')
        df_co_auteur = df_co_auteur[['author']].drop_duplicates()
        df_co_auteur = df_co_auteur.loc[df_co_auteur.author!=idAuteur]
        #df_co_auteur = df_co_auteur.rename(index={0: "id_co_author", 1: "name_author", 2: "author"})
        df_co_auteur = df_co_auteur.rename(columns={"author": "name_co_author"})
        df_co_auteur = df_co_auteur.assign(author=idAuteur)
        return df_co_auteur
    
    def getTreeAuteur(self,idAuteur):
        dfTree = pd.merge(self.df_aut[self.df_aut.author==idAuteur],    self.df_pub_Aut, left_on='author',        right_on='author',           how='left')
        dfTree = pd.merge(dfTree,                                       self.df_pub_venu,left_on='id_publication',   right_on='id_publication',      how='left')
        dfTree = pd.merge(dfTree,                                       self.df_pub_year,left_on='id_publication',   right_on='id_publication',      how='left') 
        dfTree = pd.merge(dfTree,                                       self.df_pub_key, left_on='id_publication',   right_on='id_publication',      how='left')    
        dfTree = pd.merge(dfTree,                                       self.df_ven,     left_on='id_venue',         right_on='id_venue',            how='left')
        dfTree = pd.merge(dfTree,                                       self.df_pub,     left_on='id_publication',   right_on='id_publication',      how='left')
        dfTree = pd.merge(dfTree,                                       self.df_key,     left_on='keyword',          right_on='keyword',             how='left')
        df_co_authors = self.getCoAuteurFromAuteur(idAuteur)
        dfTree = pd.merge(dfTree,           df_co_authors,     left_on='author',          right_on='author',           how='left')
        
        return dfTree
    
    # récupérer toute l'arborescence d'une venue
    def getTreeVenue(self,idVenue):
        dfTree = pd.merge(self.df_ven[self.df_ven.id_venue==idVenue],   self.df_pub_venu, left_on='id_venue',         right_on='id_venue',           how='left')
        dfTree = pd.merge(dfTree,                                       self.df_pub_Aut,  left_on='id_publication',   right_on='id_publication',     how='left')
        dfTree = pd.merge(dfTree,                                       self.df_pub_year, left_on='id_publication',   right_on='id_publication',     how='left') 
        dfTree = pd.merge(dfTree,                                       self.df_pub_key,  left_on='id_publication',   right_on='id_publication',     how='left')    
        dfTree = pd.merge(dfTree,                                       self.df_aut,      left_on='author',        right_on='author',          how='left')
        dfTree = pd.merge(dfTree,                                       self.df_pub,      left_on='id_publication',   right_on='id_publication',     how='left')
        dfTree = pd.merge(dfTree,                                       self.df_key,      left_on='keyword',          right_on='keyword',            how='left')
        return dfTree
    
    # Affichage de la liste des co-auteurs pour un auteur donné
    
    def selectCoAuteurFromAuteur(self, idAuteur):
        #selectionner les publications de l'auteur rechrché 
        df_pub_auteur = self.df_pub_Aut.loc[self.df_pub_Aut.author == idAuteur]
        if df_pub_auteur.empty :
            df= pd.read_csv("data/publication_author.csv",sep=";",nrows=self.maxLimit)
            G = nx.from_pandas_edgelist(df,source="id_publication",target="author")
            G_Dyn = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
            G_Dyn.from_nx(G)
            voisin = G_Dyn.get_adj_list();
            for node in G_Dyn.nodes :
                if not self.df_pub.loc[self.df_pub.id_publication == node['label']].empty : 
                    node["title"] = self.getInfoPublication(node["label"])
                    node["color"] = "#dd4b39"
                else :
                    node["title"] = self.getInfoAuteur(node["label"])
                    node["size"] =10*len(voisin[node["id"]])
                    node["shape"] = "star"
            self.result = G_Dyn
            self.result_df = df
            return
        #selectionner les autres auteurs ayant les publciation de l'auteur recherché
        is_co_auteur = self.df_pub_Aut.id_publication.isin(df_pub_auteur.id_publication)
        
        # jointeur entre le deux tables pour avoir les noms des auteurs 
        df_co_auteur=pd.merge(self.df_pub_Aut[is_co_auteur],self.df_aut, left_on='author', right_on='author',suffixes=('_left', '_right'), how='inner')
        df_co_auteur = df_co_auteur[['author']].drop_duplicates()
        df_co_auteur = df_co_auteur.assign(source=idAuteur)
        df_co_auteur = df_co_auteur.loc[df_co_auteur.author!=idAuteur]
        G = nx.from_pandas_edgelist(df_co_auteur,source="source",target="author")
        G_Dyn = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
        G_Dyn.from_nx(G)
        for node in G_Dyn.nodes :
            node["title"] = self.getInfoAuteur(node["label"])
            if node["label"] == idAuteur :
                node["color"] = "#dd4b39"
                node ["size"] = 20
                node["shape"] = "star"
        self.result = G_Dyn
        self.result_df = df_co_auteur
        
    #Affichage des mots-clés utilisés par un auteur donné

    def selectMotsClesFromAuteur(self, idAuteur):
        df_pub_auteur = self.df_pub_Aut.loc[self.df_pub_Aut.author == idAuteur]
        if  df_pub_auteur.empty :
            df = self.df_pub_Aut.merge(self.df_pub_key,on="id_publication").head(self.maxLimit)
            G = nx.from_pandas_edgelist(df,source="author",target="keyword")
            G_Dyn = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
            G_Dyn.from_nx(G)
            voisin = G_Dyn.get_adj_list();
            for node in G_Dyn.nodes :
                if not self.df_key.loc[self.df_key.keyword == node["label"]].empty :
                    node["title"] =  self.getInfoKeyword(node["label"])
                else :
                    node["color"] = "#dd4b39"
                    node ["size"] = len(voisin[node["id"]])*5
                    node["title"] = self.getInfoAuteur(node["label"])
                    node["shape"] = "star"
                    
            self.result = G_Dyn
            self.result_df = df
            return
        else :
            df_keyword_auteur = self.getTreeAuteur(idAuteur)
            G = nx.from_pandas_edgelist(df_keyword_auteur,source="author",target="keyword")
            G_Dyn = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
            G_Dyn.from_nx(G)
            for node in G_Dyn.nodes :
                if not self.df_key.loc[self.df_key.keyword == node["label"]].empty:
                    node["title"] =  self.getInfoKeyword(node["label"])
                else :
                    node["color"] = "#dd4b39"
                    node ["size"] = 20
                    node["title"] = self.getInfoAuteur(node["label"])
                    node["shape"] = "star"
            self.result = G_Dyn
            self.result_df = df_keyword_auteur
          
    #Affichage des publications d'un auteur donné
          
    def selectPublicationFromAuteur(self, idAuteur):
        df_pub_auteur = self.df_pub_Aut.loc[self.df_pub_Aut.author == idAuteur]
        if  df_pub_auteur.empty :
            df= pd.read_csv("data/publication_author.csv",sep=";",nrows=self.maxLimit)
            G = nx.from_pandas_edgelist(df,source="author",target="id_publication")
            G_Dyn = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
            G_Dyn.from_nx(G)
            voisin = G_Dyn.get_adj_list();
            for node in G_Dyn.nodes :
                if not self.df_pub.loc[self.df_pub.id_publication == node['label']].empty : 
                    node["title"] = self.getInfoPublication(node["label"])
                    node["label"] = self.getTitle_from_pub(node["label"])
                else :
                    node["title"] = self.getInfoAuteur(node["label"])
                    node["color"] = "#dd4b39"
                    node["size"] =10*len(voisin[node["id"]])
                    node["shape"] = "star"
            self.result = G_Dyn
            self.result_df = df
            return
        else :
            is_publication_auteur = self.df_pub.id_publication.isin(df_pub_auteur.id_publication) 
            df_publication_par_auteur=self.df_pub[is_publication_auteur]
            df_publication_par_auteur=df_publication_par_auteur.drop_duplicates().assign(source=idAuteur)
            G = nx.from_pandas_edgelist(df_publication_par_auteur,source="source",target="id_publication")
            G_Dyn = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
            G_Dyn.from_nx(G)
            for node in G_Dyn.nodes :
                if not self.df_pub.loc[self.df_pub.id_publication == node['label']].empty : 
                    node["title"] = self.getInfoPublication(node["label"])
                    node["label"] = self.getTitle_from_pub(node["label"])
                else :
                    node["title"] = self.getInfoAuteur(node["label"])
                    node["color"] = "#dd4b39"
                    node["size"] =20
                    node["shape"] = "star"
            self.result = G_Dyn
            self.result_df = df_publication_par_auteur
            
    
    
    def selectAuteurPublicationFromAuteur(self,idAuteur):
        df = self.df_aut.loc[self.df_aut.author == idAuteur]
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #Affichage des auteurs d'une publication donnée  

    def selectAuteurFromPublication(self,idpubliction):
        df_pub_auteur = self.df_pub_Aut.loc[self.df_pub_Aut.id_publication == idpubliction]
        if  df_pub_auteur.empty :
            df= pd.read_csv("data/publication_author.csv",sep=";",nrows=self.maxLimit)
            G = nx.from_pandas_edgelist(df,source="id_publication",target="id_author")
            G_Dyn = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
            G_Dyn.from_nx(G)
            voisin = G_Dyn.get_adj_list();
            for node in G_Dyn.nodes :
                if "conf/" in node["label"] : 
                    node["color"] = "#dd4b39"
                    node["size"] =10*len(voisin[node["id"]])
                    node["title"] = self.getInfoPublication(node["label"])
                else :
                    node["title"] = self.getInfoAuteur(node["label"])
            self.result = G_Dyn
            self.result_df = df
            return
        else :
            is_auteur = self.df_aut.id_author.isin(df_pub_auteur.id_author) 
            df =  self.df_aut[is_auteur].drop_duplicates().assign(source=idpubliction)
            G = nx.from_pandas_edgelist(df,source="source",target="id_author")
            G_Dyn = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
            G_Dyn.from_nx(G)
            for node in G_Dyn.nodes :
                if "conf/" in node["label"] : 
                    node["color"] = "#dd4b39"
                    node["size"] = 20
                    node["title"] = self.getInfoPublication(node["label"])
                else :
                    node["title"] = self.getInfoAuteur(node["label"])
            self.result = G_Dyn
            self.result_df = df
            
    #Affichage des lieux de publication pour un auteur donné  
    
    def selectLieuxPublicationFromAuteur(self,idAuteur):
        df_pub_auteur = self.df_pub_Aut.loc[self.df_pub_Aut.id_author == idAuteur]
        if  df_pub_auteur.empty :
            df = self.df_pub_venu.merge(self.df_ven,on="id_venue")
            df = df.merge(self.df_pub_Aut,on="id_publication")
            df = df.loc[:, ~df.columns.str.contains('^Unnamed')].head(self.maxLimit)
            G = nx.from_pandas_edgelist(df,source="id_author",target="name_venue")
            G_Dyn = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
            G_Dyn.from_nx(G)
            for node in G_Dyn.nodes :
                if "id_" in node["label"] :
                    node["title"] = self.getInfoAuteur(node["label"]) 
                    node["color"] = "#dd4b39"
                   
                else : 
                    node["title"] = "VENUE"
                    node["size"] =  20
            self.result = G_Dyn
            self.result_df = df
            return
            
             
        else :
            is_pub_auteur = self.df_pub_venu.id_publication.isin(df_pub_auteur.id_publication)
            df_liux_pub=pd.merge(self.df_pub_venu[is_pub_auteur],self.df_ven, left_on='id_venue', right_on='id_venue',suffixes=('_left', '_right'), how='inner')
            df =  df_liux_pub[['id_venue','name_venue','type_venue']].drop_duplicates().assign(source=idAuteur)
            G = nx.from_pandas_edgelist(df,source="source",target="name_venue")
            G_Dyn = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
            G_Dyn.from_nx(G)
    
            for node in G_Dyn.nodes :
                if "id_" in node["label"] :
                    node["title"] = self.getInfoAuteur(node["label"]) 
                    node["color"] = "#dd4b39"
                    node["size"] = 20
                else : 
                    node["title"] = "VENUE"
            self.result = G_Dyn
            self.result_df = df
            
            
    #Affichage des 10 mots-clés les plus utilisés pour un lieu de publication donné
    def selectTopMotsClesParLieux(self, idVenue):
        df_pub_venue = self.df_pub_venu.loc[self.df_pub_venu.id_venue == idVenue]
        if df_pub_venue.empty :
            df = self.df_pub_key.head(self.maxLimit)
            G = nx.from_pandas_edgelist(df,source="id_publication",target="keyword")
            G_Dyn = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
            G_Dyn.from_nx(G)
            voisin = G_Dyn.get_adj_list();
            for node in G_Dyn.nodes :
                if  node["label"].find("conf/") != -1:
                    node["title"] = self.getInfoPublication(node["label"]) 
                    node["color"] = "#dd4b39"
                    node["size"] = 2* len(voisin[node["id"]])
                else : 
                    node["title"] = "KEYWRD"
    
            self.result = G_Dyn
            self.result_df = df
            return
        else :
            is_pub_key = self.df_pub_key.id_publication.isin(df_pub_venue.id_publication)
            df_keywords = pd.merge(self.df_pub_key[is_pub_key],self.df_key, left_on='keyword', right_on='keyword',suffixes=('_left', '_right'), how='inner')
            df_keywords = df_keywords['keyword'].value_counts().head(10)
            df=  df_keywords.to_frame().assign(source=idVenue) 
            df = df.reset_index()
            G = nx.from_pandas_edgelist(df,source="source",target="index")
            G_Dyn = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
            G_Dyn.from_nx(G)
            
            for node in G_Dyn.nodes :
                if  node["label"].find("id_") != -1:
                    node["title"] = self.getInfoVenue(node["label"]) 
                    node["color"] = "#dd4b39"
                    node["size"] = 20
                else : 
                    node["title"] = "KEYWRD = " + node["label"]
    
            self.result = G_Dyn
            self.result_df = df_keywords
            
            
    # Les keywords les plus utilisés dans une année
    def selectTopMotsClesParAnnee(self,idAnnee):
        df_pub_year_idAnnee = self.df_pub_year.loc[self.df_pub_year.id_year == idAnnee]
        if df_pub_year_idAnnee.empty :
            return
        is_pub_key = self.df_pub_key.id_publication.isin(df_pub_year_idAnnee.id_publication)
        df_keywords = pd.merge(self.df_pub_key[is_pub_key],self.df_key, left_on='keyword', right_on='keyword',suffixes=('_left', '_right'), how='inner')
        df_keywords = df_keywords['keyword'].value_counts().head(self.maxLimit)
        df_keywords = df_keywords.to_frame().assign(source=idAnnee)
        df_keywords = df_keywords.reset_index()
        G = nx.from_pandas_edgelist(df_keywords,source="source",target="index")
        G_Dyn = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
        G_Dyn.from_nx(G)
            
        for node in G_Dyn.nodes :
            if  node["label"].find("id_") != -1:
                node["title"] = node["label"].replace("id_","")
                node["color"] = "#dd4b39"
                node["size"] = 20
            else : 
                node["title"] ="KEYWRD=" +str(node["label"])
        self.result = G_Dyn
        self.result_df = df_keywords