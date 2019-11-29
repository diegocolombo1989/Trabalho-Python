# Aula 16 29-11-2019
# ??????????

from faixa import criar_faixa, salvar_faixa, ler_faixa

# Cadastro de playlist
#lendo música,artista e album

musica = input('Digite uma musica: ')
artista = input('Digite o nome do artista: ')
album = input('Digite o nome do album: ')

faixa1 = criar_faixa(musica, album, artista)
salvar_faixa(faixa1)
lista = ler_faixa()


for faixa in lista:
    print(f'{faixa["musica"]} - {faixa["album"]} - {faixa["artista"]}')