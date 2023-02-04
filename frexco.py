# Dados de vendas
sales_data = [1692, 1097, 1302, 1405, 945]

# Cálculo da média
average_sales = sum(sales_data) / len(sales_data)

# Previsão de demanda para os próximos 5 dias
forecasted_demand = [average_sales for i in range(5)]

# Exibição da previsão de demanda
print("Previsão de demanda para os próximos 5 dias: ", forecasted_demand)
