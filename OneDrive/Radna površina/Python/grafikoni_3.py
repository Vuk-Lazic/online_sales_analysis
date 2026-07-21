#KUTIJASTI DIJAGRAM

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("online_store_order_items.csv")
 
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="order_value")                                 #PRAVLJENJE KTIJASTOG DIJAGRAMA
 
plt.title("Order Value Distribution")
plt.xlabel("Order Value (€)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
"""

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("online_store_order_items.csv")
 
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="order_value", y="category")
 
plt.title("Order Values Distribution Per Category")                                              #KUTIJASTI DIJAGRAM SA X I Y OSOM
plt.xlabel("Order Value (€)")
plt.ylabel("Category")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

#Electronics i Home su bez premca!:
#Troši se ozbiljno – velike vrednosti porudžbina i šarenilo cena koje šeta gore-dole kao skakači na trampolini.

#Stabilna ekipa:
#Books, Clothing i Toys se drže kao uzorni školarci.
#Njihove cene su mnogo ujednačenije – bez velikih skokova.
#Savršeni za one koji vole miran šoping bez iznenadnih kreditnih poziva!
"""

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("systolic_bp_by_age.csv")
 
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="age_group", y="systolic_bp", hue="age_group", palette="pastel")             #KUTIJASTI DIJAGRAM SA X I Y OSOM
 
plt.title("Distribution of Systolic Blood Pressure by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Systolic Blood Pressure (mmHg)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
"""

#TACKASTI DIJAGRAM

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("student_performance_data.csv")
 
sns.scatterplot(data=df, x="study_hours", y="grade")                          #KREIRANJE TACKASTOG DIJAGRAMA
 
plt.title("Relationship Between Study Hours and Grade")
plt.xlabel("Study hours")
plt.ylabel("Grade")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
"""

##LINEARNE KORELACIJE

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("student_performance_data.csv")
 
sns.regplot(data=df, x="study_hours", y="grade", line_kws={"color": "green"})                        #KREIRANJE LINIJE TRENDA U TACKASTOM DIJAGRAMU
 
plt.title("Relationship Between Study Hours and Grade")                                              #POZITIVNA KORELACIJA
plt.xlabel("Study hours")
plt.ylabel("Grade")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
#plt.ylim(0, 100)
plt.show()
"""

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("health_data.csv")
 
sns.regplot(data=df, x="age", y="blood_pressure", line_kws={"color": "green"})                    #PRIMER POZITIVNE KORELACIJE
 
plt.title("Relationship Between Age and Blood pressure")
plt.xlabel("age")
plt.ylabel("Blood pressure")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
"""

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("student_performance_data.csv")
sns.regplot(data=df, x="missed_classes", y="grade", line_kws={"color": "green"})                #PRIMER NEGATIVNE KORELACIJE
plt.title("Relationship Between Missed Classes and Grade")
plt.xlabel("Missed Classes")
plt.ylabel("Grade")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
"""

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("student_performance_data.csv")
sns.regplot(data=df, x="shoe_size", y="grade", line_kws={"color": "gray"})                       #PRIMER BEZ KORELACIJE
plt.title("Relationship Between Shoe Size and Grade")
plt.xlabel("Shoe Size")
plt.ylabel("Grade")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
"""

#NELINEARNE KORELACIJE

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("student_performance_data.csv")
sns.regplot(data=df, x="sleep_hours", y="grade", lowess=True, line_kws={"color": "purple"})       #PRIMER NELINEARNE KORELACIJE
plt.title("Relationship Between Sleep Hours and Grade")
plt.xlabel("Sleep Hours")
plt.ylabel("Grade")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
"""

#VISE DIJAGRAMA U JENDOM GRAFIKONU

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("student_performance_data.csv")
 
fig, axs = plt.subplots(2, 2, figsize=(14, 7))
 
# Scatter plot: study_hours vs grade
sns.regplot(data=df, x="study_hours", y="grade", line_kws={"color": "green"}, lowess=True, ax=axs[0, 0])
axs[0, 0].set_title("Study Hours vs Grade")
 
# Scatter plot: missed classes vs grade
sns.regplot(data=df, x="missed_classes", y="grade", line_kws={"color": "green"}, lowess=True, ax=axs[0, 1])     #PRAVLJENJE VISE GRAFIKONA ZAJEDNO
axs[0, 1].set_title("Missed Classes vs Grade")
 
# Scatter plot: sleep_hours vs grade
sns.regplot(data=df, x="sleep_hours", y="grade", line_kws={"color": "green"}, lowess=True, ax=axs[1, 0])
axs[1, 0].set_title("Sleep Hours vs Grade")
 
# Scatter plot: shoe_size vs grade
sns.regplot(data=df, x="shoe_size", y="grade", line_kws={"color": "green"}, lowess=True, ax=axs[1, 1])
axs[1, 1].set_title("Shoe Size vs Grade")
 
plt.suptitle("Relationships Between Student Characteristics and Grade", fontsize=16)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
"""

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("health_data.csv")
 
features = ['age', 'height', 'weight', 'bmi', 'daily_steps', 'sleep_hours', 'alcohol_units', 'exercise_minutes']
 
fig, axs = plt.subplots(2, 4, figsize=(20, 10))
axs = axs.flatten()
 
for i, feature in enumerate(features):
    sns.regplot(data=df, x=feature, y='blood_pressure', ax=axs[i], scatter_kws={'alpha': 0.6}, line_kws={'color': 'red'}, lowess=True)    #PRIMER PRAVLJENJA VISE TABELA
    axs[i].set_title(f"Blood Pressure vs {feature}")
    axs[i].grid(True, linestyle='--', alpha=0.4)
 
plt.suptitle("How Patient Characteristics Affect Blood Pressure", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
"""

#TOPLOTNA MAPA

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("student_performance_data.csv")                                     #PRAVLJENJE TOPLOTNE MAPE
 
corr_matrix = df.corr()
 
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap of Student Performance Data")
plt.tight_layout()
plt.show()
"""

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("health_data.csv")
 
corr_matrix = df.corr()                                                                #PRIMER TOPLOTNE MAPE
 
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap of Health Data")
plt.tight_layout()
plt.show()
"""