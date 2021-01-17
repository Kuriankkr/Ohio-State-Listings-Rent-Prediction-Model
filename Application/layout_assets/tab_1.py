# Installing Packages
from app import app
import dash_html_components as html
import dash_core_components as dcc
import dash

tab_1_layout = html.Div(
    
                  [
    dcc.Markdown(
        
        '''
        In the summer of 2020, I was planning to move from my current appartment and I started hunting online for appartment listings
        around Ohio State University. While googling, I noticed that multiple websites were putting up the same listing for different prices and 
        I found this to be annoying. Therefore, I decided to go ahead and create a  website that would help give an estimate of the price that I should be
        expecting to pay for an appartment, based on my preferences. 

        
        Click on the application tab to take a look!
       
       '''
                ),
    
    html.Br(),
    
    html.Div(
                [
                   dcc.Markdown(
        
'''
**Steps for taken creating the website**

1) Create the web-scraping script for scrapping from multiple websites

2) Store the scrapped data into a postgres database.

3) Develop a Linear Regression model that learns from the data in the database.

4) Containerize the scripts using Docker.

5) Create a pipeline for automating steps 1 - 3.
    
6) Create the scripts for the front end of the project.

7) Deploy the webapp.

'''
            
                                ),
                    
                ], className = 'first_half'
            ), 
    html.Br(),
    
    html.Div(
                [
        
                    dcc.Markdown(
        
'''      
** Future Work**

* Scrape more websites to feed more data and make the model more robust.
* Scale up the database to fit in more data.
* Give the user more flexibility while choosing options in the application tab
* Improve the aesthetics of the website and make it more user friendly

'''
            
                                )
                ], className = 'second_half'
        
            ),
    
            html.Br(),
    
            html.Div(

            # Create Banner Layout (Title and Logos)
            [
                html.Div(
                    [
                        dcc.Markdown('''
                            **Technologies Used**
                            '''),

                        # Insert Github Logo with href link
                        html.A(
                            [  
                                html.Img(src=app.get_asset_url(
                                    "python_logo.png"))
                            ], href="https://www.python.org/",
                        ),

                        # Insert Dash logo with href link
                        html.A(
                            [
                                html.Img(src=app.get_asset_url(
                                    "docker_logo.png"))
                            ], href="https://www.docker.com/",
                        ),

                        # Insert Dash logo with href link
                        html.A(
                            [
                                html.Img(src=app.get_asset_url(
                                    "airflow_logo.png"))
                            ], href="https://airflow.apache.org/",
                        ),

                        # Insert Dash logo with href link
                        html.A(
                            [
                                html.Img(src=app.get_asset_url(
                                    "postgresql_logo.png"))
                            ], href="https://www.postgresql.org/",
                        ),

                        # Insert Dash logo with href link
                        html.A(
                            [
                                html.Img(src=app.get_asset_url(
                                    "heroku_logo.png"))
                            ], href="https://www.heroku.com/",
                        ),

                    ], className="one-half column",
                )
            ], className="technology",
                
                
        ),
    
],
    style={'padding': '2rem 4rem 2rem 4rem', 'fontSize': 28,
              'font-family': "Myriad Pro", 'color': "#000000",         
             }
    
)


