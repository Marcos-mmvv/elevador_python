# Elevador de carga

nome = input('Informe o seu nome: \n')
peso = str(input('Informe o seu peso em Kg: \n')).replace(',', '.')
carga = str(input('Informe o peso da carga: \n')).replace(',', '.')
elevador = 200

peso = float(peso)
carga = float(carga)

if peso + carga <= 200:
    print(f'Elevador liberado para {nome}.')

else:
    print(f'{nome} você está com excesso de carga,\n Carga máxima é de 200KG, elevador bloqueado.')
