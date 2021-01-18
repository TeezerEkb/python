#пробежки
a = int(input("Введите результат первого дня в км "))
b = int(input("Введите желаемый дневной результат в км "))
result_days = 1
result_km = a
while a < b:
        a = a + 0.1 * a
        result_days += 1
        
print(f"Спортсмен достигнет желаемого результата на %.d день" % result_days)
