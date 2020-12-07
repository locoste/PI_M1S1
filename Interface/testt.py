import os
import dash
import dash_html_components as html
import dash_core_components as dcc
import flask
import test5
import pandas as pd
import dash_table

from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = 'Appli DBLP'

app.layout = html.Div([
    html.H2("Analyse de Données DBLP", style={'position': 'fixed', 'right':'0px'}),
    html.Link(href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,300i", rel="stylesheet"),
    html.Aside([
            html.Header([
                    html.Span([
                            html.A([
                                    html.Img(src="/assets/icom2.png", style={'top': '10px', 'right':'350px'}, alt="logo")
                                ])
                        ],className="logo")
                ],className="sidebar-header"),
            
                dcc.Location(id='url', refresh=False),
                html.Div(id='page-content'),
                html.Div(id='page-content2', style={'left': '200px'}),
                html.Div(id='page-content3'),
                

    
    html.Script(src="js/core.min.js"),
    html.Script(src="js/app.min.js"),
    html.Script(src="js/script.min.js")
], className="banner"),
])

divdenhaut = dcc.Tabs(
        id="tabs-with-classes",
        value='tab-1',
        parent_className='custom-tabs',
        className='custom-tabs-container',
        children=[
            dcc.Tab(
                label='Téléchargement',
                value='tab-1',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Importer',
                value='tab-2',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Affichage des données',
                value='tab-3', className='custom-tab',
                selected_className='custom-tab--selected'
            ),
    ]),

divdenbas = html.Div([
   html.Div(id='tabs-content-classes')
]),

divmain = html.Div([
    html.Main([
            html.Div([
                html.Div([
                        html.H4([
                            html.Strong('Integration Groupe Td 1'),
                            ], className="card-title"),
                        html.Div([
                                html.P('Vous pouvez accéder à chaque traveaux réalisé (Interface/Data Visu/Data analyse) par biais du volet qui se trouve à gauche')
                            ],className="card-body")
                    ], className="card")
                
                ],className="main-content"),

            
            
            
            html.Footer([
                    html.Div([
                            html.Div([
                                    html.P('Projet Intégré Groupe TD1 2020/2021', className="text-center text-md-left")
                                ],className="col-md-9")
                        ],className="row")
                ],className="site-footer")
        ],className="main-container"),
])

divnavbar = html.Div([
    html.Aside([
            html.Nav([
                    html.Ul([
                            
                                html.Li([
                                        html.A([
                                                html.Span(className="icon fa fa-home"),
                                                html.Span('Accueil', className="title")
                                            ], className="menu-link", href="http://localhost:8050/")
                                    ], className="menu-item active"),
                                
                                html.Li('Interface', className="menu-category"),
                                
                                html.Li([
                                        html.A([
                                                html.Span(className="icon fa fa-user"),
                                                html.Span('Groupe Interface', className="title"),
                                                html.Span(className="arrow")
                                            ],className="menu-link", href="/interface"),
                                        

                                    ], className="menu-item"),
                                
                                html.Li('Data Visualisation', className="menu-category"),
                                
                                html.Li([
                                        html.A([
                                                html.Span(className="icon fa fa-user"),
                                                html.Span('Groupe Data Visu 1', className="title"),
                                                html.Span(className="arrow")
                                            ],className="menu-link", href="http://localhost:10500/"),

                                    ], className="menu-item"),
                                
                                html.Li([
                                        html.A([
                                                html.Span(className="icon fa fa-user"),
                                                html.Span('Groupe Data Visu 2', className="title"),
                                                html.Span(className="arrow")
                                            ],className="menu-link", href="#"),

                                    
                                    ], className="menu-item"),
                                
                                html.Li('Data Analyse', className="menu-category"),
                                
                                html.Li([
                                        html.A([
                                                html.Span(className="icon fa fa-user"),
                                                html.Span('Groupe Data Analyse', className="title"),
                                                html.Span(className="arrow")
                                            ],className="menu-link", href="http://localhost:10546/"),
                                        
                                        html.Ul([
                                                html.Li([
                                                    html.A([
                                                            html.Span(className="dot"),
                                                            html.Span('Détection de communauté', className="title")
                                                        ], className="menu-link", href="http://localhost:10546/get_graph")
                                                    ],className="menu-item"),
                                                
                                                html.Li([
                                                    html.A([
                                                            html.Span(className="dot"),
                                                            html.Span('Détection de Topics', className="title")
                                                        ], className="menu-link", href="http://localhost:10546/Topics")
                                                    ],className="menu-item"),
                                                
                                                html.Li([
                                                    html.A([
                                                            html.Span(className="dot"),
                                                            html.Span('Prédiction', className="title")
                                                        ], className="menu-link", href="http://localhost:10546/get_prediction")
                                                    ],className="menu-item")
                                            ],className="menu-submenu")
                                    ], className="menu-item"),                  
                        ], className="menu")
                ], className="sidebar-navigation"),
        ], className="sidebar sidebar-icons-right sidebar-icons-boxed sidebar-expand-lg")
        ])


@app.callback(Output('tabs-content-classes', 'children'),
              [Input('tabs-with-classes', 'value')])

def render_content(tab):
    if tab == 'tab-1':
        return html.Div(
                [
                    dcc.Dropdown(
                        id='input1',
                        options=[
                            {'label': 'Publication', 'value': 'publ'},
                            {'label': 'Auteur', 'value': 'author'},
                            {'label': 'Lieu de publication', 'value': 'venue'}
                        ],
                        placeholder="Sélectionner une catégorie"
                    ), 
                    
                
                    dcc.Input(
                        id="input2",
                        placeholder='Entrez votre mot-clé de recherche',
                        type='text',
                        value='',
                        size= '35'
                    ),
                    html.Button(id='submit-button', type='submit', children='Submit'),
                    html.Div(id='output'),
          ],
        style = {'display': 'inline-block', 'width': '30%', 'margin':'auto'})
        
    elif tab == 'tab-2':
        return html.Div(
                [
                    dcc.Dropdown(
                        id='input4',
                        options=[
                            {'label': ';', 'value': ';'},
                            {'label': ',', 'value': ','},
                            {'label': 'Tabulation', 'value': '/t'}
                        ],
                        placeholder="Sélectionner un séparateur"
                    ),

                    dcc.Input(
                        id="input3",
                        placeholder='Entrez le nom de fichier UTF-16 contenant vos données',
                        type='text',
                        value='',
                        size= '52'
                    ), 
                    
                    
                    
                    html.Button(id='submit-button2', type='submit', children='Submit'),
                    html.Div(id='output2'),
          ],
        style = {'display': 'inline-block', 'width': '30%', 'margin':'auto'})
    elif tab == 'tab-3':
        return html.Div([
                html.H3('Tableau des données'),
                dash_table.DataTable(
                        id='table',
                        columns=[{"name": i, "id": i} for i in df.columns],
                        data=df.to_dict('records'),
                        )   
        ])
    elif tab == 'tab-4':
        return html.Div([
            html.H3('')
        ])

@app.callback(Output('output', 'children'),
              [Input('submit-button', 'n_clicks')],
              state=[State('input1', 'value'),
                     State('input2', 'value')])


def callback_signal(n_clicks,input1, input2):
    if input1 != '' and input2 != '': 
       # if os.path.exists("export.csv"):
        #    os.remove("export.csv")
        test5.test(input1, input2)
        global df
        df = pd.read_csv("export2.csv", encoding='utf-16', sep =";")
        #print(df.head())

@app.callback(Output('output2', 'children'),
              [Input('submit-button2', 'n_clicks')],
              state=[State('input3', 'value'),
                     State('input4', 'value')])

def callback_element_1(n_clicks,input3, input4):
    if input3 != '':
        #if os.path.exists("export.csv"):
         #   os.remove("export.csv")
        global df
        #test4.importer(input3)
        df = pd.read_csv(input3, sep = input4, encoding='utf-16')
        
# Update the index
@app.callback([Output('page-content', 'children'), Output('page-content2', 'children'), Output('page-content3', 'children')],
              dash.dependencies.Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return divnavbar, divmain, ""
    elif pathname == '/interface':
        return divnavbar, divdenhaut, divdenbas
    else:
        print ('')
        #return index_page
        

     
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
    
    

  
