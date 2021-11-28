print("O Mal existe? ")
print('[1] - Sim [2] = Não')
resposta = int(input())
if resposta == 1:
    print("Deus sabe que o mal existe? ")
    print('[1] - Sim [2] = Não')
    resposta = int(input())
    if resposta == 1:
        print("Deus pode acabar com o Mal? ")
        print('[1] - Sim [2] = Não')
        resposta = int(input())
        if resposta == 1:
            print("Deus quer acabar com o Mal? ")
            print('[1] - Sim [2] = Não')
            resposta = int(input())
            if resposta == 1:
                print("Entao por que o Mal existe? ")
                print("[1] = Para nos testar [2] Satã [3] Livre Arbitrio")
                resposta = int(input())
                if resposta == 1:
                    print("Se ele é onisciente, já sabe o resultado e não precisa nos testar.")
                elif resposta == 2:
                    print("Se ele é onipotente e bondoso, teria destruido Satã")
                else:
                    print("Deus podia ter criado um Universo com livre arbitrio e sem o Mal? ")
                    print('[1] - Sim [2] = Não')
                    resposta = int(input())
                    if resposta == 1:
                        print("Então ele não é bom")
                    else:
                        print("Então ele não é onipotente.")

            else:
                print("Entao ele não é bom.")
        else:
            print("Então ele não é Onipontente.")
    else:
        print("Então, ele não é onisciente.")
else:    
    print("FIM")


