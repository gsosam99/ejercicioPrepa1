saldo_inicial = 3480

print(f"Saldo actual a la fecha (2020/04/10): ${saldo_inicial}.\n")

#restar $96 por compra de ropa
saldo_restante = saldo_inicial - 96
print("Se han retirado $96.")
print(f"Saldo actual a la fecha (2020/04/11): ${saldo_restante}.\n")


#sumar $1200 de salario
saldo_restante += 1200
print("Se ha recibido un depósito de $1200.")
print(f"Saldo actual a la fecha (2020/04/17): ${saldo_restante}.\n")


#sumar 3% de intereses
saldo_restante += saldo_restante*0.03
print("Ha recibido su 3% de intereses mensual.")
print(f"Saldo actual a la fecha (2020/04/30): ${saldo_restante}.\n")


#restar $51 por mercado
saldo_restante -= 51
print("Se han retirado $51.")
print(f"Saldo actual a la fecha (2020/05/02): ${saldo_restante}.")
