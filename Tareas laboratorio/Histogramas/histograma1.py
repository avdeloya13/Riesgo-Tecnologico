import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches

# Cargar el archivo CSV
data = pd.read_csv('transacciones.csv')

# Crear una nueva columna combinando 'date' y 'time'
data['transaction_time'] = pd.to_datetime(data['date'] + ' ' + data['time'], format='%d/%m/%Y %H:%M')

# Filtrar para obtener solo transacciones fraudulentas de nuevos usuarios
fraudulent_transactions_new_users = data.loc[(data['status'] == 'fraudulent') & (data['new_user'] == True)].copy()

# Extraer la hora del día de la columna 'transaction_time'
fraudulent_transactions_new_users.loc[:, 'hour'] = fraudulent_transactions_new_users['transaction_time'].dt.hour

# Añadimos un estilo a la gráfica
sns.set(style="whitegrid")

# Se define y se crea la gráfica
plt.figure(figsize=(10, 6))
colors = ["#FF6F61"]

# Crear el histograma con el monto por hora
sns.histplot(
    data=fraudulent_transactions_new_users,
    x='hour', 
    weights='amount',  # Aquí el peso será el monto de la transacción
    bins=24,  # Una barra por cada hora del día
    color=colors[0],
    edgecolor='black'
)

# Títulos y etiquetas
plt.title('Monto de transacciones fraudulentas por hora del día (nuevos usuarios)', fontsize=16, fontweight='bold')
plt.xlabel('Hora del día', fontsize=14)
plt.ylabel('Monto total de transacciones fraudulentas', fontsize=14)

# Personalizamos los ejes
plt.xticks(range(0, 24), fontsize=12)
plt.yticks(fontsize=12)

# Cuadrícula en la gráfica
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Crear la leyenda "Fraudulentas"
fraud_patch = mpatches.Patch(color='#FF6F61', label='Fraudulentas')

# Guardar la gráfica como imagen en lugar de mostrarla
plt.legend(handles=[fraud_patch], title='Estado', loc='upper right', fontsize=12)
plt.tight_layout()

# Guardar la gráfica en un archivo PNG
plt.savefig('IMAGE/histograma1.png')

plt.show()
