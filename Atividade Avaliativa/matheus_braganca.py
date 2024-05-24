#author: Matheus Bragança - 2472190092
#Agenda com funções inserir, apagar, alterar, listar, gravar e ler os dados cadastrados.
#Requisitos:
#1 - Receba nome, tipo de telefone (cel, fixo) e telefone de pessoas e os armazene em um arquivo de texto.
#2 - Acrescente um menu principal para a decisão de leitura ou gravação do arquivo.
#3 - Acrescente no menu uma opção de ordenar a lista por nome.
#4 - Ao fazer a consulta, o código devolva "Nome cadastrado" ou "Nome não cadastrado", conforme o caso.
#5 - Tenha opção para sair do Programa.
#6- Verifique a repetição de nomes e alerte com mensagem "Usuário já está cadastrado", no caso.
################################################################################
import os
#author: Matheus Bragança
#criando agenda com o nome requisitado
agenda_de_contatos = 'matheus_braganca.txt'
def carregar_agenda():
    agenda = []
    if os.path.exists(agenda_de_contatos):
        with open(agenda_de_contatos, 'r') as arquivo:
            for line in arquivo:
                nome, tipo, telefone = line.strip().split(';')
                agenda.append({'nome': nome, 'tipo': tipo, 'telefone': telefone})
    return agenda
#salva o contato na agenda
def salvar_agenda():
    with open(agenda_de_contatos, 'w') as arquivo:
        for contato in agenda:
            arquivo.write(f"\n{contato['nome']};{contato['tipo']};{contato['telefone']}\n")
#inserir um contato na agenda
def inserir_contato(agenda):
    nome = input('\nDigite o nome: ')
    if any(contato['nome'] == nome for contato in agenda):
        print('\nUsuário já está cadastrado! Insira outro nome.')
        return
    tipo_telefone = input('Digite o tipo de telefone (cel ou fixo): ')
    telefone = input('Digite o Telefone: ')
    agenda.append({'nome':nome,'tipo':tipo_telefone,'telefone':telefone})
    print('\nNome cadastrado.')
#deleta um contato da agenda
def apagar_contato(agenda):
    nome = input('\nDigite o nome a ser apagado: ')
    for contato in agenda:
        if contato['nome']==nome:
            agenda.remove(contato)
            print("\nO Contato foi apagado com sucesso!")
            return
    print("\nNome não cadastrado.")
#atualiza uma informação na agenda    
def alterar_contato(agenda):
    nome = input('\nDigite o nome a ser alterado: ')
    for contato in agenda:
        if contato['nome'] == nome:
            nome_novo = input('Digite o novo nome: ')
            tipo_telefone = input('Digite o novo tipo de telefone: ')
            telefone = input('Digite o novo telefone: ')
            contato.update({'nome':nome_novo,'tipo':tipo_telefone,'telefone':telefone})
            print('\nContato alterado com sucesso.')
            return
    print('\nNome não cadastrado.')
#lista a agenda    
def listar_contatos(agenda):
    if not agenda:
        print('\nAgenda vazia.')
        return
    for contato in agenda:
        print(f"\nNOME: {contato['nome']}, TIPO:{contato['tipo']}, TELEFONE: {contato['telefone']}")


def ordenar_contatos(agenda):
    agenda.sort(key=lambda x: x['nome'])
    print("\nAgenda em ordem alfabética: ")
    listar_contatos(agenda)

def buscar_contato(agenda):
    nome = input('\nDigite o nome: ')
    for contato in agenda:
        if contato['nome']==nome:
            print('\nO nome está cadastrado.')
            return
    print("\nNome não cadastrado")
#menu principal
def main():
    agenda = carregar_agenda()
    while True:
        print('\n------MENU PRINCIPAL------')
        print('\n1 - INSERIR CONTATO')
        print('2 - APAGAR CONTATO')
        print('3 - ALTERAR CONTATO')
        print('4 - LISTAR CONTATO')
        print('5 - ORDENAR CONTATOS POR NOME')
        print('6 - BUSCAR CONTATO')
        print('7 - ENCERRAR')

        seletor = input("\nEscolha uma opção: ")
        if seletor =='7':
            print('\n---------------PROGRAMA ENCERRADO---------------')
            break
        elif seletor == '1':
            inserir_contato(agenda)
        elif seletor == '2':
            apagar_contato(agenda)
        elif seletor == '3':
            alterar_contato(agenda)
        elif seletor == '4':
            listar_contatos(agenda)
        elif seletor == '5':
            ordenar_contatos(agenda)
        elif seletor == '6':
            buscar_contato(agenda)
        else:
            print("\nDigite uma opção válida.")
if __name__ == "__main__":
    main()
        
        
        
    
    
