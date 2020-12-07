# -*- coding: utf-8 -*-
import sys
import os
from pyvis.network import Network
from bs4 import BeautifulSoup


from RequestManager import RequestManager
from flask import Flask,render_template,redirect,request,url_for

app = Flask(__name__)
mainDir = os.path.dirname(os.path.realpath(__file__))

requestManager = RequestManager()

custom_style = """
            body{
                margin: 0;
                padding: 0;
                overflow: hidden;
                background-color: #222222;}
            h1{visibility: collapse;}
            #mynetwork {
                width: 100%;
                height: 100%;
                background-color: #222222;
                border: 0;
                position: absolute;
                top: 0;
                left: 0;}
        """


def ExecuteRequest(settings):
        
    singleElement = settings['SingleSelectorInput']
    if settings['RButtonNameSelect'] and singleElement!='':
        singleElement = requestManager.getAuteurIdFromName(singleElement)
        
    if settings['LimitResultCheck']:
        requestManager.maxLimit = settings['MaxResultSelector']
    else:
        requestManager.maxLimit = 500
    
    if settings['TableSelector'] == 0:
        
        coAutor = settings['CoautorCheck']
        publication = settings['PublicationCheck']
        keyword = settings['KeywordCheck']
        
        if coAutor and not publication and not keyword:
            requestManager.selectCoAuteurFromAuteur(singleElement)
            return True
        
        if publication and not coAutor and not keyword:
            requestManager.selectPublicationFromAuteur(singleElement)
            return True
        
        if keyword and not publication and not coAutor:
            requestManager.selectMotsClesFromAuteur(singleElement)
            return True
        
        if coAutor and publication and not keyword:
            print("pas complété")
            return False
        
        if coAutor and not publication and keyword:
            print("pas complété")
            return False
        
        if not coAutor and publication and keyword:
            print("pas complété")
            return False
        
        if coAutor and publication and keyword:
            print("pas complété")
            return False
        
        if not coAutor and not publication and not keyword:
            return False
        
    elif settings['TableSelector'] == 1:
        print("publication")
    elif settings['TableSelector'] == 2:
        print("venue")
    elif settings['TableSelector'] == 3:
        print("keywords")    
    
    return False


@app.route('/')
def Index():
    return render_template('request.html')

@app.route('/graph', methods=['POST'])
def Graph():
    settings = {}
    print(request.form)
    settings['TableSelector'] = int(request.form["TableSelect"])
    settings['SingleSelectorInput'] = request.form["SingleSelector"]
    settings['RButtonNameSelect'] = int(request.form.get("NameRadio",0))==1
    
    settings['CoautorCheck'] = request.form.get("AutorCheck",0)=='on'
    settings['PublicationCheck'] = request.form.get("PublicationCheck",0)=='on'
    settings['KeywordCheck'] = request.form.get("KeywordCheck",0)=='on'
    
    settings['YearCheck'] = request.form.get("YearCheck",0)=='on'
    settings['MinYearInput'] = int(request.form.get("MinYearInput",1900))
    settings['MaxYearInput'] = int(request.form.get("MaxYearInput",2020))
    
    settings['LimitResultCheck'] = request.form.get("MaxNbCheck",1)=='on'
    settings['MaxResultSelector'] = int(request.form.get("MaxNbInput",100))
    
    
    if ExecuteRequest(settings):
        graph = requestManager.result
        graph.save_graph("templates/graph.html")
        
        soup = BeautifulSoup(open("graph.html").read(),features="html.parser")
        style_tag = soup.find("style")
        style_tag.string = custom_style
        open("templates/graph.html", "w", encoding="utf-8").write(str(soup))
        return render_template('graph.html')
    else:
        return redirect(url_for('index'))
    