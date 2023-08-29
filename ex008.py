#Leitura de metros em centímetros e milímetros.

metro = float(input('Digite o valor em metros:'))
print('=====EXECUTANDO=====')
cent = metro * 100
mili = metro * 1000
print('{} metros equivale a {} centímetros e {} milímetros'.format(metro, cent, mili))
