# Machine-learning-manual
Aprendendo a fazer redes  neurais, partindo do zero, fazendo maior parte manualmente

Um projeto pessoal, a ideia desse projeto é apenas testar a aplicação, não possuindo interface gráfico e sendo de díficil acesso para pessoas que não conhece a estrutura do código python, entretanto como estou deixando publico então vou explicar as funções e seus parametros para um acesso mais básico, saliento que será dificil de entender também para quem não conhece o mecanismo das redes neurais 



Neste projeto não importei nada que não fosse nativo ao python 3.12.3, então apenas devemos seguir o texto, sem instalar nada. Tudo deve ser executado nos arquivos na raiz(arquivos que não estão dentro de outras pastas,exceto  a pasta MACHINE LEARNING MANUAL), exemplo main.py, então para tudo funcionar deve-se importar as funções de outras pastas nestes arquivos raiz 

from tools import data, backpropagation

----Funções----
-----backpropagation.Network(sizes: tuple, activation_funcs_hidden_layer, classification)-------

sizes: é um parametro aonde deve-se passar as dimensões da sua rede neural, passando como tupla ou uma lista exemplo- (2, 3, 4, 1) sendo o "2" a quantidade de inputs iniciais, aonde em uma rede neural são os dados primarios, sendo o "3 e 4" as escondidas, sendo "1" a ultima camada que retornar uma resposta

activation_funcs_hidden_layer: deve passar uma lista com a quantidade de elementos exata de camadas escondidas da sua rede
e cada elemento deve ser uma string exemplo- ['sigmoid', 'tangh', 'relu'], neste caso só posso passar para uma 
rede com 3 elementos na camada escondida exemplo- sizes=(3, 4, 4, 4, 1). Caso você passe uma lista vazia([]) ele vai setar funções de ativação como sendo 'sigmoid', sendo todas as funções validas, sendo expressa por este dicionario:

dict_act_func = {
    'sigmoid': sigmoid,
    'tangh': tangh,
    'relu': relu,
    'linear': linear

}

que no código se encontra na pasta tools/base/act_func.py

classification: uma expressão boleana, deve apenas especificar qual tipo de resultado deve-se se retornar,
exemplo se você deseja classificar o tipo de uma flor então deve setar como True, caso só queria fazer uma regressão simplês como por exemplo achar o calculo exato para converter por exemplo celsius em kelvins, deve deixar desligado

obs: eu apenas permitir que ao deixar desligado ele represente um calculos lineares, então deve-se configurar a rede neural com mais camadas para um treinamento melhor, exigindo testes e se não for possivel então sugiro personalizar, lembrando que o calculo lineares já consideram bias então por exemplo no calculo de fahrenheit deve-se passar em sizes na ultima camada o parametro 1, mesmo que o calculo correto seja 1.8c + 32, pois o 32 já será expresso por meio do bias 

Agora com a rede configurada devemos fazer o processo de treinamento, quero mostrar que possui duas formas diferentes de se treinar usando o metodo estocatico e o mini batch, essa ideia não é minha caso tenha duvidas pesquise na internet sobre esses métodos

por exemplo: rede_neural = backpropagation.Network((3, 2), ['tangh'])

---- rede_neural.trainer_weights_mini_batch(data: list, response: list, len_mini_batch: int, eppochs=100, lr=float)

data: deve-se passar uma lista que possui todos seus elementos como uma matrix(backpropagation.Matrix) exemplo
[
        backpropagation.Matrix([[0], [0], [0]]),
        backpropagation.Matrix([[1], [0], [0]]),
        backpropagation.Matrix([[0], [1], [0]]),
        backpropagation.Matrix([[1], [1], [1]])

]

cada matrix simboliza uma entrada de dados diferentes, é importante dizer que neste caso possui 3 dados entrando por vez e que cada dado deve ser representando dentro de uma lista dentro da função como sendo uma lista com apenas um parametro, fiz a escolha dessa estrutura poís facilitava as contas para o treinando, lembrando que na configuração da rede o primeiro parametro deve ser o mesmo que a quantidade de dados que entra por vez, e o ultimo a quantidade de saidas da rede

responses: deve-se passar simplismente uma lista comum com parametros numericos, no caso de redes para a classificação deve-se passar parametros numericos int, e o tamanho dessa lista precisa ser a quantidade de entradas de dados passados, neste caso foram 4 entradas exemplo: [0, 1, 1, 0]

len_mini_batch: simplismente o tamanho da batch

eppochs = quantidade de epocas para o treinamento 

lr = learning rate, sendo a taxa de aprendizado 
