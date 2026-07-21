#HISTOGRAM

"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
df = pd.read_csv("online_store_data.csv")
 
plt.figure(figsize=(10, 5))
sns.histplot(df["price"], bins='auto', color="skyblue", edgecolor="black")           #KREIRANJE HISTOGRAMA
 
plt.title("Distribution of Product Prices")
plt.xlabel("Price ($)")
plt.ylabel("Number of Products")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
"""

"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
df = pd.read_csv("call_durations.csv")
 
plt.figure(figsize=(10, 5))
sns.histplot(df["call_duration_min"], bins=15, kde=True, color="skyblue", edgecolor="black")       #PRIMER PRAVLJENJA HISTOGRAMA SA KDE-OM
plt.title("Distribution of Call Durations") 
plt.xlabel("Call Duration (min)")
plt.ylabel("Number of Calls")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
#"""

"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
df = pd.read_csv("online_store_data.csv")
 
plt.figure(figsize=(10, 5))
sns.histplot(df["price"], bins=15, kde=True, color="skyblue", edgecolor="black")         #PRIMER HISTOGRAMA SA KDE KRIVOM
 
plt.title("Distribution of Product Prices with KDE Curve")
plt.xlabel("Price ($)")
plt.ylabel("Number of Products")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
"""

"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
df = pd.read_csv("online_store_data.csv")
 
plt.figure(figsize=(10, 5))
sns.kdeplot(df["price"], fill=True, color="skyblue")                       #PRAVLJENJE HISTOGRAMA BEZ STUBICA SAMO SA KDE-OM
 
plt.title("Smoothed Distribution of Product Prices (KDE Only)")
plt.xlabel("Price ($)")
plt.ylabel("Density")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
"""

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("product_ratings.csv")
 
plt.figure(figsize=(10, 5))
sns.kdeplot(df["user_rating_percent"], fill=True, color="green")
plt.title("KDE Curve of User Ratings")
plt.xlabel("User Rating (%)")
plt.ylabel("Density")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
"""

#TUMACENJE KDE GRAFIKONA

##NORMALNA RASPODELA

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
def plot_distribution(df, column, title=None, xlabel=None):
    plt.figure(figsize=(10, 5))
    sns.kdeplot(df[column], fill=True, color="skyblue")
    plt.title(title or f"Distribution of {column}")                                       #PRIMER PRAVLJENJA FUNKCIJE ZA PRAVELNJE GRAFIKONA
    plt.xlabel(xlabel or column)
    plt.ylabel("Count")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()

df = pd.read_csv("human_behavior_patterns.csv")
 
plot_distribution(df, "height_cm", title="Height Distribution", xlabel="Height (cm)")                      #PRIMER NORMALNE RASPODELE
"""
 
##LEVO ASIMETRICNA RASPODELA

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
def plot_distribution(df, column, title=None, xlabel=None):
    plt.figure(figsize=(10, 5))
    sns.kdeplot(df[column], fill=True, color="skyblue")
    plt.title(title or f"Distribution of {column}")
    plt.xlabel(xlabel or column)
    plt.ylabel("Count")
    plt.grid(True, linestyle="--", alpha=0.5)                                                       #PRIMER LEVO ASIMETRICNE RASPODELE
    plt.tight_layout()
    plt.show()

df = pd.read_csv("human_behavior_patterns.csv")

plot_distribution(df, "grade_percent", title="Test Grade Distribution", xlabel="Grade (%)")
"""

##DESNO ASIMETRICNA RASPODELA

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
def plot_distribution(df, column, title=None, xlabel=None):
    plt.figure(figsize=(10, 5))
    sns.kdeplot(df[column], fill=True, color="skyblue")
    plt.title(title or f"Distribution of {column}")
    plt.xlabel(xlabel or column)
    plt.ylabel("Count")
    plt.grid(True, linestyle="--", alpha=0.5)                                                       #PRIMER DESNO ASIMETRICNE RASPODELE
    plt.tight_layout()
    plt.show()

df = pd.read_csv("human_behavior_patterns.csv")

plot_distribution(df, "household_income", title="Househol Income", xlabel="Income (E)")
"""

##UNIFORMNA RASPODELA

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
def plot_distribution(df, column, title=None, xlabel=None):
    plt.figure(figsize=(10, 5))
    sns.kdeplot(df[column], fill=True, color="skyblue")
    plt.title(title or f"Distribution of {column}")
    plt.xlabel(xlabel or column)
    plt.ylabel("Count")
    plt.grid(True, linestyle="--", alpha=0.5)                                                       #PRIMER UNIFORMNE RASPODELE
    plt.tight_layout()
    plt.show()

df = pd.read_csv("human_behavior_patterns.csv")

plot_distribution(df, "coffee_hour", title="First Coffee of the Day", xlabel="Hour")
"""

##BIMODALNA RASPODELA

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
def plot_distribution(df, column, title=None, xlabel=None):
    plt.figure(figsize=(10, 5))
    sns.kdeplot(df[column], fill=True, color="skyblue")
    plt.title(title or f"Distribution of {column}")
    plt.xlabel(xlabel or column)
    plt.ylabel("Count")
    plt.grid(True, linestyle="--", alpha=0.5)                                                       #PRIMER BIMODALNE RASPODELE
    plt.tight_layout()
    plt.show()

df = pd.read_csv("human_behavior_patterns.csv")

plot_distribution(df, "store_visit_hour", title="Store Visit Times", xlabel="Hour")
"""

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("ecommerce_order_values.csv")
 
plt.figure(figsize=(10, 5))
sns.histplot(df["order_value"], kde=True, bins=30, color="skyblue", edgecolor="black")           #PRIMER NALAZENJA RASPODELE PODATAKA
plt.title("Distribution of Order Values in Online Store")                                        #DESNO ASIMETRICNA RASPODELA
plt.xlabel("Order Value (€)")
plt.ylabel("Number of Orders")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
"""