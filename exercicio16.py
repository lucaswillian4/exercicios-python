salario = int(input("qual o seu salario"))
aumento = int(input("qual o seu aumento"))
novo_aumento = salario+(salario*aumento)/100
novo_salario = salario+novo_aumento

print (f"seu novo salario é {novo_salario} e seu novo aumento é {novo_aumento}")