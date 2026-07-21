#LINIJSKI GRAFIKON
##MATPLOTLIB

"""
import matplotlib.pyplot as plt
 
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']          #PRAVLJENJE LINIJSKOG GRAFIKONA
rentals = [34, 45, 50, 47, 60, 75, 38]
 
plt.plot(days, rentals)
plt.show()
"""

"""
import matplotlib.pyplot as plt
 
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']           #PRIMER PRAVLJENJA LINIJSKOG DIJAGARAMA
internet_usage = [3.2, 3.5, 4.1, 4.8, 5.3, 6.9, 6.1]
 
plt.plot(days, internet_usage)
plt.show()
"""

"""
import matplotlib.pyplot as plt
 
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
rentals = [34, 45, 50, 47, 60, 75, 38]
 
plt.figure(figsize=(10, 5)) #PODESAVANJE SIRINE I VISINE U INCIMA
plt.plot(days, rentals, marker='o', color='green')                                              #DODAVANJA STVARI NA LINIJSKI GRAFIK
#MARKER OZNACAVA PRIKAZ VREDNOSTI PODATAKA
plt.title("Book Rentals Throughout the Week")
plt.xlabel("Day")
plt.ylabel("Number of Books Rented")
plt.grid(True) #PRIKAZIVANJE MREZE U POZADINI GRAFIKONA, RADI BOLJE CITLJIVOSTI
plt.tight_layout() #RASPORED ELEMENATA BEZ PREKLAPANJA
plt.show()
"""

"""
import matplotlib.pyplot as plt
 
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
internet_usage = [3.2, 3.5, 4.1, 4.8, 5.3, 6.9, 6.1]
 
plt.plot(days, internet_usage, marker='o', color='purple')
 
plt.title("Internet usage by day")                                #PRIMER PRAVLJENJA LINIJSKOG GRAFIKONA
plt.xlabel("Day")
plt.ylabel("Internet usage in GB")
plt.grid(True)
plt.tight_layout()
plt.show()
"""

##SEABORN

"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
 
df = pd.DataFrame({
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Rentals': [34, 45, 50, 47, 60, 75, 38]
})
 
 
plt.figure(figsize=(10, 5))
 
 
sns.set_style(style="whitegrid")
sns.lineplot(data=df, x='Day', y='Rentals', marker='o', color='green')       #PRAVLJENJE GRAFIKONA UZ POMOC SEABORNA
 
 
plt.title("Book Rentals Throughout the Week")
plt.xlabel("Day")
plt.ylabel("Number of Books Rented")
plt.tight_layout()
plt.show()
"""

#KRUZNI DIJAGRAM (PIE CHART)

"""
import matplotlib.pyplot as plt
 
categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Toys']
orders = [120, 90, 60, 80, 50]
 
plt.figure(figsize=(6, 6))                                              #PRAVLJENJE KRUZNIG DIJAGRAMA
plt.pie(orders, labels=categories, autopct='%1.1f%%', startangle=90)
plt.title("Share of Orders by Product Category")
plt.show()
"""

"""
import matplotlib.pyplot as plt
 
 
delivery_types = ['Standard', 'Express', 'Pickup']                           #PRIMER PRAVLJENJA KRUZNOG DIJAGRAMA
orders = [180, 70, 50]
 
 
plt.figure(figsize=(6, 6))
plt.pie(orders, labels=delivery_types, autopct='%1.1f%%', startangle=90)
plt.title("Distribution of Orders by Delivery Type")
plt.show()
"""

"""
import matplotlib.pyplot as plt
import pandas as pd
 
df = pd.read_csv("books.csv")
 
section_counts = df["section"].value_counts()
labels = section_counts.index                                     #PRAVLJENJE KRUZNOG DIJAGRAMA IZVLACENJEM IZ DATAFREJMA
sizes = section_counts.values
 
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Books per Section")
plt.show()
"""

#STUBICASTI DIJAGRAM

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("books.csv")
 
section_counts = df.groupby("section").agg(
    count=("section", "count")).reset_index().sort_values(by="count", ascending=False)               #PRAVLJENJE STIBICASTOG DIJAGRAMA
 
plt.figure(figsize=(8, 6))
sns.barplot(data=section_counts, x="count", y="section", hue="section", palette="pastel", legend=True)
 
plt.title("Books per section")
plt.xlabel("Number of books")
plt.ylabel("Section")
plt.tight_layout()
plt.show()
"""

"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
df = pd.read_csv("online_orders.csv")
 
category_counts = df.groupby("product_category").agg(
    count=("product_category", "count")
).reset_index().sort_values(by="count", ascending=False)                                    #PRIMER PRAVLJENJA STUBICASTOG DIJAGRAMA
 
plt.figure(figsize=(10, 6))
sns.barplot(data=category_counts, x="count", y="product_category", color="skyblue")
 
plt.title("Number of Orders per Product Category")
plt.xlabel("Number of Orders")
plt.ylabel("Product Category")
plt.show()
"""

#CUVANJE DIJAGRAMA

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("books.csv")
 
section_counts = df.groupby("section").agg(
    count=("section", "count")).reset_index().sort_values(by="count", ascending=False)                  #CUVANJE GRAFIKONA
 
plt.figure(figsize=(10, 6))
sns.barplot(data=section_counts, x="section", y="count", hue="section", palette="pastel", legend=True)
 
plt.title("Books per section")
plt.xlabel("Number of books")
plt.ylabel("Section")
 
plt.savefig("books_per_section.png")
plt.savefig("books_per_section.pdf")
plt.savefig("books_per_section.svg")                                                           #EKSPORTOVANJE U RAZLICITIM FORMATIMA
plt.savefig("books_per_section.eps")
plt.savefig("books_per_section.jpg")
"""

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("ecommerce_orders_may.csv")
 
df_completed = df[df["status"] == "Completed"]
 
df_completed["total"] = df_completed["quantity"] * df_completed["price"]
 
category_totals = df_completed.groupby("category", as_index=False)["total"].sum()                      #PRIMER CUVANJA GRAFIKONA
category_totals = category_totals.sort_values(by="total", ascending=False)
 
plt.figure(figsize=(10, 7))
sns.barplot(data=category_totals, x="category", y="total", hue="category", palette="Blues")
 
plt.title("Total Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("total_revenue_by_category.png")
"""




















































