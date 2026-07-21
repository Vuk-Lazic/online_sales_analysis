#PLOTLY

"""
import plotly.express as px
import pandas as pd

df = pd.read_csv("books.csv")

section_counts = df["section"].value_counts().reset_index()                                 #PRAVLJENJE INTERAKTIVNOG DIJAGRAMA
section_counts.columns = ["section", "count"]

fig = px.pie(data_frame=section_counts, names="section", values="count", title="Number of books per section")
fig.show()
"""

"""
import plotly.express as px
import pandas as pd

delivery_types = ['Standard', 'Express', 'Pickup']
orders = [180, 70, 50]

data = pd.DataFrame({ 
    "delivery_type": delivery_types,                                      #PRAVLJERNJE NOVOG DATA FRAME-A I PRAVLJENJE INTERAKTIVNOG DIJAGRAMA
    "order_number": orders
})

fig = px.pie(data_frame=data, names="delivery_type", values="order_number", title="Number of orders by delivery type")
fig.show()
"""

#BOKEH

"""
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource
import pandas as pd

df = pd.read_csv("books.csv")
df["published_century"] = ((df["year_published"] - 1) // 100 + 1).astype("Int64")

avg_rating_by_century = (
    df.groupby("published_century")["rating"].mean().reset_index()
)

output_file("line_chart.html")
 
source = ColumnDataSource(avg_rating_by_century)                                   #PRAVLJENJE BOIKEH INTERAKTIVNOG DIJAGRAMA

p = figure(title="Average Book Rating by Century",
 
           x_axis_label='Century',
 
           y_axis_label='Average rating',
 
           width=1000, height=600, toolbar_location=None)

p.line(x='published_century', y='rating', source=source, line_width=2)
p.circle(x='published_century', y='rating', size=8, source=source, color="navy", alpha=0.6)

show(p)
"""

"""
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool
import pandas as pd
 
df = pd.read_csv("books.csv")
df["published_century"] = ((df["year_published"] - 1) // 100 + 1).astype("Int64")

avg_rating_by_century = (
    df.groupby("published_century")["rating"].mean().reset_index()
)

output_file("line_chart.html")

source = ColumnDataSource(avg_rating_by_century)

p = figure(title="Average Book Rating by Century",
           x_axis_label='Century',
           y_axis_label='Average rating',
           width=1000, height=600,
           tools="pan,wheel_zoom,box_zoom,reset,save")

hover = HoverTool(tooltips=[
    ("Century", "@published_century"),                                              #DODAVANJE ALATKI ZA POKAZIVANJE VREDNOSTI
    ("Average rating", "@rating{0.00}")
])

p.add_tools(hover)
p.line(x='published_century', y='rating', source=source, line_width=2)
p.circle(x='published_century', y='rating', size=8, source=source, color="navy", alpha=0.6)

show(p)
"""

#PLOTLY VS BOKEH

"""
import pandas as pd
import plotly.express as px

df = pd.read_csv("books.csv")
df["published_century"] = ((df["year_published"] - 1) // 100 + 1).astype("Int64")

avg_rating_by_century = (
    df.groupby("published_century")["rating"].mean().reset_index()                      #ISTRAZI JOS PA VIDI KAKO I STA!!!
)

fig = px.line(avg_rating_by_century,
            x="published_century",
            y="rating",
            markers=True,
            title="Average Book Rating by Century",
            labels={"published_century": "Century", "rating": "Average Rating"})

fig.update_traces(hovertemplate='Century: %{x}<br>Avg Rating: %{y:.2f}')

fig.show()
"""

#INTERAKTIVNI HISTOGRAM

"""
import pandas as pd
import plotly.express as px

df_books = pd.read_csv("books.csv")         

fig = px.histogram(                                                             #PRAVLJENJE INTERAKTIVNOG HISTOGRAMA
    data_frame=df_books,
    x="rating",
    color="section",  #DODAVANJE BOJA PO ONOME STA NAVEDEMO
    marginal="box",   #DODAVANJE BOX PLOTOVA IZNAD HISTOGRAMA
    hover_data=["title", "author", "rating", "ratings_count"], #DODAVANJE PODATAKA ZA EKSTREMNE VREDNOSTI U SMISLU NAZIVA ITD...
    title="Distribution of Book Ratings"                                                   
)

fig.update_layout(
    xaxis_title="Rating",
    yaxis_title="Books (No.)",
    xaxis_range=[0, 5],
    bargap=0.1
)

fig.show()
#"""

"""
import pandas as pd
import plotly.express as px

df_books = pd.read_csv("online_store_order_items.csv")         

fig = px.histogram(                                                             #PRIMER PRAVLJENJE INTERAKTIVNOG HISTOGRAMA
    data_frame=df_books,
    x="order_value",
    color="category",
    marginal="box",
    hover_data=["name", "category", "order_value"],
    title="Order Values Distribution Per Category"                                                   
)

fig.update_layout(
    xaxis_title="Order Value (€)",
    yaxis_title="Orders (No.)",
    bargap=0.1
)

fig.show()
#"""

#INTERAKTIVNA KORELACIJA

"""
import pandas as pd
import plotly.express as px

df = pd.read_csv("books.csv")

fig = px.scatter(
    df,
    x="page_count",
    y="rating",
    hover_name="title",  #OVIM DODAJEMO DA NAM SE PRVO POKAZE NASLOV PA SVE OSTALO
    hover_data=["author", "genre", "ratings_count", "year_published", "page_count", "price", "language"],          #KREIRANJE INTERAKTIVNE KORELACIJE
    trendline="lowess",
    title="Rating vs Page Count"
)

fig.show()
"""

"""
import pandas as pd
import plotly.graph_objects as go       #ZA PRAVLJENJE KOMPLEKSNIJIH DIJAGRAMA KORISTIMO OVAJ IMPORT!!!!!!

df = pd.read_csv("books.csv")
fig = go.Figure()

features = ["page_count", "ratings_count", "year_published", "price"]

# hover data
 
hover_text = df.apply(lambda row:
    f"<b>{row['title']}</b><br><br>"
    f"Author: {row['author']}<br>"
    f"Pages: {row['page_count']}<br>"
    f"Price: {row['price']}<br>"
    f"Year: {row['year_published']}<br>"
    f"Ratings count: {row['ratings_count']}", axis=1)

# create trace (plot) for each feature
 
for i, feature in enumerate(features):
    fig.add_trace(go.Scatter(
        x=df[feature],
        y=df["rating"],
        mode="markers",
        hovertext=hover_text,
        hoverinfo="text",
        name=feature,
        visible=(i == 0)  # only first trace will be visible                     #PRAVLJENJE INTERAKTIVNOG DIJAGRAMA SA PADAJUCIM MENIJEM I SA VISE DIJAGRAMA
))

# create buttons

buttons = []

for i, feature in enumerate(features):
    visibility = [j == i for j in range(len(features))]
    buttons.append(dict(
        label=feature,
        method="update",
        args=[
            {"visible": visibility},
            {
                "title": {"text": f"Rating vs {feature}"},
                "xaxis": {"title": {"text": feature}}
            }
        ]
    ))

# add menu and configure
 
fig.update_layout(
    updatemenus=[dict(
        type="dropdown",
        direction="down",
        buttons=buttons,
        x=1.15,
        y=0.9
    )],
    title=f"Rating vs {features[0]}",
    xaxis_title=features[0],
    yaxis_title="Rating",
    showlegend=False
)

fig.show()
"""



































































