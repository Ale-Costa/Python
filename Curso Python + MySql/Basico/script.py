# -*- coding: utf-8 -*-

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
operador = input("Digite o operador: ")

def soma(valor1, valor2):
    return(valor1+valor2)

res_soma = soma
if operador == "+":
    print("A soma dos valores é: ")
    print(res_soma)