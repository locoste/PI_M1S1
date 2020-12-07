# -*- coding: utf-8 -*-
import sys
import os
from pyvis.network import Network
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLineEdit, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPixmap


from UI_graph import Ui_GraphWindow
from UI_request import Ui_RequestWindow
from UI_list import Ui_ListWindow
from RequestManager import RequestManager
from PandasDFModel import DataFrameModel

mainDir = os.path.dirname(os.path.realpath(__file__))

class ListDialog(QDialog):
    def __init__(self, elementList, *args, **kwargs):
        super(ListDialog, self).__init__(*args, **kwargs)
        self.ui = Ui_ListWindow()
        self.ui.setupUi(self)
        self.elementList = elementList
        for elem in self.elementList:
            textItem = QLineEdit(elem)
            self.ui.ElementLayout.addWidget(textItem)
            
        self.ui.AddButton.clicked.connect(self.AddElement)
        self.ui.RemoveButton.clicked.connect(self.RemoveElement)
        
    def GetResults(self):
        if self.exec_() == QDialog.Accepted:
            return self.elementList
        else:
            return None
    
    def AddElement(self):
        textItem = QLineEdit()
        self.ui.ElementLayout.insertWidget(0,textItem)
        
    def RemoveElement(self):
        self.ui.ElementLayout.takeAt(0)

class GraphWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(GraphWindow, self).__init__(*args, **kwargs)
        self.ui = Ui_GraphWindow()
        self.ui.setupUi(self)
        self.webview = QWebEngineView()
        self.ui.GraphLayout.addWidget(self.webview)
        self.graphManager = GraphManager(self.webview)
        self.ui.actionCapturer.triggered.connect(self.SaveScreen)
        
    def SaveScreen(self):
        self.webview.grab().save("graph.png")
        msg = QMessageBox()
        msg.setWindowTitle("Info")
        msg.setText("Graph capturé avec succès")
        msg.exec_()
        
class RequestWindow(QMainWindow):
    def __init__(self, graphWindow, *args, **kwargs):
        super(RequestWindow, self).__init__(*args, **kwargs)
        self.ui = Ui_RequestWindow()
        self.ui.setupUi(self)
        self.requestManager = RequestManager()
        self.graphWindow = graphWindow
        
        self.ui.PreviewButton.clicked.connect(self.PreviewRequest)
        self.ui.ShowGraphButton.clicked.connect(self.ShowGraph)
        
        self.listVenues = []
        
    def ExecuteRequest(self):
        
        singleElement = self.ui.SingleSelectorInput.text()
        if self.ui.RButtonNameSelect.isChecked():
            if self.ui.TableSelector.currentIndex() > 0:
                singleElement = self.requestManager.getAuteurIdFromName(singleElement)
            
        if self.ui.LimitResultCheck.isChecked():
            self.requestManager.maxLimit = self.ui.MaxResultSelector.value()
        else:
            self.requestManager.maxLimit = 500
        
        if self.ui.TableSelector.currentIndex() == 0:
            
            coAutor = self.ui.AutorCheck.isChecked()
            publication = self.ui.PublicationCheck.isChecked()
            keyword = self.ui.KeywordCheck.isChecked()
            
            if coAutor and not publication and not keyword:
                self.requestManager.selectCoAuteurFromAuteur(singleElement)
                return True
            
            if publication and not coAutor and not keyword:
                self.requestManager.selectPublicationFromAuteur(singleElement)
                return True
            
            if keyword and not publication and not coAutor:
                self.requestManager.selectMotsClesFromAuteur(singleElement)
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
                msg = QMessageBox()
                msg.setWindowTitle("Graph Impossible")
                msg.setText(self.requestManager.getInfoAuteur(singleElement))
                msg.exec_()
                return False
            
        elif self.ui.TableSelector.currentIndex() == 1:
            print("publication")
        elif self.ui.TableSelector.currentIndex() == 2:
            print("venue")
        elif self.ui.TableSelector.currentIndex() == 3:
            print("keywords")    
        
        return False
        
        
        
    def PreviewRequest(self):
        isValid = self.ExecuteRequest()
        if isValid:
            model = DataFrameModel(self.requestManager.result_df)
            self.ui.PreviewTable.setModel(model)
        
    def ShowGraph(self):
        isValid = self.ExecuteRequest()
        if isValid:
            self.graphWindow.graphManager.GenerateGraph(self.requestManager.result)
            self.graphWindow.show()
        
    def closeEvent(self, event):
        self.graphWindow.close()
        
    def SelectVenues(self):
        dlg = ListDialog(self.listVenues)
        self.listVenues = dlg.GetResults()
    


        

class GraphManager:
    def __init__(self, webview):
        self.webview = webview
        self.graph = Network()
        self.graph.set_options('var options = {"autoResize": true, "height": "100%", "width": "100%", "locale": "fr", "clickToUse": false}')
        
        self.__custom_style__ = """
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
        
    def GenerateGraph(self, data):
        self.graph = data
        self.graph.barnes_hut(gravity=-40000, central_gravity=0.3, spring_length=250, spring_strength=0.01, damping=0.09, overlap=0)
        self.graph.save_graph("graph.html")
        graph_path = os.path.abspath(os.path.join(mainDir, "graph.html"))
        
        soup = BeautifulSoup(open("graph.html").read(),features="html.parser")
        style_tag = soup.find("style")
        style_tag.string = self.__custom_style__
        open("graph.html", "w", encoding="utf-8").write(str(soup))
        
        self.webview.load(QUrl.fromLocalFile(graph_path))
        

if __name__ == '__main__':
    
    #SETUP APP
    app = QApplication(sys.argv)
    themeFile = "darkorange.qss"
    with open(themeFile,"r") as theme:
        app.setStyleSheet(theme.read())
    
    #SETUP WINDOWS
    graph_win = GraphWindow()
    request_win = RequestWindow(graph_win)
    
    #DISPLAY WINDOWS
    request_win.show()
    
    app.exec_()
    sys.exit()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    