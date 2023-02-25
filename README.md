# Insurance-Health-Cross-Sell

# 1. Problema de Négocio
A Insurance é uma empresa com tradição na venda de seguros de saúde. Entre tanto após chegar na sua fase de maturidade de mercado a empresa está buscando
oferecer novos produtos aos seus clientes e com isso sempre aumentar sua participação de mercado.
Então a empresa está querendo oferecer agora para seus clientes seguros veícular. Então Insurance efetuou uma pesquisa com mais de 304 mil clientes s
obre o interessse de adquirir esse novo serviço. Entre tanto há aínda mais de 76 mil clientes que não responderam essa pesquisa. 
Mais o setor de call center da empresa já muito atarefado, também tem esse dever de entrar em contato com essa lista de pessoas, mas a capacidade de telefonemas diários é apenas de 20 mil ligações.
E com isso já é visto a primeira dor da empresa é não saber quais são os clientes mais propensos a adquirir o produto. Ou seja, a escolhas dos clientes
são feitas de forma plenamente aleatória. Foi neste momento que o gestor do call center gostaria de ter uma lista com os clientes saber mais inclinados em comprar esse novo seguro automotivo e pensando nisso, o gestor decidiu chamar um especialista de dados para ajudar a saber quais os clientes com mais perfil de compra e responder as seguintes perguntas:


1. Quais são os principais insights sobre os atributos mais relevantes de clientes interessados em seguro veicular?
2. Qual a porcentagem de clientes interessados em seguro veicular, o call center conseguirá contatar fazendo 20 mil ligações?
3. Se a capacidade do call center aumentar para 40 mil ligações, qual a porcentagem de clientes interessados em adquirir um seguro veícular o 
call center conseguirá contatar?
4. Quantas ligações o call center precisa fazer para contatar 80% dos clientes interessados em adquirir um seguro veicular?

## 1.1 - Objetivo do projeto:
Com base da lista de 304 mil clientes entrevistados, será feito um ranking com por ordem de interesse(propensão de compra) dos 76 mil clientes potenciais e responder as perguntas do gestor do Call Center da empresa para que suas tommadas de decisões sejam mais assertivas por meio de dados. 

## 1.2 Planejamnto da Solução:
A solução deste projeto será seguindo o método ciclíco CRISP para que cada etapa do projeto seja entregue o mais rápido possível e agregue valor ao 
time de negócios.E entre esses processos será feito uma análise explorátorio dos dados com a finalidade de adquirir mais conhecimento sobre o negócios, selecioar as features mais relevantes e com isso será implementado um algoritmo de machine learning para que ele possa calcular as propensões de compras dos 76 mil clientes. 
 

# 2 - Insights do Projeto:

 Nesta etapa é feito uma análise explorátoria dos dados com a finalidade de ter mais connhecimento sobre o negócio e como consequência será respondida 
 a primeira pergunta do gestor do Call Center para que o mesmo já tenha condinções de melhorar suas tomadas de decisões. 
 
 **H4** Homens danificam mais os veículos do que mulheres.
 
 **Verdadeira:** Homens danificam mais os veículos do que mulheres
 
![h4_insurance](https://user-images.githubusercontent.com/78666925/220450551-bdcf1873-edeb-4b6b-a82e-78bc8ec331ca.png)

**H7** - O maior número de pessoas interessadas são pessoas com veículos com idade superior há 2 anos.

**Falso:** O maior número de pessoas interessadas, são as pessoas com veículo com idade entre 1 e 2 anos

![h7_insurance](https://user-images.githubusercontent.com/78666925/220450591-fd6bf76e-0dda-4f5f-9d4a-75b3d3f851a4.png)
 
 **H9** - Pessoas que pagam mais pelo seguro de saúde tem menos interesse no seguro veícular.
 
 **Falsa:** Pessoas que pagam mais pelo seguro de saúde tem mais interesse no seguro veícular do que as pessoas que pagam menos pelo seguro de saúde.
 
![h9_insurance](https://user-images.githubusercontent.com/78666925/220450628-d9c5320f-f260-4c90-8621-d21180e301e6.png)

# 3- Modelo de Machine Learning:

Nessa fase do projeto após fazer os processos de coleta, limpeza e exploração dos dados para selecionar as váriaveis mais relevantes, é feito a 
escolha e treinamento de alguns modelos de machine Learning para vê o tão complexo são os dados que estou trabalhando. 

Os modelos selecionados nessa primeira fase foram :

* KneighborsClassifier Model
* Random Forest Classifier Model
* XGBoost Classifier Model

E os resultados após o treinamento e validação foram:

|      Modelo         |    Precision        |     Recall          | 
| ------------------- | ------------------- | ------------------- | 
|  Mean-Xgb-Cross-Vl  |   0.423502	    |   0.016433     | 
|  Mean-Rf_Cross-Vl   |   0.364351     |   0.08557      | 
|  Mean-Knn-Vl        |   0.157051     |   0.007613     | 

Como vista na tabela acima o algoritmo que teve melhor desempenho foi o XGboost Classifier.É possível indenticar issos com as 
seguintes métricas utlizadas que foram: 

Precision que é uma métrica que calcula quantos os modelos realmente acertou em relação ao todo conjunto de exemplos que ofereci no teste generalização.
Recall que é uma métrica que calcula a quantidade também em percentual dos meu acertos em relação apenas com exemplos verdadeiros daquela classe. 

Para ter uma noção mais precisa da peformance do modelo foi feito um ranking com Top K 50. Objetivo aqui é saber mais afundo a precisão do modelo 
para uma certa quantidade de clientes selecionados em uma lista.

|      Métrica        |    Peformance        | 
| ------------------- | -------------------  | 
|  Precison           |   43.13	%    |   

Também foi adicionado um gráfco de Curva Lift para saber o tão bom meu modelo odernada era em relação a minha lista aleatória. Como é possível vê na 
imagem abaixo,o modeloodernado (linha laranja) é 4 vezes melhor do que é a lista aleatória. (linha pontilhada).  

Peformance do modelo com lista odernada X lista aleatória
![curva_elevação_lifit](https://user-images.githubusercontent.com/78666925/220880243-21c41c28-3334-4910-b8a4-df62e045e8a1.png)

Outra métrica visual que foi implementada para indentifcar a peformance do modelo foi o gráfico de Curva Cumulativa do Ganho. Esse gráfico mensura 
o percentual de pessoas interessadas de forma odernada X percentual de pessoas de forma aleatória. 

Gráfico de Curva Cumulativo de ganho
![curva_aculativa_ganho](https://user-images.githubusercontent.com/78666925/220450973-beb72810-0d1a-4286-a90b-f91585e3cb22.png)

# Resultados Financeiros:

2. Qual a porcentagem de clientes interessados em seguro veicular, o call center conseguirá contatar fazendo 20 mil ligações?

A porcentagem de pessoas interessadas são de 12.38% que totaliza uma quantidade de 9437 pessoas interessadas dentro da base de dados das 76 mil pessoas. 
Como a capacidade de ligações diária do call center é de 20 mil ligações que representa uma porcentagem de 26.24% em relação a toda base.Olhando o 
gráfico acumulativo de ganho, com essa capacidade, o call center conseguirá atingir uma estimativa de 60% de pessoas interessadas (ver linha laranja) 
que resulta em contatar 4996 com o modelo odernado. Com o modelo aleatório conseguirá apenas contatar apenas com 2427 pessoas interessdas. 
No dataset não há os valores de acordo com o perfil dos clientes, nesse caso é assumida uma premissa de acordo com os dados da feature "annual_premium" 
que representa os valores médios pagos pelos clientes dentro do período que eles contrataram o plano de saúde. Portando fazendo um ticket médio pagos 
por esses clientes é ticket médio fica em $31,604.00. 

Como é possível visualizar no gráfico na curva de elevação o modelo odernado de acordo com essa capacidade de ligações diárias é 3 vezes melhor
(linha laranja) do que o modelo aleatório (linha pontilhada).

Portanto com o modelo aleatório os ganhos serão de $76,702,908.00. Já os ganhos com o modelo odernado por ser 3 vezes melhor do que o modelo base, serão 
de $230,108,724.00. Com isso é possível afirmar que o modelo odernado é 1.50 vezes melhor do que o modelo aleatório. 

**Resposta final:** Porcentagem de pessoas interessdas é de 12.38% e o call center não conseguirá contatar todos os interessados fazendo 20 mil ligações. 

3. Se a capacidade do call center aumentar para 40 mil ligações, qual a porcentagem de clientes interessados em adquirir um seguro veícular o call center
conseguirá contatar?

Com aumenta da capacidade para 40 mil ligações diárias o percentual em relação a toda base de clientes será de 52.48%. Observando o gráfico de ganho
de ganho acumulado é possível vê com o modelo odernado é possível contatar 87% das pessoas interessadas que corresponde um total de 8210 clientes. E com
o modleo aleatório será possivel contatar apenas 4952 pessoas. 

|      Ticket médio   |  Interessados       |    Retorno           | 
| ------------------- | ------------------- | ------------------- | 
|  $31,604.00.        |      8210	          |   0.016433          | 
|  $31,604.00.        |   4952              |   0.08557           | 
  

4. Quantas ligações o call center precisa fazer para contatar 80% dos clientes interessados em adquirir um seguro veicular?

# Deploy
![deploy_google_sheets](https://user-images.githubusercontent.com/78666925/220597453-d76f2c2c-2573-4767-b04a-ed952adefba9.gif)
