#
#
#
"""
"""

class Crud:
    def __init__(self):
        pass


    def colunas(self):
        lista = []
        #identificação das colunas no mysql
        colunas = ['alunos.id','alunos.nome','alunos.profissao', 'alunos.nascimento','alunos.sexo','alunos.peso', 'alunos.altura', 'alunos.nacionalidade']
        
        #identificação para escolher a coluna do select
        visualizacao = ['id','nome','profissao','nascimento','sexo','peso','altura','nacionalidade']


        while True:
            for i, j in enumerate(visualizacao, start = 1 ):
                print(f'{i} - {j}')

            escolha = int(input('Qual colunas você deseja ver que você deseja ver? '))
            
            for i in range(len(colunas)):
                if escolha-1 == i:
                    visualizacao.pop(i)
                    string = colunas.pop(i)
                    lista.append(string)
            continuar = int(input('''Deseja adiconar mais uma coluna?
                              1 - Sim
                              2 - Não'''))
            if continuar == 2:
                break
                
        lista = ','.join(lista)
        return lista
      
    def where(self):
        lista = ''
        criterios = []
        colunas = ['alunos.id','alunos.nome','alunos.profissao', 'alunos.nascimento','alunos.sexo','alunos.peso', 'alunos.altura', 'alunos.nacionalidade']
        visualizacao = ['id','nome','profissao','nascimento','sexo','peso','altura','nacionalidade']
        lista_de_operadores = ['=','>','<']
        
        while True:
            lista= []
            for i, j in enumerate(visualizacao):
                print(f'{i+1} - {j}')

            escolha = int(input('Qual colunas você deseja utilizar como validação? '))

            for i in range(len(colunas)):
                if escolha-1 == i:
                    visualizacao.pop(int(i))
                    string = colunas.pop(int(i))
                    criterios.append(string)

                    operador = int(input('''Qual o critério: 
                                    1 - igual
                                    2 - Maior que
                                    3 - Menor que
                                    '''))
                    
                    criterio = lista_de_operadores.pop(operador-1)
                    criterios.append(criterio)
                    
                    valor_da_operacao = input('Qual o valor para comparação: ') 

                    criterios.append(valor_da_operacao)
                   
            lista.append(' '.join(criterios))
            continuar = int(input('''Deseja adiconar mais uma coluna? 
                            1 - Sim
                            2 - Não'''))
            if continuar == 1:
                escolha = int(input('''Deseja utilizar qual critério:
                                    1 - and
                                    2 - or'''))
                if escolha == 1:
                    criterios.append('and')
                else:
                    criterios.append('or')
            else:
                break 
        lista = ' '.join(lista)
        return lista    
    
    def unir(self):
        visualizar = self.colunas() 
        criterio = self.where()
        query = f'SELECT {visualizar} from alunos where {criterio};'
        return query


        

    # def select(self):
    #     self.opcoes()
        
