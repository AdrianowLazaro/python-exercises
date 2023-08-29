# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela.

var = input('Digite algo para mim: ')
print('O tipo primitivo desse valor é:',type(var))
print('So tem espaços? ', var.isspace())
print('É um número? ',var.isnumeric())
print('É alfabetico?', var.isalpha())
print('É alfanúmerico?', var.isalnum())
print('Está em letras maiúsculas?', var.isupper())
print('Está em letras minúsculas?', var.islower())
print('Está capitalizada ?', var.istitle())

