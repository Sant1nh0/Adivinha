import random

print('Digite um número entre 0 e 10:')
n = range(11)
r = random.choice(n)
num = int(r)

tentativa = 0

while True:
    tentativa += 1
    res = input()
    rp = int(res)
    if (rp == num):
        print(f'Parabéns, você acertou! \nNa {tentativa} tentativa!')
        break
    else:
        print(f'Tente novamente!')
