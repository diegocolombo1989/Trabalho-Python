from Aula60.ForTwo.resolucao2.local import Local

class Terminal(Local):
    def __init__(self):
        self.__pessoas = [
                        'piloto'. 'oficial1', 'oficial2'
                        'chefe de serviço', 'comissario1', 'comissario2'
                        ,'policial', 'presidiario'
                        ]

        super().__init__(self.__pessoas)
    # valida saida de alguma pessoa do terminal
    def valida_saida(self, pessoa:str):
        if pessoa == 'policial' and 'presidiario' in self.__pessoas and len(self.__pessoas) > 1:
            return False
        if len(self.__pessoas) <= 4:
            # chefe de serviço - oficiais
            if pessoa == 'chefe de serviço' and 'piloto' in self.__pessoas and 'comissario2' in self.__pessoas
                pass
            # piloto - comissarios
            if pessoa == 'piloto' :
                pass