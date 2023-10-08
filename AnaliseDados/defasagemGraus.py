
#Calcualr a defasagem em graus de um filtro passa faixa
deltaT = [18, 17.2, 15.6, 12.8, 8.8, 
          6.8, 4.8, 3.4, 1.2, 2.4, 6.6, 8.8, 10.4, 11.6]

periodo = [95.24, 90.91, 86.96, 
           83.33, 80, 78.74, 77.52, 76.92, 75.76, 74.07, 
           71.43, 68.965, 66.67, 64.52]

for i in range(len(deltaT)):
    defasagem = (deltaT[i]/periodo[i]) * 360
    print(f"{defasagem:.2f}")