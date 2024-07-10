#vamos ve
import random
from numpy import random
import time
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def typewriter_effect(sentence, type_delay, delete_delay):
  # Loop through each character in the sentence
  for char in sentence:
      # Write, display and delay
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(type_delay)

  # Pause after printing the entire sentence
  time.sleep(0.01)

  # Loop to delete the sentence
  for _ in sentence:
      # Write backspace, space, delete and delay
      sys.stdout.write('\b \b')
      sys.stdout.flush()
      time.sleep(delete_delay)

def jogo():
  print(Fore.BLUE+Style.BRIGHT+"Bem vindo ao jogo mais desnecessariamente difícil já feito para um trabalho escolar!\n")
  print("Infelizmente, o jogo teve que ser encurtado. Se tivesse ficado com o tamanho e complexidade originais, ele não teria sido terminado tão cedo.\n")
  print("Este é um jogo de escolhas, você terá que escolher entre várias opções e enfrentar vários desafios para finalizá-lo.\n")
  print("É um RPG de texto, então não tem muitas imagens e você tem que digitar sua resposta para prosseguir.\n")
  print("Sempre escreva apenas UMA das opções pedidas nas perguntas.")
  print("O foco do jogo é testar a sua capacidade cognitiva",Style.DIM+"(e a sua paciência também)\n")
  print(Style.DIM+"Obs.: O final do jogo foi feito enquanto a programadora estava chapada de sono, então peço desculpas pela baixa qualidade.\n")
  print("Boa sorte!",Fore.BLUE+Style.BRIGHT+"Você vai precisar.\n")
  print(Fore.LIGHTMAGENTA_EX+Style.DIM+"História: Maria Giovana Justino da Silva, N°23")
  print(Fore.LIGHTMAGENTA_EX+Style.DIM+"Programação: Rafaela Saraiva Souza, N°29\n")
  print("\n")
  start=False
  while start == False:
    typewriter_effect("Quer entrar nessa aventura? (sim/não)\n",0.05,0.01)
    answer=input()
    if answer.lower() == 'sim':
      print(Fore.BLUE+Style.BRIGHT+"Segurem seus chapéus, vamos começar!\n")
      start=True
    elif answer.lower() == "não":
      print(Fore.BLUE+"Pra quê abriu o jogo então?")
      exit()
    else:
      print("Por favor,",Fore.RED+ "insira uma resposta válida.")
  
    if start== True:
      print(Fore.CYAN+"Você acorda em um lugar desconhecido, e acaba perdendo todas as suas memórias, inclusive as de quem você é ou de como chegou ali. Tudo ao seu redor parece real, mas há algo estranho, como se estivesse dentro de um sonho fantasioso. O ambiente mescla natureza e tecnologia, com árvores cujas folhas brilham como LEDs e um céu que muda de cor conforme suas emoções e as nuvens se assemelham a algodão doce. Você se levanta, tentando entender o que está acontecendo, e percebe que suas mãos têm um aspecto pixelado, com pequenos bugs.\n")
      typewriter_effect("Melhor escolher um nome para si mesmo/a. Qual vai ser?\n",0.05,0.01)
      nome=input()
      print(Fore.CYAN+"Certo. Você se chama", nome,Fore.CYAN+ "então. \n")
      print(Fore.CYAN+"Investigando seu corpo, você apalpa sua jaqueta, calças e bolsos, até encontrar um mapa. Ao abri-lo, vê várias trilhas e suas ramificações. O ponto inicial indica uma clareira, e, sem outra alternativa, você decide seguir o mapa até lá.\n")

      print(Fore.LIGHTGREEN_EX+"""\
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⢀⣼⣦⠀⠀⣠⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣆⠀⠀⠀⠀⠀
      ⠀⠀⠒⣿⣿⣿⠓⠀⠀⠻⣿⣿⠀⢀⣴⣿⣦⡀⠀⢀⣾⣦⠘⢿⣿⣧⡀⠀⠀⠀
      ⠀⢀⣴⣿⡿⠃⡄⠈⠻⣿⣟⣉⣀⠉⣽⡿⠋⠡⠴⣿⣿⣿⠓⠀⠙⢇⠀⠀⠀⠀
      ⠀⠿⣿⠟⢁⣾⣿⣦⣀⠘⠿⠟⢁⣼⣿⣿⣷⠂⣴⣿⣿⣿⣆⠘⢶⣶⣿⠶⠤⠀
      ⠀⣀⣀⡀⢉⣿⣿⣿⡍⠀⢀⣀⠙⢻⠿⢋⣤⣾⣿⣿⣿⣿⣿⣷⣄⠙⢿⣦⡀⠀
      ⠀⠟⠋⣠⣾⣿⣿⣿⣿⣦⣌⠉⠠⣤⣤⣤⡌⢙⣿⣿⣿⣿⣿⣿⠛⠛⠂⢈⣙⠀
      ⠀⠀⣉⡉⣹⣿⣿⣿⣿⣏⠉⣉⣀⣈⠙⠋⣠⣿⣿⣿⣿⣿⣿⣿⣆⠙⠛⠛⠛⠀
      ⠀⠀⠋⣴⣿⣿⣿⣿⣿⣿⣷⣌⠉⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀
      ⠀⠴⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠦⠈⣙⠛⠛⠛⠛⠛⠛⠛⠛⣉⣉⠁⠀⠀⠀
      ⠀⠀⣦⣤⡄⢉⣉⣉⣉⠉⣡⣤⠀⠀⠀⣿⣿⣷⠀⢰⣿⣿⡇⢸⣿⣿⠀⠀⠀⠀
      ⠀⠀⣿⣿⡇⣸⣿⣿⣿⡄⢻⣿⠀⠀⠀⣿⣿⣿⠀⢸⣿⣿⡇⢸⣿⣿⠀⠀⠀⠀
      ⠀⠀⣿⣿⠁⣿⣿⣿⣿⡇⠸⠿⠀⠀⠀⣿⣿⣿⠀⢸⣿⣿⣇⠸⣿⣿⠀⠀⠀⠀
      ⠀⠀⠛⠛⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠉⠉⠉⠀⢸⣿⣿⣿⠀⠿⠿⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠛⠛⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀
      """)
      
      typewriter_effect("A Floresta Cibernética.\n",0.05,0.01)
      print("\n")
      print(Fore.CYAN+"Você finalmente chega até a grande clareira cercada por árvores com troncos metálicos e folhas luminosas. Três caminhos se abrem à sua frente, um mais à esquerda, um mais à direita e outro ao centro, cada um levando a um destino desconhecido. Na entrada de cada um deles há uma placa.\n")
      isok=False
      while isok == False:
        typewriter_effect("Quer ler as placas? (não)\n",0.05,0.01)
        placas=input()
        if placas.lower() == "não":
          typewriter_effect("Quem precisa de placas, né? Qual caminho você quer seguir? (esquerda/direita/centro)\n",0.05,0.01)
          isok=True
          
          isok=False
          while isok == False:
            caminhos=input()
            if caminhos.lower() == "esquerda":
              print(Fore.CYAN+"Você segue pela trilha com pedras brilhantes até chegar a uma caverna. Quando você se aproxima, um holograma que tem a sua exata aparência te cumprimenta.\n")
              print("Holograma: Olá,",nome,"\n")
              print(Fore.CYAN+"Você se assusta com a aparência do holograma, mas depois de tocá-lo algumas vezes e perceber que ele é imaterial, você se acalma. Você tenta dizer alguma coisa, talvez perguntar como ele sabe o nome que você acabou de inventar para si mesmo, mas ele te interrompe.\n")
              typewriter_effect("\nHolograma: Nesta caverna, um quebra-cabeça de cristais precisa ser resolvido. Cada cristal deve ser colocado na ordem correta para abrir a passagem. Descubra o valor de X e coloque os cristais em ordem decrescente de acordo com resultado de cada equação.\n", 0.05, 0)
              print("\n'Credo, ignorante'",Fore.CYAN+",você pensa, franzindo a testa. Você logo percebe que o Holograma não é alguém com quem você pode conversar.\n")
              print(Fore.CYAN+"Você entra na caverna. Há três cristais, cada um com uma equacão diferente escrita na sua superfície.\n")
              print("Cristal 1: 2x-3=43\n")
              print("Cristal 2: 5x−8=2\n")
              print("Cristal 3: x+18=66\n")
              print("(Exemplo de resposta: 1>2>3)\n")
              isok=False
              while isok== False:
                typewriter_effect("Qual é a ordem correta?\n",0.05,0.01)
                resposta=input()
                if resposta == "3>1>2":
                  print(Fore.CYAN+"Você coloca os cristais na ordem correta e a passagem se abre. O Holograma aparece novamente.\n")
                  typewriter_effect("Holograma: Você chegou ao fim da floresta, meus parabéns! Um novo destino te espera.\n",0.05,0)
                  isok=True
                else:
                  print("Não, essa não é a resposta correta.",Fore.RED+"Tente novamente.\n")
      
            elif caminhos.lower() == "direita":
              print(Fore.CYAN+"Você segue pela trilha cheia de espelhos. Ao invés de exibirem o seu reflexo normalmente, eles mostram versões distorcidas de você. São tantos espelhos que você se sente desnorteado conforme anda, mas mesmo assim persiste.\n")
              print(Fore.CYAN+"No meio do caminho, um holograma que tem a sua exata aparência te cumprimenta.\n")
              print("Holograma: Olá,",nome,"\n")
              print(Fore.CYAN+"Você se assusta com a aparência do holograma, mas depois de tocá-lo algumas vezes e perceber que ele é imaterial, você se acalma. Você tenta dizer alguma coisa, talvez perguntar como ele sabe o nome que você acabou de inventar para si mesmo, mas ele te interrompe.\n")
              typewriter_effect("Holograma: Para prosseguir, você deve resolver um enigma.\n",0.05,0)
              print("\n'Credo, ignorante'",Fore.CYAN+",você pensa, franzindo a testa. Você logo percebe que o Holograma não é alguém com quem você pode conversar.\n")
              typewriter_effect("Holograma: Veja aquela menina. Ela é filha do único filho da minha avó. O interessante é que o único filho da minha avó tem uma irmã, que é a mãe de dois meninos, que são meus primos. Além disso, a minha avó tem uma neta que tem uma filha. Ah, e meu tio é irmão do único filho da minha avó. Sabendo disso, a menina é minha irmã, minha tia ou minha mãe?\n",0.05,0)
              print(Style.DIM+"Dica: O avô de João teve dois filhos fora do casamento.\n")
              print(Fore.CYAN+"Você começa a considerar a possibilidade de isso ser um pesadêlo.")
              isok=False
              while isok == False:
                typewriter_effect("Qual é a resposta? (irmã/tia/mãe)\n",0.05,0)
                resposta=input()
                if resposta.lower()=="irmã":
                  typewriter_effect("Holograma: Você chegou ao fim da floresta, meus parabéns! Um novo destino te espera.\n",0.05,0)
                  isok=True
                else:
                  print("Não, essa não é a resposta correta.",Fore.RED+"Tente novamente.\n")
      
            if caminhos.lower() == "centro":
              print(Fore.CYAN+"Você anda pela trilha com chão de madeira, percebendo que o brilho azul que ela emitia aumentava a medida que você prosseguia. No final da trilha, Um lago brilhante bloqueia o caminho. É dele que vinha a luz. \n")
              print(Fore.CYAN+"Quando você se aproxima, um holograma que tem a sua exata aparência te cumprimenta.\n")
              print("Holograma: Olá,",nome,"\n")
              print(Fore.CYAN+"Você se assusta com a aparência do holograma, mas depois de tocá-lo algumas vezes e perceber que ele é imaterial, você se acalma. Você tenta dizer alguma coisa, talvez perguntar como ele sabe o nome que você acabou de inventar para si mesmo, mas ele te interrompe.\n")
              typewriter_effect("Holograma: Você deve resolver um problema matemático para solidificar a água e atravessar.\n",0.05,0)
              print("\n'Credo, ignorante'",Fore.CYAN+",você pensa, franzindo a testa. Você logo percebe que o Holograma não é alguém com quem você pode conversar.\n")
              typewriter_effect("Holograma: Resolva a equação: (7×3+5−2)×4−8+10÷2+(5^2−3×4)+(6+8)−(10−3)+9×(4−2).\n",0.05,0)
              print(Fore.CYAN+"\nVocê começa a considerar a possibilidade de isso ser um pesadêlo.")
              print("Exemplo de resposta: 23\n")
              isok=False
              while isok == False:
                resposta=input("Qual é a resposta?\n")
                if resposta == "131":
                  print(Fore.CYAN+"Você vê o lago se solidificar na sua frente. A paisagem se torna ainda mais bela.\n")
                  typewriter_effect("Holograma: Você chegou ao fim da floresta, meus parabéns! Um novo destino te espera.\n",0.05,0)
                  isok=True
                else:
                  print("Não, essa não é a resposta correta.",Fore.RED+"Tente novamente.\n")
            else:
              typewriter_effect("Tá bem, então.\n",0.05,0)
              typewriter_effect("Você anda por várias horas para dar a volta na floresta. Dar a volta foi uma péssima ideia, porque é um caminho absurdamente longo. Você se pergunta por que diabos você não escolheu uma das outras opções de caminho ao invés de se forçar a andar por horas só para não passar por dentro da floresta.\n",0.30,0)
            
            print(Fore.CYAN+"\nVocê deixa a floresta. Há um enorme portal à sua frente. Ao olhar em volta, você percebe que não importava qual caminho você escolhesse no início, todos te levariam a este mesmo lugar. Meio anticlimático.\n")
            typewriter_effect("Holograma: Não há linhas de código o suficiente neste progama para gerar destinos diferentes para cada caminho. Foi mal.\n",0.05,0)
            print(Fore.CYAN+"Você toma um susto com a aparição repentina do Holograma. Você decide que não vai nem tentar entender o que diabos aquilo queria dizer. Seu cérebro está frito depois de tantos desafios.\n")
            print(Fore.CYAN+"Você entra no portal. Ao atravessá-lo, você se depara com uma sala de laboratório branca, cheio de aparatos tecnológicos que você não fazia ideia para quê serviam. Há um homem virado de costas para você.\n")
            isok = True
            while isok == True:
              typewriter_effect("Chamar a atenção dele? (sim)\n",0.05,0)
              resposta=input()
              if resposta.lower() == "sim":
                print(Fore.CYAN+"Você chama a atenção dele. Ele se aproxima de você e ele lhe parece levemente familiar, mas você não consegue identificar se o conhece ou não.\n")
                typewriter_effect("Homem: Ah, finalmente você chegou. Aposto que quer se lembrar de quem é. Beba isto, vai te fazer lembrar-se de tudo.\n",0.05,0)
                print(Fore.CYAN+"O homem te entrega um líquido marrom borbulhante em uma garrafa redonda de bico comprido. Parecia uma poção.\n")
                print(Fore.CYAN+"Será que você deveria beber o líquido desconhecido e potencialmente perigoso que um completo estranho te deu?\n")
              

                typewriter_effect("Você se sente muito indeciso e prefere deixar a sorte decidir. Você rola um dado que estava em cima de uma mesa próxima.\n",0.05,0)
                isok = False
                while isok == False:
                  typewriter_effect("Se o número for menor ou igual a 3, você aceita o líquido. (ok)\n",0.05,0)
                  resposta=input()
                  if resposta.lower() == "ok":
                      dado = random.randint(1, 6)
                      print("A face superior do dado mostrou um número. Esse número foi", dado, "\n")
                      if (dado < 3) or (dado == 3):
                        print("Você bebe o líquido. Tem gosto de refrigerante. Coca-Cola gelada. Seu favorito.\n")
                        isok = True
                      elif (dado > 3):
                        print("Na verdade, esse líquido parece convidativo demais para rejeitar. Você não concorda com o resultado da sua sorte.",Fore.RED+"Tente de novo.\n")
                        isok=False
                  else:
                    print("Por favor,"+Fore.RED+"insira uma resposta válida.\n")
              
                typewriter_effect("Lucas Aoki: Gostou, né? Uma coquinha gelada é sempre bom mesmo.\n",0.05,0)
                print(Fore.CYAN+"Você se lembra de tudo agora. Você era um estudante de ensino médio, que sentia que tinha a mesma capacidade cognitiva de uma pedra. Lições de casa, provas e trabalhos se empilhavam cada vez mais, e você não conseguia acompanhar. Eram tantas preocupações e dores de cabeça diárias que tudo o que você queria era um descanso.")
                print(Fore.CYAN+"Por isso, quando anunciaram a chegada de novos headsets VR na escola, você decidiu se esgueirar para dentro da sala de informática e jogar um pouco.")
                print(Fore.CYAN+"Aparentemente, Deus decidiu te castigar, porque ao invés de descansar, você acordou em um jogo maluco de enigmas e problemas matemáticos.\n")
                typewriter_effect("Lucas Aoki: Mas você aprendeu, não aprendeu? Todos os problemas que você enfrentou e desafios que resolveu eram sobre os conteúdos que você anda aprendendo em sala. Mesmo com as dificuldades, você passou nos testes.\n",0.05,0)
                print(Fore.CYAN+"\nVocê pondera por um momento e faz que sim com a cabeça. Realmente, você merecia se dar um pouco de crédito depois de tudo isso.\n")
                typewriter_effect("Lucas Aoki: Não percebe? Foi por causa da Inteligência Artificial, da interatividade que ela proporcionou, que você pode aprender com tanta efetividade!\n",0.05,0)
                typewriter_effect("Foi para isso que eu te trouxe aqui. Eu precisava observar alguém experimentando as maravilhas desta tecnologia na prática para provar que a Inteligência Artificial pode revolucionar o ensino. Não, o mundo todo!\n",0.03,0)
                print(Fore.CYAN+"\nVocê não acha que realidade virtual é algo tão revolucionário assim. Já existe há bastante tempo.\n")
                typewriter_effect("Lucas Aoki: Ah não, não falo apenas de realidade virtual. Quando você colocou o headset VR, um chip foi inserido na sua cabeça. Seu cérebro está fazendo download de tudo que está acontecendo aqui neste exato momento! Estou falando de transferencia direta de dados! Não é incrível?\n",0.03,0)
                print(Fore.CYAN+"\nVocê imediatamente leva as mãos à cabeça. Você não se lembra de ter dado permissão para nada disso.\n")
                typewriter_effect("Lucas Aoki: Não se preocupe. Não vai te prejudicar em nada, muito pelo contrário. E então, o que me diz? Me ajudaria a transformar a humanidade?\n",0.05,0)
                isok=False
                while isok == False:
                  typewriter_effect("Você aceita? (sim/melhor voltar...)\n",0.05,0)
                  resposta=input()
                  if resposta.lower()== "sim":
                    typewriter_effect("Lucas Aoki: Ótimo! Começaremos agora mesmo.\n",0.05,0)
                    isok = True
                    print(Fore.CYAN+"Você o ajuda a propagar os benefícios da tecnologia apresentada. Vocês dão várias palestras juntos internacionalmente e deram início a uma produção em massa dos dispositivos. Logo, o mundo todo estava usufruindo do que vocês produziram.\n")
                    print(Fore.CYAN+"No entanto, o tiro saiu pela culatra. Um único curto-circuito na central de controle dos chips foi suficiente para causar morte cerebral em 90% de seus usuários. Inclusive em você. Os poucos que não tinham aderido à novidade foram os únicos que sobreviveram.\n")
                    print("\n")
                    print(Fore.RED+"THE BAD ENDING\n")
                    print("\n")
                    print("Obrigada por jogar!")
                    exit()
          
                  elif resposta.lower() == "melhor voltar...":
                    typewriter_effect("Lucas Aoki: Ah, certo... Bem, se é isso que você quer, não posso te forçar a ficar aqui...\n",0.05,0)
                    isok=False
                    print(Fore.CYAN+"\nVocê acorda de volta na sala de informática da escola, ainda com o headset VR. Você o tira e sai da sala tão silenciosamente quanto entrou. Você tenta não pensar em como agora tem um chip no seu cérebro...\n")
                    print(Fore.CYAN+"Sua única opção é voltar para a sua vida patética de estudante de ensino médio. De volta às aulas intermináveis, as provas, os trabalhos...\n")
                    print(Fore.CYAN+"Isso vai passar, claro. Nenhum sofrimento é para sempre. Um dia você vai alcançar coisas das quais você vai se orgulhar. Mas, por agora, tudo que você precisa pensar é em como diabos vai passar no Enem... \n")
                    print("\n")
                    print(Fore.GREEN+"THE GOOD ENDING\n")
                    print("\n")
                    print("Obrigada por jogar!")
                    exit()
                  else:
                    print("Por favor,",Fore.RED+ "insira uma resposta válida.")
              
              else:
                print("Por favor,",Fore.RED+ "insira uma resposta válida.")
        else:
          print("Por favor,",Fore.RED+ "insira uma resposta válida.")
jogo()
