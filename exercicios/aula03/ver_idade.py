#esse código verifica a idade , maior de idade ,  adolescente ou criança 


idade = int(input("Digite sua Idade: "))
#se idade for maior que 18 anos maior de idade 
if idade >=18:
    print("Você é maior de Idade")
#se idade for maior que 12 anos e menor que 18 anos adolescente
elif 12 <= idade < 18:
    print("Você é Adolescente")
#se não for nenhuma dessas você é uma criança 
else:
    print("Você é uma Criança")
