salary = 5000  # зарплата в месяц
spend = 6000  # расходы в месяц
increase = 0.03  # рост цен 3%
months = 10  # количество месяцев
money_capital = 0  # начальная подушка безопасности
current_spend = spend  # текущие расходы
for month in range(months):
    if month > 0:
        current_spend = current_spend * (1 + increase) # увеличиваем расходы каждый месяц, кроме первого
    if current_spend > salary:
        money_capital = money_capital + (current_spend - salary) # если расходы больше зарплаты, то разницу добавляем к подушке
money_capital = round(money_capital) # округляем результат
print("Подушка безопасности, чтобы протянуть 10 месяцев без долгов:", money_capital) # выводим на печать

