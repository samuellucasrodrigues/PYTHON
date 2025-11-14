pesos=float(input('What do you have left in pesos? '))
soles=float(input('What do you have left in soles? '))
reais=float(input('What do you have left in reais? '))

usd = (pesos * 0.00027) + (soles * 0.3) + (reais * 0.19)
print(usd)