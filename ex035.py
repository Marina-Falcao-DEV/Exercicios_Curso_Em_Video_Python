print('=+='*10)
print('Analisando um triângulo')
print('=+='*10)
a = float(input('Qual o comprimento (cm) do primeiro lado do triangulo? '))
b = float(input('Qual o comprimento (cm) do segundo lado do trinângulo? '))
c = float(input('Qual o comprimento (cm) do terceiro lado do triângulo? '))
if a < b + c and b < a + c and c < a + b:
    print ('Irá formar um triângulo!!!')
else:
    print('Não irá formar um triângulo!!!')
