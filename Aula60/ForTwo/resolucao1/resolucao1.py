# técnica
     # 'piloto'
     #'oficial1'
     # 'oficial2'

# cabine
    # 'chefe de servico'
    # 'comissario1'
    # 'comissario2'

# passageiro
     #'policial'
     # 'presidiario'

terminal = [ 'descricao':'piloto', 'oficial1'. 'oficial2', 'chefe de servico', 'comissario1', 'comissario2', 'policial', 'presidiario']
aviao = {'descricao':'aviao', 'pessoas' : [] }

def retirar(lista:list):
    lista.remove(item)


def inserir(item, lista:list):
    lista.append(item)

def viagem(motorista, passageiro, lista_saida, lista_chegada):
    fortwo = embarque(motorista, passageiro, lista_saida)
    fortwo['motorista'] = motorista
    fortwo ['passageiro'] = passageiro
    print('Iniciando a viagem...')
    # alto aoplamento
    desembarcando (fortwo, lista_chegada)

def embarque(motorista,passageiro, lista:list):
    lista.remove(motorista)
    lista.remove(passageiro)
    fortwo = {'motorista': motorista, 'passageiro': passageiro}
    print(f"{fortwo['motorista']} embarcou como motorista")
    print(f"{fortwo['passageiro']} embarcou como passageiro")
    return fortwo

def desembarcando(fortwo, lista:list):

    print(f'{passageiro} desembarcou')
    print(f'{motorista} desembarcou')
    lista.append(fortwo['motorista'])
    lista.append(fortwo['mpassageiro'])
