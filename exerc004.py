# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

inputAleatorio = input("Digite qualquer coisa:")

print("type: {} ".format(type(inputAleatorio)))
print("isalnum: {} ".format(inputAleatorio.isalnum()))
print("isAlpha: {} ".format(inputAleatorio.isalpha()))
print("isAscii: {} ".format(inputAleatorio.isascii()))
print("isDecimal: {} ".format(inputAleatorio.isdecimal()))
print("isDigit: {} ".format(inputAleatorio.isdigit()))
print("isIdentifier: {} ".format(inputAleatorio.isidentifier()))
print("isSlower: {} ".format(inputAleatorio.islower()))
print("isNumeric: {} ".format(inputAleatorio.isnumeric()))
print("isPrintable: {} ".format(inputAleatorio.isprintable()))
print("isspace: {} ".format(inputAleatorio.isspace()))
print("istitle: {} ".format(inputAleatorio.istitle()))
print("isupper: {} ".format(inputAleatorio.isupper()))
