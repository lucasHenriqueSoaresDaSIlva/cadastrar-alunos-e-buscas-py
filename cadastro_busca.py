# Lucas Henrique DEV2B
def mostrar_menu():
    print("Menu de Opções:")
    print("1. Cadastrar aluno")
    print("2. listar alunos")
    print("3. Pesquisar aluno")
    print("4. Sair ")
    
    
def cadastrar_aluno(alunos):
    nome = input("Digite o nome do aluno: ").strip()
    idade = input("Digite a idade do aluno: ").strip()
    curso =input("Digite o curso do aluno: ").strip()
    
    aluno = {"nome":nome,"idade":idade,"curso":curso}
    
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!")
    
def listar_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:("\nLista de Alunos:")
    for i,aluno in enumerate(alunos, start=1):
        print(f"{i}. Nome: {aluno['nome']}, Idade: {aluno['idade']}, Curso: {aluno['curso']}")
        
def pesquisar_aluno(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    nome_buscasr = input("Digite o nome do aluno para pesquisar: ").strip()
    encontrados = False
    for aluno in alunos:
        if aluno['nome'].lower() == nome_buscasr.lower():
            print(f"Aluno encontrado: Nome: {aluno['nome']}, Idade: {aluno['idade']}, Curso: {aluno['curso']}")
            encontrados = True
            break
    if not encontrados:
        print("Aluno não encontrado.")
        
def main ():
    alunos = []
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opcção (1-4): ").strip()
        if opcao == '1':
            cadastrar_aluno(alunos)
        elif opcao =='2':
            listar_alunos(alunos)
        elif opcao =='3':
            pesquisar_aluno(alunos)
        elif opcao == '4':
            print("Saindo do programa")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
     