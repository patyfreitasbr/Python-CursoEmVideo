txt = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(txt))
print('Só tem espaços? ',txt.isspace())
print('É um número? ',txt.isnumeric())
print('É alfabetico? ',txt.isalpha())
print('É alfanumerico?',txt.isalnum())
print('Está em maiúsculas? ',txt.isupper())
print('Está em minúsculas? ',txt.islower())
print('Está capitalizada? ',txt.capitalize())


