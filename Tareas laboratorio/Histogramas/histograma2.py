import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches

# Cargar el CSV
data = pd.read_csv('transacciones.csv')

# Filtra para obtener solo transacciones fraudulentas
fraudulent_transactions = data[data['status'] == 'fraudulent']

# Formato para extraer la informacion para las columnas de los usuarios no nuevos y nuevos
fraudulent_transactions_users = fraudulent_transactions[
    (fraudulent_transactions['new_user'] == True) | 
    (fraudulent_transactions['new_user'] == False)
]

# Se añade un estilo a la gráfica
sns.set(style="whitegrid")

# Se define y se crea la gráfica
plt.figure(figsize=(10, 6)) 
colors = ["#73a13f", "#73a13f"]

# Personalizamos las barras
sns.histplot(
    data=fraudulent_transactions_users, 
    x='new_user', 
    hue='new_user',  
    multiple='stack', 
    palette=colors,
    shrink=7.5,  
    edgecolor='black'  
)

# Titulos
plt.title('Cantidad de transacciones fraudulentas por tipo de usuario', fontsize=16, fontweight='bold')
plt.xlabel('Tipo de usuario', fontsize=14)
plt.ylabel('Cantidad de transacciones fraudulentas', fontsize=14)

# Perzonalizamos los ejes
plt.xticks([0, 1], ['Non New', 'New'], fontsize=12) 
plt.yticks(fontsize=12)

# Cuadrícula en la gráfica 
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Crear la leyenda "Fraudulentas" de Estado
new_patch = mpatches.Patch(color='#73a13f', label='Fraudulentas')

# Muestra la gráfica
plt.legend(handles=[new_patch], title='Estado', loc='upper right', fontsize=12)
plt.tight_layout()
plt.show()
