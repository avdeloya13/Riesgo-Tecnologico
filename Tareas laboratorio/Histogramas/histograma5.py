import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos desde el archivo CSV
data = pd.read_csv('transacciones.csv')

# Filtrar para obtener solo transacciones fraudulentas
fraudulent_transactions = data[(data['status'] == 'fraudulent')]

# Formato para extraer solo el mes de la columna 'date'
fraudulent_transactions['month'] = pd.to_datetime(fraudulent_transactions['date'], format='%d/%m/%Y').dt.month

# Crear una lista de nombres de los meses
months_names = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

# Se define y se crea la gráfica con pesos
plt.figure(figsize=(12, 6))  # Ajusta el tamaño de la figura
sns.histplot(
    data=fraudulent_transactions, x='month', weights='amount', bins=12, kde=True, color='red', label='fraudulent')

# Cambiar las etiquetas del eje X a los nombres de los meses
plt.xticks(ticks=range(1, 13), labels=months_names)

# Títulos
plt.title('Distribución del monto de transacciones fraudulentas por mes del año')
plt.xlabel('Mes del año')
plt.ylabel('Monto')
plt.grid(True)

# Mostramos la gráfica
plt.legend()
plt.show()


