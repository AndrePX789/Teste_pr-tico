class KlingonUtils:         
    @staticmethod
    def contar_preposicao(lista):
        preposicao = 0
        for palavra in lista:
            if len(palavra) == 3 and 'd' not in palavra and palavra[2] not in letras_foo:
                preposicao += 1                   
                        
        return preposicao
    
    @staticmethod
    def contar_verbos(lista):
        verbos = 0
        verbos_1pessoa = 0
        for verbo in lista:
            if len(verbo) >= 8 and verbo[-1] in letras_foo:
                verbos += 1
                if verbo[0] not in letras_foo:
                    verbos_1pessoa +=1
        
        return verbos, verbos_1pessoa

texto_A = open('Texto_A.txt', 'r')
texto_B = open('Texto_B.txt', 'r')

lista_A = texto_A.read().split()
lista_B = texto_B.read().split()

letras_foo = ['s', 'l', 'f', 'w', 'k']

preposicao_texto_a = KlingonUtils.contar_preposicao(lista_A)
preposicao_texto_b = KlingonUtils.contar_preposicao(lista_B)
print(preposicao_texto_a)
print(preposicao_texto_b)

verbos_texto_a = KlingonUtils.contar_verbos(lista_A)
verbos_texto_b = KlingonUtils.contar_verbos(lista_B)
print(verbos_texto_a)
print(verbos_texto_b)
