#LARGURA ALTURA E ÁREA
print('=====LÁZARO REFORMAS=====')

alt = float(input('Informe a largura da parede: '))
larg = float(input('Informe a altura da parede: '))
area = alt * larg
tint = area / 2
print('A área total de sua parede equivale a {} M²'.format(area))
print('Serão necessários {} litros de tinta para pintura.'.format(tint))
