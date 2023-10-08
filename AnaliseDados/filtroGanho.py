import math

#Calcular ganho em dB de um filtro passa faixa
vgEntrada = 5.2
vLCSaida = [0.42, 0.48, 0.6, 0.78, 0.98, 1.06, 1.16, 
            1.18, 1.22, 1.24, 1.06, 0.84, 0.68, 0.6 
    ]
ganho = 0
for i in range(len(vLCSaida)):
    ganho = 20 * math.log10(vLCSaida[i]/vgEntrada)
    print(f"{ganho:.2f}", end=" ")
