def autoriza_voto(ano): #-> Função de validação de idade
    idade = 2021 - ano #-> ano autal - ano de nascimento = idade atual
    voto = 0 #-> Variavel que ira resever o resultado,indicando se é obrigado, opcional ou negado.
    if idade >= 18 and idade < 65: #-> Si a idade é maio a 18 ou menor a 65.
        voto = 'Obrigatorio'
    elif idade >= 16 and idade < 18 or idade >= 65: #-> se a idade é igual ou maior a 16, menor a 18 ou maior/igual a 65.
        voto = 'Opcional'
    elif idade < 16: #-> se a idade é menor a 16.
        voto = 'Negado'
    return voto #-> Retorna o valor de voto.
def votacao(permissao):
    candidato1 = 0 #-> Variavel que ira resever a contagem do voto, caso seja escolido.
    candidato2 = 0 #-> Variavel que ira resever a contagem do voto, caso seja escolido.
    candidato3 = 0 #-> Variavel que ira resever a contagem do voto, caso seja escolido.
    branco = 0 #-> Variavel que ira resever a contagem do voto, caso seja escolido.
    nulo = 0 #-> Variavel que ira resever a contagem do voto, caso seja escolido.
    totalvotos = 0 #-> Variavel que ira resever a soma de todos os votos.
    finalvotacao=[0,0,0,0,0,0] #-> Lista com valores em 0 para retornar sem adicionar votos.
    if permissao == 'Negado': #- se a idade for menor a 16 a autorização sera negada.
        print('Você não pode votar') #-> printa você não pode votar e não altera a contagem de votos.
        return #-> Retorna vacio para nao alterar a contagem de votos.
    elif permissao == 'Opcional': #-> decide se os eleitores dentro da faixa opcional vai votar ou nao.
        decisao = input('Você deseja votar? Sim/Não:\n').capitalize().replace(' ','').replace('a','ã') #-> decisao do eleitor.
        if decisao == 'Não':#-> caso nao queira votar retornara a lista em 0 para nao alterar a contagem.
            return finalvotacao #->  retorna a lisa em 0
        elif decisao == 'Sim': #-> caso o eleitor dentro da faixa de voto opcional responda sim, entra na lista de votos.
            print('Opções de votos:\nGoku 1\nNaruto 2\nDeku 3\nVoto em Branco 4\nNulo 5') #->  printa a lisata de candidatos.
            candidato = int(input('Disgite o seu voto:\n'))#->  solicita o voto do eleitor.
            if candidato == 1:#-> se o voto for igual a 1 a contagem é computada para o primeiro candidato.
                candidato1 += 1 #-> computação do voto.
                totalvotos += 1 #-> contagem total de votos.
            elif candidato == 2: #->  se o voto for igual a 2 a contagem é computada para o segundo candidato.
                candidato2 +=1#-> computação do voto.
                totalvotos += 1#-> contagem total de votos.
            elif candidato == 3:#-> se o voto for igual a 3 a contagem é computada para o terceiro candidato.
                candidato3 += 1#-> computação do voto.
                totalvotos += 1#-> contagem de votos.
            elif candidato == 4:#-> se o voto for igual a 4 a contagem  é computada para voto em branco.
                branco += 1#->  computação do voto.
                totalvotos += 1#-> contagem de votos.
            elif candidato == 5:#->  se o voto for igual a 5 a contagem é computada para voto nulo.
                nulo +=1 #-> computação do voto.
                totalvotos += 1 #->  contagem de votos.
        finalvotacao=[] #->  lista onde serão guardados os resultados de cada opção de voto.
        finalvotacao.append(candidato1) #->  será adicionado o elemento 0 ou 1 no indice 0 da lista.
        finalvotacao.append(candidato2)#->  será adicionado o elemento 0 ou 1 no indice 0 da lista.
        finalvotacao.append(candidato3)#->  será adicionado o elemento 0 ou 1 no indice 0 da lista.
        finalvotacao.append(branco)#->  será adicionado o elemento 0 ou 1 no indice 0 da lista.
        finalvotacao.append(nulo)#->  será adicionado o elemento 0 ou 1 no indice 0 da lista.
        finalvotacao.append(totalvotos)#->  será adicionado o elemento 0 ou 1 no indice 0 da lista.
        return finalvotacao #-> retornara a lista com seus resultados para ser guardada fora da função.
    elif permissao == 'Obrigatorio': #-> ingressa a votação para os eleitores que tem voto obrigatorio.
        print('Opções de votos:\nGoku 1\nNaruto 2\nDeku 3\nVoto em Branco 4\nNulo 5')#->  printa a lisata de candidatos. 
        candidato = int(input('Disgite o seu voto:\n'))#->  solicita o voto do eleitor.
        if candidato == 1:#-> se o voto for igual a 1 a contagem é computada para o primeiro candidato.
            candidato1 += 1#-> computação do voto.
            totalvotos += 1#-> contagem total de votos.
        elif candidato == 2:#->  se o voto for igual a 2 a contagem é computada para o segundo candidato.
            candidato2 +=1#-> computação do voto.
            totalvotos += 1#-> contagem total de votos.
        elif candidato == 3:#-> se o voto for igual a 3 a contagem é computada para o terceiro candidato.
            candidato3 += 1#-> computação do voto.
            totalvotos += 1#-> contagem total de votos.
        elif candidato == 4:#-> se o voto for igual a 4 a contagem  é computada para voto em branco.
            branco += 1#-> computação do voto.
            totalvotos += 1#-> contagem total de votos.
        elif candidato == 5:#->  se o voto for igual a 5 a contagem é computada para voto nulo.
            nulo +=1#-> computação do voto.
            totalvotos += 1#-> contagem total de votos.
        finalvotacao=[]#->  lista onde serão guardados os resultados de cada opção de voto.
        finalvotacao.append(candidato1)#->  será adicionado o elemento 0 ou 1 no indice 0 da lista.
        finalvotacao.append(candidato2)#->  será adicionado o elemento 0 ou 1 no indice 0 da lista.
        finalvotacao.append(candidato3)#->  será adicionado o elemento 0 ou 1 no indice 0 da lista.
        finalvotacao.append(branco)#->  será adicionado o elemento 0 ou 1 no indice 0 da lista.
        finalvotacao.append(nulo)#->  será adicionado o elemento 0 ou 1 no indice 0 da lista.
        finalvotacao.append(totalvotos)#->  será adicionado o elemento 0 ou 1 no indice 0 da lista.
        return finalvotacao#-> retornara a lista com seus resultados para ser guardada fora da função.
siclo = 'Sim'#-> Gera a chave para rodar o questionario.
contagem = [] #->Lista dispensavel, aqui sera guardado todos os valores computados por todos os eleitores.
candidato1 = []#->Lista onde será guardados todos os votos que esta opção receber.
candidato2 = []#->Lista onde será guardados todos os votos que esta opção receber.
candidato3 = []#->Lista onde será guardados todos os votos que esta opção receber.
branco = []#->Lista onde será guardados todos os votos que esta opção receber.
nulo = []#->Lista onde será guardados todos os votos que esta opção receber.
totalvotos = []#->Lista onde será guardados todos os votos que esta opção receber.
while siclo == 'Sim': #-> Sclo de repetição.
    ano_nascimento = int(input('Digite o ano no qual você nasceu (No formato XXXX):\n'))#-> Solicita ao usuaio seu ano de nascimento para verificar se deve votar.
    idade = autoriza_voto(ano_nascimento) #-> recebe o resultado da autorização de voto e guarda na variavel para poder ser utilizado.
    if idade == 'Negado': #-> caso a primeira funçaõ devolva que o usuario não tem idade de votar vai, vai entrar na segunda função para informar que o mesmo não esta habilitado para participar.
        licenca = votacao(idade) #-> envia a informação para a função votação que retornara que o usuario não pode votar.
    elif idade == 'Obrigatorio' or idade == 'Opcional': #-> caso o usuario este dentro das idades habilitadas para votar envia esta salva os resultados da lista emitida pela função votação.
        licenca = votacao(idade) #-> envia para a função votação que o usuario é apto a escolher se quer votar ou se é obrigado a votar.
        contagem.append(licenca)#-> recebe todos os resultados da votação é guarda na lista contagem.
        candidato1.append(licenca[0])#->recebe o indice 0 da lista criada fora da função para e guarda cada voto que o candidato 1 recebeu.
        candidato2.append(licenca[1])#->recebe o indice 1 da lista criada fora da função para e guarda cada voto que o candidato 2 recebeu.
        candidato3.append(licenca[2])#->recebe o indice 2 da lista criada fora da função para e guarda cada voto que o candidato 3 recebeu.
        branco.append(licenca[3]) #->#->recebe o indice 3 da lista criada fora da função para e guarda cada voto que a opção reebeu.
        nulo.append(licenca[4])#->#->recebe o indice 4 da lista criada fora da função para e guarda cada voto que a opção reebeu.
        totalvotos.append(licenca[5])#->recebe o indice 5 da lista criada fora da função para somar a quantidade total de votos.
    siclo = input('Resta outro eleitor? Sim/Não:\n').capitalize().replace(' ','').replace('a','ã') #-> consulta com o usuario se iremos receber mais algum eleitor, caso a resposta seja sim, repere o ciclo completo. Caso a resposta seja nao finaliza e mostra o resultado.  
rescan1 = sum(candidato1) #-> recebe a soma de votos que o candidato teve.
rescan2 = sum(candidato2) #-> recebe a soma de votos que o candidato teve.
rescan3 = sum(candidato3) #-> recebe a soma de votos que o candidato teve.
resbran = sum(branco)#-> recebe a soma de votos que a opção teve.
resnul = sum(nulo)#-> recebe a soma de votos que a opção teve.
resvot = sum(totalvotos)#-> recebe a soma total de votos efetivados.
if rescan1 > rescan2 and rescan1 > rescan3:#->verifica se o numero de votos do primeiro candidato é o maior e printa os resultados.
    print(f'\nA contagem total de votos foi de {resvot}.\n\n{resbran} Votos em brando.\n\n{resnul} Votos nulos.\n\n---O vencedor foi Goku com {rescan1} votos.---\n\nNaruto ficou com {rescan2} votos.\n\nDeku ficou com {rescan3} votos.')
elif rescan2 > rescan1 and rescan2 > rescan3:#->verifica se o numero de votos do seundo candidato é o maior é o maior e printa os resultados.
    print(f'\nA contagem total de votos foi de {resvot}.\n\n{resbran} Votos em brando.\n{resnul} Votos nulos.\n\n---O vencedor foi Naruto com {rescan2} votos.---\n\nGoku ficou com {rescan1} votos.\n\nDeku ficou com {rescan3} votos.')
elif rescan3 > rescan1 and rescan3 > rescan2:#->verifica se o numero de votos do terceito candidato é o maior é o maior e printa os resultados.
    print(f'\nA contagem total de votos foi de {resvot}.\n\n{resbran} Votos em brando.\n{resnul} Votos nulos.\n\n---O vencedor foi Deku com {rescan3} votos.---\n\nNaruto ficou com {rescan2} votos.\n\nGoku ficou com {rescan1} votos.')
print('\n\nFim da votação.')