import entidades
import os
import platform

# Classe que executa a integracao entre PessoaValida e ManipulaArquivoTexto
# em modo Terminal
class Window: 
  def __init__(self, minha_agenda):
    # inicializa da agenda de contatos
    self.minha_agenda = minha_agenda

  # Limpa a tela ao iniciar a janela de terminal
  def limpa_tela(self):
    if platform.system != 'Windows':
      os.system('clear')
    else:
      os.system('cls')

  # Dadas as informacoes de contato, insere contato na agenda
  def insere_contato(self):
    try: 
      cpf = input("CPF: ")
      nome = input("NOME: ")
      data_nascimento = input("Data Nascimento: ")
      if (len(cpf)==0 or len(nome)==0):
        print(f"Atenção: CPF e Nome obrigatório")
      else:
          try: 
            novo_contato = entidades.PessoaValida(cpf, nome, data_nascimento)
            self.minha_agenda.insere_contato(novo_contato)
            msg = f'Seu CPF: {cpf}, nome: {nome} e data_nascimento: {data_nascimento}'
            print(f"Informação: {msg}")
          except Exception as ex: 
            print(f"Atenção: {str(ex)}")
    except Exception as ex: 
      print(f"Atenção: {str(ex)}")

  # Dado um cpf valido e que exista na agenda remove o contato
  def remove_contato(self):
    try:
      cpf = input("CPF: ")
      if len(cpf)==0: 
          print(f"Atenção: informe o CPF!")
      else:
          try: 
              contato = self.minha_agenda.pesquisa_contato(cpf)
              if contato: 
                pessoa = entidades.PessoaValida(cpf, contato[0], contato[1])
                self.minha_agenda.remove_contato(pessoa)
                msg = f"O contato {pessoa.nome}, {pessoa.cpf}, {pessoa.data_nascimento} removido."
                print(f"Informação: {msg}")
              else: 
                print('Contato não encontrado!')
          except Exception as ex:
              print(f"Atenção: {str(ex)}")
    except Exception as ex:
      print(f"Atenção: {str(ex)}")

  # Faz a pesquisa de um contato por CPF
  def pesquisa_contato(self):
    cpf = input("Qual o CPF? ")
    contato = self.minha_agenda.pesquisa_contato(cpf)
    if contato:
        print(f"{contato}")
    else:
      print(f"Atenção: Contato não encontrado!")

  # Mostra todos os contatos cadastrados no arquivo
  def lista_contatos(self):
    contatos = self.minha_agenda.listar_conteudo()
    if contatos: 
      for contato in contatos:
        print(contato, end='')
    else: 
      print("Agenda vazia!")

  # Mostra o menu de opcoes da agenda de contatos  
  def menu(self):
    print("### Mini agenda de contatos ###")
    print(f"1. Inserir contato")
    print(f"2. Listar contatos")
    print(f"3. Pesquisar contato")
    print(f"4. Remover contato")
    print(f"5. SAIR")

  # Executa a agenda de contatos
  def executa(self):
    self.limpa_tela()
    while (True):
      self.menu()
      opcao = input("Qual a sua opção? ")
      if opcao=='1': 
        self.insere_contato()
      elif opcao=='2':
        self.lista_contatos()
      elif opcao=='3':
        self.pesquisa_contato()
      elif opcao=='4':  
        self.remove_contato()
      elif opcao=='5':
        break
      else:
        print(f"Opção {opcao} inválida!")
