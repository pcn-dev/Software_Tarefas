tarefas = []

def exibir_paulo_tarefas():
    print('''
    
    𝙋𝙖𝙪𝙡𝙤 𝙏𝙖𝙧𝙚𝙛𝙖𝙨
    
    ''')
    
def exibir_opcoes():
    print('1. Adicionar tarefa')
    print('2. Ver minhas tarefas')
    print('3. Excluir tarefa')
    print('4. Sair do app')
    
def subtitulo_opcao(texto):
    print(texto)

def opcao_invalida():
    print('\nOpção inválida! Tente novamente.')
    voltar_menu()
    
def voltar_menu():
    input('\nDigite qualquer tecla para voltar ao menu de opções ')
    main()
    
def adicionar_tarefa():
    subtitulo_opcao('\nAdicionar uma tarefa\n')
    nome_da_tarefa = input('Digite o nome da tarefa que gostaria de adicionar: ')
    data_da_tarefa = input(f'Digite a data da tarefa ({nome_da_tarefa}): ')
    # Novo campo para a hora
    hora_da_tarefa = input(f'Digite a hora da tarefa ({nome_da_tarefa}) (ex: 14:30): ') 
    
    nova_tarefa = {
        'nome': nome_da_tarefa,
        'data': data_da_tarefa,
        'hora': hora_da_tarefa
    }
    
    tarefas.append(nova_tarefa)
    
    print(f'\nA tarefa "{nome_da_tarefa}", do dia {data_da_tarefa} às {hora_da_tarefa}, foi registrada com sucesso!')
    voltar_menu()
    
def ver_tarefas():
    subtitulo_opcao('\nLista de tarefas\n')
    
    if not tarefas:
        print('Nenhuma tarefa registrada.')
    else:
        # Tabela formatada
        print(f"{'#'.ljust(3)} | {'Nome da tarefa'.ljust(30)} | {'Data'.ljust(10)} | {'Hora'.ljust(5)}")
        print('-' * 55)
        for i, tarefa in enumerate(tarefas):
            print(
                f"{str(i+1).ljust(3)} | "
                f"{tarefa['nome'].ljust(30)} | "
                f"{tarefa['data'].ljust(10)} | "
                f"{tarefa['hora'].ljust(5)}"
            )
            
    voltar_menu()
    
def excluir_tarefa():
    subtitulo_opcao('\nExcluir tarefa\n')
    
    if not tarefas:
        print('Nenhuma tarefa para excluir.')
        voltar_menu()
        return

    print(f"{'#'.ljust(3)} | {'Nome da tarefa'.ljust(30)} | {'Data'.ljust(10)} | {'Hora'.ljust(5)}")
    print('-' * 55)
    for i, tarefa in enumerate(tarefas):
        print(
            f"{str(i+1).ljust(3)} | "
            f"{tarefa['nome'].ljust(30)} | "
            f"{tarefa['data'].ljust(10)} | "
            f"{tarefa['hora'].ljust(5)}"
        )
        
    try:
        indice_excluir = int(input('\nDigite o NÚMERO da tarefa que gostaria de excluir: '))
        
        indice_real = indice_excluir - 1
        
        if 0 <= indice_real < len(tarefas):
            tarefa_excluida = tarefas.pop(indice_real)
            print(f'\nA tarefa "{tarefa_excluida["nome"]}" foi excluída com sucesso!')
        else:
            print('\nNúmero da tarefa inválido.')
            
    except ValueError:
        print('\nEntrada inválida. Digite um número.')
        
    voltar_menu()
    
def sair_app():
    subtitulo_opcao('\nSaindo do app...\n')
    
def escolher_opcao():
    try:
        opcao_escolhida = int(input('\nDigite a opção que você gostaria de selecionar: '))
        
        if opcao_escolhida == 1:
            adicionar_tarefa()
        elif opcao_escolhida == 2:
            ver_tarefas()
        elif opcao_escolhida == 3:
            excluir_tarefa()
        elif opcao_escolhida == 4:
            sair_app()
        else:
            opcao_invalida()
            
    except ValueError:
        opcao_invalida()
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        voltar_menu()


def main():
    exibir_paulo_tarefas()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()