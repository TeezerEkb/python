# конвертация секунд




n = int(input("Введите число секунд: "));
  
 

n = n % (24 * 3600)

hour = n // 3600

  

n %= 3600

minutes = n // 60

  

n %= 60

seconds = n

      

print(hour, "часов", 

          minutes, "минут",

          seconds, "секунд")
