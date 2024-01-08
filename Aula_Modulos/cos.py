import math

# valor do angulo
angulo = float(input('digite o valor do ângulo:'))

#converta sa desgraça 
angulo_rad = math.radians (angulo)

# 123, 321 todo mundo sobre 2 raiz em cada um....
seno = math.sin (angulo_rad)
cosseno = math.cos (angulo_rad)
tangente = math.tan (angulo_rad)

print(f'seno:{seno:.4f} \ncosseno: {cosseno:.4f} \ntangente: {math.ceil(tangente)}')
