
# uso padrão
print("Se inscreve no canal")

inscritos = 500000
print("Temos mais de", inscritos, "inscritos")

# formatando
inscritos = 500000
print(f"Temos mais de {inscritos:,} inscritos")

# separador
faturamento = 10000
custo = 6000
print("Faturamento", faturamento, sep=":")
print("Custo", custo, sep=":")
print("Lucro", faturamento - custo, sep=":\n")

# end
faturamento = 10000
custo = 6000
print("Faturamento:", faturamento, end="; ")
print("Custo:", custo, end="; ")
print("Lucro", faturamento - custo)

# cronometro
import time

print("10", end="\r")
time.sleep(1)
print("09", end="\r")
time.sleep(1)
print("08", end="\r")
time.sleep(1)
print("07", end="\r")
time.sleep(1)
print("06", end="\r")