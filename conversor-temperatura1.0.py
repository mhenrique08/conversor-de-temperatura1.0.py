#Conversor de temperatura #1

#[=========================================================================================================================]

#Título/Opções/Entrada de Dados
while True:
 print ("[", "="*30, "CONVERSOR DE TEMPERATURA" ,"="*30, "]")
 print ("1) Celsius para Fahrenheit.")
 print ("2) Celsius para Kelvin.")
 print ("3) Fahrenheit para Kelvin.")
 print ("4) Fahrenheit para Celsius.")
 print ("5) Kelvin para Fahrenheit.")
 print ("6) Kelvin para Celsius.")
 print ("SAÍDA) Para sair digite 'sair'. ")
 print ()
 conversao = input("Insira qual conversão você deseja fazer (1/2/3/4/5/6):   ")
#[=========================================================================================================================]

#Condicionais/ Sistema de desligamento
 if conversao == 'sair':
  print ("Encerrando conversor...")
  break
 
 elif conversao == '1':
  num_celsius = float(input("Insira a temperatura em C°:  "))
  resultado = (((num_celsius*9)/5)+32)
  print (" - O resultado é:", resultado, "°F")

 elif conversao == '2':
  num_celsius = float(input("Insira a temperatura em C°:  "))
  resultado = (num_celsius+273.15)
  print (" - O resultado é:", resultado, "K")
  if resultado == 0:
   print (" - O resultado é:", resultado, "K")
   print ("Parabéns! Você encontrou o zero absoluto!")

 elif conversao == '3':
  num_fahrenheit = float(input("Insira a temperatura em °F:  "))
  resultado =((((num_fahrenheit*5)+2297)/9)+0.15)
  print (" - O resultado é:", resultado, "K")

 elif conversao == '4':
  num_fahrenheit = float(input("Insira a temperatura em °F:  "))
  resultado = (((num_fahrenheit*5)-160)/9)
  print (" - O resultado é:", resultado, "C°")

 elif conversao == '5':
  num_kelvin = float(input("Insira a temperatura em K:  "))
  resultado = ((((num_kelvin-0.15)*9)-2297)/5)
  if num_kelvin == 0:
   print (" - O resultado é:", resultado, "°F")
   print ("Parabéns! Você encontrou o zero absoluto!")
  elif num_kelvin <0:
   print ("Temperatura em K não possuem valores negativos.")
   continue
  else:
   print (" - O resultado é:", resultado, "°F")

 elif conversao == '6':
  num_kelvin = float(input("Insira a temperatura em K:  "))
  resultado = (num_kelvin-273.15)
  if num_kelvin == 0:
   print (" - O resultado é:", resultado, "°C")
   print ("Parabéns! Você encontrou o zero absoluto!")
  else:
   print (" - O resultado é:", resultado, "C°")

 else:
  print ("Insira um comando válido. ")
  
#[=========================================================================================================================]
