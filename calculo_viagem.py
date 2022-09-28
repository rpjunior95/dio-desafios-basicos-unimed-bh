entrada = input().split(" ")


delta_tempo = int(entrada[0])
velocidade_media = int(entrada[1])

delta_distancia = delta_tempo * velocidade_media

carro = 12

resultado = delta_distancia / carro

print(f'{resultado:.3f}')