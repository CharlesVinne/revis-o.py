class Pessoa:
	def __init__(self,nome,idade,genero):
		self.nome = nome   
		self.idade = idade
		self.genero = genero


class Paciente(Pessoa):
    def __init__(self, nome, idade, genero, sintoma):
        super().__init__(nome, idade, genero)
        self.sintoma = sintoma

    def imprimir_sintoma(self):
        return print('PACIENTE: ' + self.sintoma)

    def imprimir_dados(self):
        print(f'Nome: + {self.nome}')
        print('Idade:' + self.idade)
        print ('Genero:' + self.genero)
class Medico(Pessoa):
    def __init__(self,nome,idade,genero, crm):
        super().__init__(nome, idade, genero)
        self.crm = crm

    def imprimir_crm(self):
        return print('CRM: ' + self.crm)

print('____PACIENTE____')
paciente = Paciente('Gripe', 'Marcia', 'f', 26)
paciente.imprimir_dados()
paciente.imprimir_sintoma()
