#----------Packages----------
from app import app
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import pickle
import dash


available_indicators = [i for i in range(1,9)]
number_of_baths = [i for i in range(1,5)]


filename = 'finalized_model.sav'
model = pickle.load(open(filename, 'rb'))


tab_2_layout = html.Div([
                            html.H4("Location"),
                            dcc.Dropdown(
                                id = 'location',
                                options = [
                            
                                        {'label': 'East', 'value':'East'},
                                        {'label': 'West', 'value':'West'},
                                        {'label': 'South', 'value':'South'},
                                        {'label': 'North', 'value':'North'},
                                            ],
                                placeholder = "Select a location",
                                value = '',   
                            ),
                             
                            html.H4("Number of Beds"),
                            dcc.Dropdown(
                               id = 'Beds',
                               options=[{'label': i, 'value': i} for i in available_indicators],
                               placeholder = "Select the number of beds",
                               value = '',
                            ),
                         
                            html.H4("Number of Baths"),
                            dcc.Dropdown(
                                id = 'Baths',
                                options = [{'label': i, 'value': i} for i in number_of_baths],
                                placeholder = 'Select the number of baths',
                                value = '',
                            ),
                         
                            html.H4("Laundry"),
                            dcc.RadioItems(
                                id = 'Laundry',
                                options = [{'label': i, 'value': i} for i in ['In Unit', 'In Building']],
                                value = '',
                                labelStyle={'display': 'inline-block'},
                            ),
    
                            
                            html.H4("Furished"),
                            dcc.RadioItems(
                                id = 'Furnished',
                                options = [{'label': i, 'value': i} for i in ['Yes', 'No']],
                                value = '',
                                labelStyle={'display': 'inline-block'}
                            ),
                         
                            html.H4("Parking"),
                            dcc.RadioItems(
                                id = 'Parking',
                                options = [{'label': i, 'value': i} for i in ['Off-Street Parking', 'On-Street Parking']],
                                value = '',
                                labelStyle={'display': 'inline-block'}, 
                                
                            ),
                            
                            
    
                            html.Br(),
                            html.Br(),
    
                            html.Button('Click Me for the housing prediction', id='button'),
    
                            html.Br(),
                            html.Br(),
    
                            html.Div(id = 'my-output', style={'color': 'red'})
                    ])
        


@app.callback(
    Output('my-output','children'),
    [Input('button', 'n_clicks')],
    state = [State('location', 'value'),
            State( 'Beds', 'value'),
            State( 'Baths', 'value'),
            State( 'Laundry', 'value'),
            State( 'Furnished', 'value'),
            State( 'Parking', 'value')])
    
def predict_value(n_clicks,location_cho, beds, baths, laundry, furnished, parking):
    data = []
    data.append(beds)
    data.append(baths)
    
    
    if furnished == '':
         raise dash.exceptions.PreventUpdate
    elif furnished == 'Yes':
        data.append(1)
    else:
        data.append(0)
        
    if parking == '': 
        raise dash.exceptions.PreventUpdate
    elif parking == 'Off-Street Parking':
        data.append(1)
    else:
        data.append(0)
    
    if laundry == '': 
        raise dash.exceptions.PreventUpdate
    elif laundry == 'In Unit':
        data.append(1)
    else:
        data.append(0)
        
        
    if location_cho == '': 
        raise dash.exceptions.PreventUpdate
    elif location_cho == 'West':
        data.append(1)
        data.append (0)
        data.append(0)

    elif location_cho == "East":
        data.append(0)
        data.append (0)
        data.append(1)

    elif location_cho == "North":
        data.append(0)
        data.append (1)
        data.append(0)
    
    else:
        data.append(0)
        data.append (0)
        data.append(0)

    
    column_names = ["beds", "baths", "furnished","parking","laundry","location_West","location_North","location_East"]
    df = pd.DataFrame(columns = column_names)
    df.loc[len(df)] = data

    val_pred = model.predict(df)
    val_pred = int(val_pred[0][0])
    return "The predicted price for your housing choice is estimated to be  ${} ".format(round(val_pred,2))
    
