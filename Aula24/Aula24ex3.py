
# Aula 22 - 10-12-2019
# # Como Tratar e Trabalhar Erros!!!

# Dica: O mais importante é conseguir fazer! Não importa como chegou ao resultado e sim o resultado!

# Dica2: na função .open() você pode escolher entre 'r' para ler, 'w' para sobrescrever e criar um 
# arquivo novo ou o 'a' que é abreveativo de append, onde ele inclui linha no final do arquivo.
# Você sabia que o 'r', 'w' e o 'a' são string que podem ser passadas via variável exemplo:

# atributo = 'r'
# nome_arquivo = 'cadastro'
# arquivo.open(f'exercicio/{nome_arquivo}.txt',atributo)



# 1) Crie uma classe cadastro.
# Esta classe deve abrir o arquivo cadastro2.txt e guardar os cadastros numa lista com dicionários.

# 2) crie o metodo salvar os dados dos clientes em um arquivo txt.
# 3) crie um metodo para cadastrar novos clientes. O código cliente é unico por pessoa, sendo assim não pode 
# se repetir.
# 3) Crie um metodo de consulta de cliente, mostrando os dados dele na tela.
# 4) Crie um metodo para atualizar o cadastro de um cliente qualquer pelo codigo cliente.
# Após atualizar, salvar todos no arquivo "cadastro_atualizado.txt" (use o 'w' para sobrescrever o arquivo.)
#
#  Observação: Use o try/filnaly para abrir e fechar os arquivos. Veja na aula 21- Ecessões como é!

class Cadastro:

    def __init__(self):
        self.cadastros = []
        arquivo = open('Aula24/cadastro2.txt', 'r')
        for linha in arquivo:
            # linha = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117' na primeira
            linha_separada = linha.strip().split(';')
            dic = {
                'codigo': int(linha_separada[0]),
                'nome': linha_separada[1],
                'idade': int(linha_separada[2]),
                'sexo': linha_separada[3],
                'email': linha_separada[4],
                'telefone': linha_separada[5]
            }
            self.cadastros.append(dic)
        arquivo.close()
    
    def consulta(self, codigo):
        for pessoa in self.cadastro:
            if pessoa['codigo'] == codigo:
                print(f"Nome: {pessoa['nome']},\nIdade: {pessoa['Idade']},\nSexo: {pessoa['sexo']},\nEmail: {pessoa['email']},\nTelefone: {pessoa['telefone']}")
            
    



# p = Cadastro()

# for i in p.cadastros:
#     print(i)






# cad = Cadastro()
# print(cad.cadastros)

