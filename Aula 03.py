"""
CONDICIONAIS
1) if (se)
2) else (então)
3) elif (else + if) (senão)
"""

#Exemplo

# informacao_usuario= str(input('Você deseja "Entrar" ou "Sair" do programa ?'))
# if informacao_usuario =="Entrar" :
#     print("Sistema acessado com sucesso!")
# else:
#     print("Você não acessou o sistema!")

# entrada_usuario = str(input('Digite "E" para entrar ou "S" para sair:'))
# if entrada_usuario == "E":
#     print("Bem vindo ao sistema!")
# elif entrada_usuario == "S":
#     print("Você saiu do sistema")
# else:
#     print('Você não digitou nem "E" ne "S".')

"""
Operadores Relacionais (de comparação)
1) Igual: ==
2) Maior: >
3) Menor: <
4) Maior ou igual: >=
5) Menor ou igual: <=
6) Diferente: !=
# """
#
# #Igual
#
# igual = "a" == "a"
# print(igual)
# maior = 2> 1
# print(maior)
#
# #Diferente
#
# diferente = 1 !="1"
# print(diferente)

"""
# Operadores Lógicos
# e (and)
# X(True) and Y(False)= False
# X(False) and (True) = False
# X(False) and (False) = True
# X(True) and Y(True)=True
# 
# ou (or)
# 
# X(True)or(False)= True
# X(False or(True) = True
# X(True) or Y(True)=True
# X(False) or (False) =False
# 
# Negação (Not)
# 
# X (True) not X =False
# X (False) not X = True
# 
# """
#
# #and
# x = True
# y = True
# resultado= x and y
# print(resultado)
#
# #or
# x= False
# y=False
# # resultado= x or y
# # print(resultado)
# #1-
# temp_celsius = int(input("Digite a temperatura em C°"))
# transformação = (temp_celsius * (9/5)) + 32
# print("A temperatura em °F é:", transformação,"°F")

#2 -

nota1= float(input("Digite a nota1:"))
nota2= float(input("Digite a nota2:"))
nota3= float(input("Digite a nota3:"))
nota4= float(input("Digite a nota4:"))
soma =(nota1 + nota2+ nota3+ nota4)/4
print("A sua média bimestral é:", soma)
