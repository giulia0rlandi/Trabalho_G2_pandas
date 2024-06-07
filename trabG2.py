# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

dfInstgram=pd.read_csv('C:/Users/micro1/Documents/aaaaaaaa/top_insta_influencers_data.csv',header=0,index_col=0)
print('\n1-O dfCaracCel')


print('\n2-Exiba as informacoes do dfCelular')


print('\n3-Exiba a coluna fabricante')


print('\n4.A-Renomeie as colunas sistema operacional(SO) e tamanho tela (tela). Exiba')


print('\n4.B-Renomeie as colunas bateria ligado (bateria) e bateria repouso (autonomia). Exiba')


print('\n5-Crie e exiba um DF (dfCel1) so com as colunas tela,SO,fabricante')


print('\n6-Alterar ordem das colunas: SO,fabricante,tela,camera,bateria,autonomia, peso')


print('\n7-Exibir ordenado descrescentemente por tela, fabricante')


print('\n8-Tratando NaN nas  colunas bateria e autonomia')
print('\nNas colunas bateria e autonomia NaN deve ser substituido pelo valor minimo na coluna')

print('\n10-Exiba as informacoes do dfPrecosCel')


print('\n11-Tratando NaN: colunas com preco NaN devem ser descartadas. Exiba')


print('\n13-Exiba as informacoes do dfNotasCel')


print('\n14-Renomeie Nota Tela (NTT), Nota Camera(NCC), Nota Desempenho (NTD)')


print('\n15- Concatene os 3 dataframes, criando o dfCelular. Exiba')


print('\n16- Incluindo Preco Medio (PrecoMed). Exiba' )


print('\n17- Incluindo Nota Global(NTG) =( 1XTela+1XCamera+2XDesempenho)/4. Exiba' )
#PESOS: 1, 1 e 2

print('\n----------------------------------------------------------------')
print('\n18-Graficamente (barras juntas) precos no CasaTecno e no TemTudo' )


print('\n----------------------------------------------------------------')


print('\n19- Graficamente: PrecoMedio X Nota Global')



print('\n20- Exibir os celulares com tela >= 5.7 e com preco na CasaTecno menor que 3000')

print('APENAS OS NOMES dos Modelos que atendem o criterio')



print('\n21-Categorias (faixas) de nota global: de 0 a 6, de 6(exc) a 7,de 7 a 8, de 8 a 9, acima de 9')
print('\n- Rotular com "RUIM", "REGULAR","BOM","MUITO BOM","EXCELENTE"')
print('\n Exibir TabFreq das categorias de nota')



#ATENCAO:
print('\nTabela de Frequencia Percentual (RELATIVA) das categorias graficamente')


#ATENCAO 2:
print('\nTabela de Frequencia Percentual (RELATIVA) das categorias NUMERICAMENTE')



print("\n22- Qual(is) o(s) celular(es) de pior desempenho?")



print("\n23- Qual(is) o(s) celular(es) de melhor desempenho e seus precos medios?")



print("\n24-Qual(is) o(s) celular(es) de maior nota global , seu menor preco e onde ocorre seu menor preco")
