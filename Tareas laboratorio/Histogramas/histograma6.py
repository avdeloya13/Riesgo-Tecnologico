import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches

# Cargar el archivo CSV
data = pd.read_csv('transacciones.csv')

# Crear una nueva columna combinando 'date' y 'time'
data['transaction_time'] = pd.to_datetime(data['date'] + ' ' + data['time'], format='%d/%m/%Y %H:%M')

# Filtrar transacciones fraudulentas de tipo purchase
fraudulent_purchase_transactions = data.loc[(data['status'] == 'fraudulent') & 
                                            (data['transaction_type'] == 'purchase')].copy()

# Extraer el mes de la columna 'transaction_time'
fraudulent_purchase_transactions['month'] = fraudulent_purchase_transactions['transaction_time'].dt.month

# Añadimos un estilo a la gráfica
sns.set(style="whitegrid")

# Se define y se crea la gráfica
plt.figure(figsize=(10, 6))
colors = ["#FF6F61"]

# Crear el histograma con el monto por mes
sns.histplot(
    data=fraudulent_purchase_transactions,
    x='month', 
    weights='amount',  # Aquí el peso será el monto de la transacción
    bins=12,  # Una barra por cada mes
    color=colors[0],
    edgecolor='black'
)

# Títulos y etiquetas
plt.title('Monto perdido por mes en transacciones "purchase" fraudulentas', fontsize=16, fontweight='bold')
plt.xlabel('Mes del año', fontsize=14)
plt.ylabel('Monto total de transacciones fraudulentas', fontsize=14)

# Personalizamos los ejes
plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'], fontsize=12)
plt.yticks(fontsize=12)

# Cuadrícula en la gráfica
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Crear la leyenda "Fraudulentas"
fraud_patch = mpatches.Patch(color='#FF6F61', label='Fraudulentas')

# Guardar la gráfica como imagen en lugar de mostrarla
plt.legend(handles=[fraud_patch], title='Estado', loc='upper right', fontsize=12)
plt.tight_layout()

# Guardar la gráfica en un archivo PNG
plt.savefig('IMAGE/histograma6.png')

plt.show()
