class Animal:
    #nome_animal = ""  #posso excluir todas essas linhas, o init já faz isso pra mim, quando chamo self.nome de algo. São atributos globais
    #idade_animal = 0
    #peso_animal = 0.0

    def __init__(self,nome_animal,idade_animal,peso_animal):
        #deixando tudo privado: usar dois _ _ 
        self.__nome_animal = nome_animal
        self.__idade_animal = idade_animal
        self.__peso_animal =peso_animal


    def exibir_informacoes(self):
        print("--"*20)
        print(f"Nome do animal : {self.__nome_animal}")
        print(f"peso do animal : {self.__peso_animal}")
        print(f"Idade do animal : {self.__idade_animal}")
        print("--"*20)
    

    def exibir_nome(self):
        return self.__nome_animal
    
    def exibir_idade(self):
        return self.__idade_animal
    
    def exibir_peso(self):
        return self.__peso_animal



class cachorro(Animal):
    def __init__(self, nome_animal,idade_animal,peso_animal,raca,nivel_energia,solta_pelos):
        super().__init__(nome_animal,idade_animal,peso_animal)
        self.__raca = raca
        self.__nivel_energia = nivel_energia
        self.__solta_pelos = solta_pelos
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"A raça do cachorro é : {self.__raca}")
        print(f"O nível de energia do cachorro é : {self.__nivel_energia}")
        
        if self.__solta_pelos:
            print(f"O cachorro solta pelos")
        else:
            print(f"O cachorro não solta pelos")
class gato(Animal):
    def __init__(self, nome_animal,idade_animal,peso_animal,cor_pelo,agressivo):
        super().__init__(nome_animal,idade_animal,peso_animal)
        self.__cor_pelo = cor_pelo
        self.__agressivo = agressivo
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"A cor do pelo é: {self.__cor_pelo}")
        if self.__agressivo:
            print(f"O gato é agressivo")
        else:
            print(f"O gato não é agressivo")




    
    