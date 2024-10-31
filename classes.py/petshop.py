from animal import Animal, cachorro,gato 

nome = "Carlos Adão"
idade = 12
peso = 23

animal1 = Animal(nome,idade,peso)
animal1.exibir_informacoes()
print(f"O nome do animal é: {animal1.exibir_nome()}")
print(f"A idade do animal é: {animal1.exibir_idade()}")
print(f"O peso do animal é: {animal1.exibir_peso()}")



#print(f"O nome do animal é {animal1.nome}") #print em apenas um atributo, mas pode gerar uma falha ou vulnerabilidade para o código. Não deixar o atributo público
Cachorro1 = cachorro("Zelda", 1, 4.4, "Pitbull", 9, False)
Cachorro1.exibir_informacoes()

gato1 = gato("Mel",5,3.3,"Azul",False)
gato1.exibir_informacoes()




