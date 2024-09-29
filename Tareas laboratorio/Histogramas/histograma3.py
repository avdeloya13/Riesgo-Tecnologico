import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches

# Cargar el CSV
data = pd.read_csv('transacciones.csv')

# Filtrar para obtener solo transacciones fraudulentas
fraudulent_transactions = data[data['status'] == 'fraudulent']

# Formato para extraer solo la compra y transfrencia de la columna 'purchase' y 'transfer'
fraudulent_transactions_filtered = fraudulent_transactions[
    (fraudulent_transactions['transaction_type'] == 'purchase') | 
    (fraudulent_transactions['transaction_type'] == 'transfer')
]

# Añadimos un estilo a la gráfica
sns.set(style="whitegrid")

#Se define y se crea la gráfica
plt.figure(figsize=(10, 6)) 
colors = ["#FF6F61", "#6B5B95"]

# Personalizamos las barras
sns.histplot(
    data=fraudulent_transactions_filtered, 
    x='transaction_type', 
    hue='status', 
    multiple='stack', 
    palette=colors,
    shrink=0.8,  
    edgecolor='black'  
)

#Titulos
plt.title('Cantidad de transacciones fraudulentas por tipo de transacción', fontsize=16, fontweight='bold')
plt.xlabel('Tipo de transacción', fontsize=14)
plt.ylabel('Cantidad de transacciones fraudulentas', fontsize=14)

# Perzonalizamos los ejes
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Cuadrícula en la gráfica 
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Crear la leyenda "Fraudulentas"
fraud_patch = mpatches.Patch(color='#FF6F61', label='Fraudulentas')

#Mostramos la gráfica
plt.legend(handles=[fraud_patch], title='Estado', loc='upper right', fontsize=12)
plt.tight_layout()
plt.show()