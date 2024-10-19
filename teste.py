import os





def exibir_nome():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░""")


def exibir_op():
 print('1. Cadastrar restaurantes')
 print('2. Listar restaurantes')
 print('3. Ativar restaurantes')
 print('4. Sair\n')


def finalizar_app():
 os.system("cls")
 #OS.system("clear") limpar o terminal no mac
 print('finalizando o app\n')


def escolher_opcao():
    
    #escolhe a opção e transforma em inteiro.
    opcao_escolhida = int(input('Escolha uma opção: '))
    match opcao_escolhida:
        case 1:
            print('Cadastrar restaurantes')
        case 2:
            print('listar restaurantes ')
        case 3:
            print(' Ativar restaurantes ')
        case 4:
            finalizar_app()
        case _:
            print('Opção inválida!')
            
  
def main():
   exibir_nome()
   exibir_op()
   escolher_opcao()

   
if __name__ == '__main__':
    main()