import dash
import pandas as pd
from dash import no_update , dcc , html
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots
import base64
import dash_extensions as de

# Read_Csv (Sales Data)
df1 = pd.read_csv(r"Dataset/Sales.csv",encoding="ISO-8859-1")
sales = pd.read_csv(r"Dataset/vgsales.csv",encoding="ISO-8859-1")

# Drop_NaN Values
df = df1.dropna()

# Sort the sales by the highest
North_xb = df.sort_values(by=['North America_xb'], ascending=False)[0:6]
Europe_xb = df.sort_values(by=['Europe_xb'], ascending=False)[0:6]
North_ps = df.sort_values(by=['North America_PS'], ascending=False)[0:6]
Europe_ps = df.sort_values(by=['Europe_PS'], ascending=False)[0:6]
Global_xb = df.sort_values(by=['Global_xb'], ascending=False)[0:6]
Global_ps = df.sort_values(by=['Global_PS'], ascending=False)[0:6]

sales['TotalSales'] = sales['Global_Sales'].groupby(sales['Year']).transform('sum')
df = sales.sort_values(by=['Year'], ascending=False)

# --------------------------------------------------------------------------
# 1-North America Sales
fig_NA = make_subplots(rows=2, cols=1)

fig_NA.add_trace(
    go.Bar(name="Playstation", y=North_ps["Game"], x=North_ps["North America_PS"], text=North_ps["North America_PS"],
           marker_color='cadetblue', orientation='h'),
    row=1,
    col=1,
)

fig_NA.add_trace(
    go.Bar(name="XBox", y=North_xb["Game"], x=North_xb["North America_xb"], text=North_xb["North America_xb"],
           marker_color='yellowgreen', orientation='h'),
    row=2,
    col=1,
)

fig_NA.update_layout(
    title={'text': "North America Sales: Xbox VS Playstation",
           'x': 0.5,
           'xanchor': 'center'
           },
    title_font_family="Times New Roman",
    title_font_color="black",
    yaxis2_title="Game",
    xaxis2_title="Global Sales in Billions",
    yaxis_title="Game",
    xaxis_title="VS"
)
fig_NA.update_xaxes(automargin=False, autorange=True)

fig_NA.update_yaxes(
    autorange="reversed")

# --------------------------------------------------------------------------
# 2-Europe Sales
fig_EU = make_subplots(rows=2, cols=1)

fig_EU.add_trace(
    go.Bar(name="Playstation", y=Europe_ps["Game"], x=Europe_ps["Europe_PS"], text=Europe_ps["Europe_PS"],
           marker_color='rgb(55, 83, 109)', orientation='h'),
    row=1,
    col=1,
)

fig_EU.add_trace(
    go.Bar(name="XBox", y=Europe_xb["Game"], x=Europe_xb["Europe_xb"], text=Europe_xb["Europe_xb"],
           marker_color='rgb(26, 118, 255)', orientation='h'),
    row=2,
    col=1,
)

fig_EU.update_layout(
    title={'text': "Europe Sales: Xbox VS Playstation",
           'x': 0.5,
           'xanchor': 'center'
           },
    title_font_family="Times New Roman",
    title_font_color="black",
    yaxis2_title="Game",
    xaxis2_title="Global Sales in Billions",
    yaxis_title="Game",
    xaxis_title="VS"
)
fig_EU.update_xaxes(automargin=False, autorange=True)

fig_EU.update_yaxes(
    autorange="reversed")

# --------------------------------------------------------------------------
# 3- Global Sales

fig_GL = go.Figure(data=[
    go.Bar(y=Global_xb["Game"], x=Global_xb["Global_xb"], orientation='h', name="XBox", marker_color="#13c385",
           text=Global_xb["Global_xb"]),
    go.Bar(y=Global_ps["Game"], x=Global_ps["Global_PS"], orientation='h', name="Playstation", marker_color='#136ec3',
           text=Global_ps["Global_PS"])
])

fig_GL.update_layout(
    barmode='stack',
    title={'text': "Global Sales: Xbox VS Playstation",
           'x': 0.5,
           'xanchor': 'center'
           },
    title_font_family="Times New Roman",
    title_font_color="black",
    yaxis_title="Game",
    xaxis_title="Global Sales in Billions")

fig_GL.update_yaxes(
    autorange="reversed")

fig_GL.update_traces(textfont_size=12, textangle=0, textposition="auto", cliponaxis=False)

# --------------------------------------------------------------------------
# 4-Number of games by Genre
fig_BU = go.Figure()

fig_BU.add_trace(go.Scatter(
    y=["Action", "Shooter", "Sports", "Racing", "Adventure", "Action-Adventure", "Simulation", "Fighting", "Puzzle"],
    x=[108, 57, 56, 40, 34, 24, 16, 14, 5],
))

fig_BU.update_traces(mode='markers', marker=dict(sizemode='area',
                                                 line_width=2,
                                                 size=[1400, 1300, 1200, 1000, 800, 500, 300, 200, 100],
                                                 color=["#a625ad", "#a625ad", 7, 7, "#a625ad", 7, 7, 7, 7]))

fig_BU.update_layout(
    title={'text': "<b>Number of Games Created by Genre</b>",
           'x': 0.5,
           'xanchor': 'center'
           },
    width=550, height=550,

    xaxis=dict(
        title='Number of Games Created',

    ),
    yaxis=dict(
        title='Genre',

    )
)

fig_BU.update_yaxes(
    autorange="reversed")

fig_BU.add_annotation(x=53, y=0.4,
                      text="Target 2",
                      showarrow=True,
                      arrowhead=1)
fig_BU.add_annotation(x=102, y=-0.6,
                      text="Target 1",
                      showarrow=True,
                      arrowhead=1)
fig_BU.add_annotation(x=30, y=3.50,
                      text="Target 3",
                      showarrow=True,
                      arrowhead=1)

# --------------------------------------------------------------------------
# time series chart
fig_time = px.line(df, x=df['Year'].unique(), y=df['TotalSales'].unique(),
                   color_discrete_sequence=px.colors.qualitative.G10)

fig_time.update_layout(
    title={'text': "<b>Global Sales from 1980-2020</b>",
           'x': 0.5,
           'xanchor': 'center'
           },
    width=550, height=550,

    xaxis=dict(
        title='Year'
    ),
    yaxis=dict(
        title='Global Sales in Billions $'
    )
)
# --------------------------------------------------------------------------
# ISO_Data
iso = pd.read_csv(r"Dataset/GamingStudy_data-ISO.csv",encoding="ISO-8859-1")

# Gaming Study Data set

study = pd.read_csv(r"Dataset/GamingStudy_data.csv",encoding="ISO-8859-1")

# Clean the Data
study_na = study.dropna()
study_a = study_na.drop(columns=study_na.columns[0:2], axis=1, inplace=True)

# Group the Values
study_na["SWL_T"] = study_na["SWL_T"].replace(range(5, 10), value="Extremely Dissatisfied")
study_na["SWL_T"] = study_na["SWL_T"].replace(range(10, 15), value="Dissatisfied ")
study_na["SWL_T"] = study_na["SWL_T"].replace(range(15, 20), value="Slightly Dissatisfied")
study_na["SWL_T"] = study_na["SWL_T"].replace(to_replace=(20), value="Neutral")
study_na["SWL_T"] = study_na["SWL_T"].replace(range(21, 26), value="Slightly Satisfied")
study_na["SWL_T"] = study_na["SWL_T"].replace(range(26, 31), value="Satisfied")
study_na["SWL_T"] = study_na["SWL_T"].replace(range(31, 36), value="Extremely Satisfied")

study_na['GAD_T'] = study_na['GAD_T'].replace(range(0, 5), value="Low Risk")
study_na['GAD_T'] = study_na['GAD_T'].replace(range(5, 10), value="Mild Risk")
study_na['GAD_T'] = study_na['GAD_T'].replace(range(10, 15), value="Moderate Risk")
study_na['GAD_T'] = study_na['GAD_T'].replace(range(15, 22), value="Severe Risk")

study_na['SPIN_T'] = study_na['SPIN_T'].replace(range(0, 21), value="No Risk")
study_na['SPIN_T'] = study_na['SPIN_T'].replace(range(20, 31), value="Mild Risk")
study_na['SPIN_T'] = study_na['SPIN_T'].replace(range(31, 41), value="Moderate Risk")
study_na['SPIN_T'] = study_na['SPIN_T'].replace(range(41, 50), value="Severe Risk")
study_na['SPIN_T'] = study_na['SPIN_T'].replace(range(50, 69), value="Very Severe Risk")

study_na['Hours'] = study_na['Hours'].replace(range(0, 30), value="Under 30 hours")
study_na['Hours'] = study_na['Hours'].replace(range(30, 50), value="From 30 to 50")
study_na['Hours'] = study_na['Hours'].replace(range(50, 100), value="From 50 to 100")
study_na['Hours'] = study_na['Hours'].replace(range(100, 200), value="Over 100 Hours")

study_na['Age'] = study_na['Age'].replace(range(18, 21), value="18-20")
study_na['Age'] = study_na['Age'].replace(range(21, 25), value="21-24")
study_na['Age'] = study_na['Age'].replace(range(25, 30), value="25-29")
study_na['Age'] = study_na['Age'].replace(range(30, 35), value="30-34")
study_na['Age'] = study_na['Age'].replace(range(35, 60), value="34+")

pyramid = study_na.sort_values(by=['Age'], ascending=False)

# Check the Value counts
study_na["Age"].value_counts()

# --------------------------------------------------------------------------
# 5- SunBurst Graph (only first 50 Values)
platform = study_na['Platform'][:100]
genre = study_na['Genre'][:100]
game = study_na["Game"][:100]

fig_SB = px.sunburst(study_na,
                     path=[platform, genre, game],
                     width=550, height=550)
fig_SB.update_layout(title={'text': "<b> 100 Game Distribution By Genre</b>",
                            'x': 0.5,
                            'xanchor': 'center'})

# --------------------------------------------------------------------------
# 6- Sun Graph (M)

fig_M = go.Figure(go.Sunburst(

    labels=["Game Genre", "Action", "Guild Wars 2", "Diablo 3", "Skyrim", "MOBA", "League of Legends",
            "Heroes of the Storm"
        , "Fantasy", "World of Warcraft", "Strategy", "Starcraft 2", "Hearthstone", "Shooter", "Destiny",
            "Counter Strike",
            "Other"],

    parents=["", "Game Genre", "Action", "Action", "Action", "Game Genre", "MOBA", "MOBA", "Game Genre", "Fantasy",
             "Game Genre", "Strategy", "Strategy", "Game Genre", "Shooter", "Shooter", "Game Genre",
             "Game Genre", "Other", "Game Genre"],

    values=[2588, 304, 87, 139, 78, 791, 700, 91, 202, 202, 546, 395, 151, 436, 68, 368, 400],
    marker_colors=['#9f25ad']))

fig_M.update_layout(width=550, height=550)
fig_M.update_layout(title={'text': "<b>All Games Distribution by Genre</b>",
                           'x': 0.5,
                           'xanchor': 'center'})

# --------------------------------------------------------------------------
# 7-World Map countries vs hours

fig_W = px.choropleth(iso, locations="Residence_ISO3",
                      color="Hours",
                      hover_name="Number of players",
                      color_continuous_scale=px.colors.sequential.Plasma)

# --------------------------------------------------------------------------
# 8- Word Cloud


# --------------------------------------------------------------------------
# Tree map
fig_Tr = px.treemap(study_na, path=["Gender", "Genre", 'Age', 'SWL_T'],
                    color='Narcissism',
                    color_continuous_scale='RdBu')
fig_Tr.update_layout(margin=dict(t=50, l=25, r=25, b=25))

fig_Tr1 = px.treemap(study_na, path=["Gender", 'Age', 'SWL_T'],
                     color='Narcissism',
                     color_continuous_scale='deep')
fig_Tr1.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# --------------------------------------------------------------------------
# Pie chart
night_colors = ['#8425ad', '#256ead', '#2599ad', "#259fad"
    , '#25ad49']
fig_pie = go.Figure(data=[go.Pie(labels=study_na["Age"], values=study_na["Age"].value_counts(), pull=[0.1, 0, 0, 0],
                                 marker_colors=night_colors)])

fig_pie.update_layout(width=550, height=550)
fig_pie.update_layout(margin=dict(t=0, b=1, l=1, r=1))
fig_pie.update_layout(
    title={'text': "<b>Targeted Age Group</b>",
           'x': 0.5,
           'xanchor': 'center'})

fig_degree = go.Figure(data=[go.Pie(labels=study_na["Degree"], values=study_na["Degree"].value_counts(), hole=.4,

                                    marker_colors=['#0b3b8c', '#4c25ad'])])
fig_degree.update_layout(width=550, height=550)

fig_degree.update_layout(margin=dict(t=0, b=1, l=1, r=1))
fig_degree.update_layout(title={'text': "<b>Targeted Degree</b>",
                                'x': 0.5,
                                'xanchor': 'center'})

fig_work = go.Figure(data=[go.Pie(labels=study_na["Work"], values=study_na["Work"].value_counts(), hole=.4,

                                  marker_colors=['#9f25ad', '#9f25ad'])])
fig_work.update_layout(width=550, height=550)
fig_work.update_layout(margin=dict(t=0, b=1, l=1, r=1))
fig_work.update_layout(title={'text': "<b>Targeted Status</b>",
                              'x': 0.5,
                              'xanchor': 'center'})

# --------------------------------------------------------------------------
# Dash code

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


image_filename3 = "assets/final.png"
encoded_image3 = base64.b64encode(open(image_filename3, 'rb').read())

image_filename5 = "assets/des.png"
encoded_image5 = base64.b64encode(open(image_filename5, 'rb').read())

image_filename4 = "assets/testtt.png"
encoded_image4 = base64.b64encode(open(image_filename4, 'rb').read())

image_filename7 = "assets/test3.png"
encoded_image7 = base64.b64encode(open(image_filename7, 'rb').read())

url = "https://assets1.lottiefiles.com/packages/lf20_xsrtzvyq.json"
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

image_filename = "assets/Plotly-World_Cloud.png"
image_filename1 = "assets/Wordcloud-freq.png"
image_filename2 = "assets/Wordcloud-platform.png"
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
encoded_image1 = base64.b64encode(open(image_filename1, 'rb').read())
encoded_image2 = base64.b64encode(open(image_filename2, 'rb').read())
why = html.Img(src='data:Plotly-World_Cloud.png;base64,{}'.format(encoded_image.decode()))
freq = html.Img(src='data:Wordcloud-freq.png;base64,{}'.format(encoded_image1.decode()))
plat = html.Img(src='data:Wordcloud-platform.png;base64,{}'.format(encoded_image2.decode()))

app.layout = html.Div([

    # ________________________________________________________________
    # Headlines

    html.Div([
        html.Img(src='data:test3.png;base64,{}'.format(encoded_image7.decode()),
                 style={"width": "100%"}),

        html.Div([

            html.Img(src='data:test.png;base64,{}'.format(encoded_image5.decode()),
                     style={"width": "50%"}),

            html.Div(de.Lottie(options=options, width="50%", height="50%", url=url))]
            ,
            style={"display": "flex",
                   "flex-direction": "row",
                   "justify-content": "space-evenly",
                   "align-items": "center"
                   }),

    ], style={"background-color": "#e6effe"}),

    # ________________________________________________________________
    # Wordcloud images with call back

    html.Div([

        html.H2("Video Game Questionnaire",
                style={'padding': '20px', 'text-align': 'center',
                       'background-color': 'WhiteSmoke'}),

        html.Label("Choose the Question:",
                   style={'text-align': 'right', "position": "relative",
                          "left": "1080px"}),

        dcc.Dropdown(id='word_dropdown',
                     options=[{'label': "Why do you play?", 'value': "why"},
                              {'label': 'Which systems/consoles do you usually use to play?', "value": "plat"},
                              {'label': "How frequent do you play video games?", 'value': "freq"}],
                     value="why", multi=False, clearable=False,
                     style={"width": "60%", "position": "relative",
                            "left": "440px", "align-items": "center"}),

        html.Div([
            html.Img(src='data:testtt.png;base64,{}'.format(encoded_image4.decode()),
                     style={"width": "50%"}),

            html.Div(id="graph3", children=[]
                     )], style={
            "display": "flex",
            "flex-direction": "row",
            "justify-content": "space-evenly",
            "align-items": "center"
        }),

        dcc.Store(id="store-word", data=[], storage_type="memory")],
        style={
            "border": "0.5px solid Gainsboro"}),
        # ________________________________________________________________
    # Sales analysis

    html.Div([

        html.H2("Sales of xBox vs PlayStation in Different Regions",
                style={'padding': '20px', 'text-align': 'center',
                       'background-color': 'WhiteSmoke'}),

        html.Label("Choose a Region:",
                   style={'text-align': 'center', "position": "relative",
                          "left": "670px"}),

        dcc.Dropdown(id='Region_dropdown',
                     options=[{'label': 'North America', 'value': "fig_NA"},
                              {'label': 'Europe', "value": "fig_EU"},
                              {'label': 'Global', 'value': "fig_GL"}],
                     value="fig_NA", multi=False, clearable=False,
                     style={"width": "60%", "position": "relative",
                            "left": "230px", 'text-align': 'center'})
        ,

        html.Div([
            html.Div(id="graph1", children=[]
                     )]),

        dcc.Store(id="store-data", data=[], storage_type="memory")],
        style={
            "border": "0.5px solid Gainsboro"}),
    # ________________________________________________________________
    # Distribution by genre

    html.Div([

        html.H2("Distribution",
                style={'padding': '20px', 'text-align': 'center',
                       'background-color': 'WhiteSmoke'}),

        html.Div([

            html.Label("The Distribution is Based on:",
                       style={'text-align': 'right', "position": "relative",
                              "left": "960px"}),
            dcc.Dropdown(id='graph_dropdown',
                         options=[{'label': 'Age Groups', "value": "fig_pie"},
                                  {'label': 'Education Level', "value": "fig_degree"},
                                  {'label': 'Professional Level', "value": "fig_work"},
                                  {'label': 'Most used Platform by Genre', 'value': "fig_SB"},
                                  {'label': 'Games by Genre', "value": "fig_M"}],
                         value="fig_pie", multi=False, clearable=False,
                         style={"width": "60%", "position": "relative",
                                "left": "400px", "align-items": "center",
                                }),

            html.Label("Sales and Top Genres",
                       style={'text-align': 'middle', "position": "relative",
                              "left": "330px", "top": "-58px"}),

            dcc.Dropdown(id='chart_dropdown',
                         options=[{'label': 'Sales Over the Years', 'value': "fig_time"},
                                  {'label': 'Top Genres', "value": "fig_BU"}],
                         value="fig_time", multi=False, clearable=False,
                         style={"width": "60%", "position": "relative",
                                "align-items": "center", "left": "75px", "top": "-30px"})]
        ),

        html.Div([
            html.Div(id="graph11", children=[],
                     style={'display': 'inline-block'}),
            html.Div([
                html.Div(id="graph2", children=[],
                         style={'display': 'inline-block'}
                         )]),

            dcc.Store(id="store-dataa", data=[], storage_type="memory")
        ], style={
            "display": "flex",
            "flex-direction": "row",
            "justify-content": "space-evenly",
            "align-items": "center"
        })], style={
        "border": "0.5px solid Gainsboro"}),

    # ________________________________________________________________
    # Tree map with call back

    html.Div([

        html.H2("Customer Analyze by Gender, Satisfaction of Life, and Narcissism",
                style={'padding': '20px', 'text-align': 'center',
                       'background-color': 'WhiteSmoke'}),

        html.Label("Choose a Gender:",
                   style={'text-align': 'center', "position": "relative",
                          "left": "290px"}),

        dcc.Dropdown(id='gender_dropdown',
                     options=[{"label": s, "value": s}
                              for s in sorted(study_na.Gender.unique())],
                     value="Male", multi=False, clearable=False,
                     style={"width": "60%", "position": "relative",
                            "left": "43px", 'text-align': 'center'}),

        html.Label("Age group:",
                   style={'text-align': 'center', "position": "relative",
                          "left": "1090px", "top": "-59px"}),

        dcc.Dropdown(id='age_dropdown',
                     options=[],
                     style={"width": "60%", "position": "relative",
                            "left": "430px", "top": "-30px", 'text-align': 'center'}),

        dcc.Graph(id='display-map', figure={}),
    ],
        style={
            "border": "0.5px solid Gainsboro"}),

    # ________________________________________________________________
    # Hours by country

    html.Div([

        html.H2("Number of Hours Played per Country",
                style={'padding': '20px', 'text-align': 'center',
                       'background-color': 'WhiteSmoke'}),
        html.Label("Choose a Country:",
                   style={'text-align': 'center', "position": "relative"}),
        dcc.Dropdown(iso["Residence_ISO3"].unique(), '', id='country_dropdown',
                     multi=True, clearable=True),
        dcc.Graph(id="8"),

    ],
        style={
            "border": "0.5px solid Gainsboro"}),

    # ________________________________________________________________
    # conclusion

    html.Div([

        html.Img(src='data:final.png;base64,{}'.format(encoded_image3.decode()),
                 style={"width": "100%",
                        'background-color': '#4d81d1'})
    ])

],
    style={
        "border": "2px solid Gainsboro"})


@app.callback(
    Output('graph1', 'children'),
    Input(component_id='Region_dropdown', component_property='value'))
def create_graph1(value):
    if value == "fig_NA":
        return dcc.Graph(figure=fig_NA)

    elif value == "fig_EU":
        return dcc.Graph(figure=fig_EU)

    elif value == "fig_GL":
        return dcc.Graph(figure=fig_GL)


@app.callback(
    Output('graph2', 'children'),
    Input(component_id='graph_dropdown', component_property='value'))
def create_graph2(value):
    if value == "fig_SB":
        return dcc.Graph(figure=fig_SB)

    elif value == "fig_M":
        return dcc.Graph(figure=fig_M)

    elif value == "fig_degree":
        return dcc.Graph(figure=fig_degree)
    elif value == "fig_pie":
        return dcc.Graph(figure=fig_pie)
    elif value == "fig_work":
        return dcc.Graph(figure=fig_work)


@app.callback(
    Output('graph11', 'children'),
    Input(component_id='chart_dropdown', component_property='value'))
def create_graph11(value):
    if value == "fig_BU":
        return dcc.Graph(figure=fig_BU)

    elif value == "fig_time":
        return dcc.Graph(figure=fig_time)


@app.callback(
    Output('graph3', 'children'),
    Input(component_id='word_dropdown', component_property='value'))
def word(value):
    if value == "why":
        return why

    elif value == "plat":
        return plat

    elif value == "freq":
        return freq


@app.callback(
    Output('8', 'figure'),
    Input('country_dropdown', 'value')
)
def update_output(value):
    filter = []
    df_flitered = []
    if (value != '' and value != []):
        filter = [value] if type(value) == str else value
        df_filtered = iso[iso["Residence_ISO3"].isin(filter)]
    else:
        df_filtered = iso

    fig_map = px.choropleth(df_filtered, locations="Residence_ISO3",
                            color="Hours",
                            hover_name="Number of players",
                            color_continuous_scale=px.colors.sequential.Plasma)

    return (fig_map)


@app.callback(
    [
        Output('age_dropdown', 'options'),
        Output('age_dropdown', 'value')
    ],
    Input('gender_dropdown', 'value')
)
def set_genre_options(chosen_state):
    study = study_na[study_na.Gender == chosen_state]
    output_options = [{'label': c, 'value': c} for c in sorted(study.Age.unique())]
    return (output_options, output_options[0]['value'])


@app.callback(
    Output('display-map', 'figure'),
    Input('age_dropdown', 'value'),
    Input('gender_dropdown', 'value')
)
def update_grpah_gender(selected_Age, selected_gender):
    if selected_Age == 0:
        return no_update
    else:
        study = study_na[(study_na.Gender == selected_gender) & (study_na["Age"].eq(selected_Age))]

        fig_Tr2 = px.treemap(study, path=['Age', 'SWL_T'],
                             color='Narcissism',
                             color_continuous_scale='deep')
        fig_Tr2.update_layout(margin=dict(t=50, l=25, r=25, b=25))
        return fig_Tr2


if __name__ == '__main__':
    app.run_server(debug=True, port=8082)
