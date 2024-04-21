import datetime
import os
import utilidades

class PessoaValida:
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        # inicializa classe de validacao de dados
        self.validador = utilidades.ValidadorDados()
        # Chama o metodo para validar os dados da pessoa
        self.valida_dados()

    # calcula a idade da pessoa baseado no ano corrente
    def calcular_idade(self):
        hoje = datetime.datetime.now()
        ano_corrente = hoje.year
        if self.data_nascimento:
          data_temp = self.data_nascimento.split("/")
          ano_nascimento = int(data_temp[2])
          idade = ano_corrente - ano_nascimento
          return idade

    # valida os dados da pessoa de acordo com as
    # regras de validacao da classe ValidadorDados
    def valida_dados(self):
      self.validador.cpf = self.cpf
      self.validador.data_nascimento = self.data_nascimento
      if not self.validador.validar_cpf():
        raise ValueError('CPF inválido!')
      if not self.validador.validar_data_nascimento():
        raise ValueError('Data de nascimento inválida')

class ManipulaArquivoTexto:
  def __init__(self, nome_arquivo):
    self.nome_arquivo = nome_arquivo
    # prepara o arquivo para gravar dados
    self.inicializa_arquivo(self.nome_arquivo)

  # Checa se o arquivo existe
  def arquivo_existe(self,nome_arquivo):
    if os.path.exists(nome_arquivo):
        return True
    else:
        return False

  # Inicializa o arquivo
  # Caso o arquivo ainda nao exista, e criado um novo arquivo pronto para gravacao
  # Se o arquivo ja existe, informa que o arquivo foi inicializado com sucesso
  def inicializa_arquivo(self, nome_arquivo):
    if not self.arquivo_existe(nome_arquivo):
        with open(nome_arquivo, mode="w") as file:
            print(f'Arquivo {nome_arquivo} criado com sucesso!')
    else:
        print(f'Arquivo {nome_arquivo} inicializado com sucesso!')

  # Carrega os dados do arquivo em uma estrutura da memoria principal
  # A estrutura escolhida para guardar os dados do arquivo foi um dicionario
  def carrega_contatos(self):
    contatos = {}
    if self.arquivo_existe(self.nome_arquivo):
        with open(self.nome_arquivo, mode='r') as file:
            for linha in file:
                cpf, nome, data_nascimento = linha.strip().split(';')
                contatos[cpf] = (nome, data_nascimento)
        return contatos
    else:
        return dict()

  # Salva os dados (contatos) da memoria principal no arquivo em memoria secundaria
  def salvar_contatos(self, contatos):
    with open(self.nome_arquivo, mode='w') as file:
        for cpf, dados in contatos.items():
            nome, data_nascimento = dados
            nova_linha = '\n'
            file.write(f"{cpf};{nome};{data_nascimento}{nova_linha}")
  
  # Insere os dados de um contato direto no arquivo em memoria principal
  # obs: faz uma busca no dicionario de contatos para checar se o contato ainda nao existe
  def insere_contato(self, pessoa):
    contatos = self.carrega_contatos()
    if pessoa.cpf not in contatos:
        registro = pessoa.cpf + ';' + pessoa.nome + ';' + pessoa.data_nascimento
        with open(self.nome_arquivo, 'a') as file_temp:
            conteudo = registro + "\n"
            file_temp.write(conteudo)
    else:
        raise ValueError("CPF já existe!")

  # Lista os contatos a partir do conteudo do arquivo em memoria secundaria
  def listar_contatos(self):
    lista_conteudo = []
    if self.arquivo_existe(self.nome_arquivo):
      with open(self.nome_arquivo, mode='r') as file_temp:
        for linha in file_temp:
          lista_conteudo.append(linha)
    else:
      raise ValueError(f'O arquivo {self.nome_arquivo} ainda não existe!')
    return lista_conteudo

  # Remove um contato do dicionario de contatos e depois 
  # salva o dicionario atualizado no arquivo na memoria secundaria
  def remover_contato(self, pessoa):
    contatos = self.carrega_contatos()
    if contatos:
        if pessoa.cpf:
            if pessoa.cpf in contatos:
                del contatos[pessoa.cpf]
                self.salvar_contatos(contatos)
            else:
                raise ValueError("CPF não existe!")
    else:
        raise ValueError("Agenda vazia!")

  # Faz a pesquisa (pelo cpf) de um contato no dicionario de contatos
  # Retorna uma tupla (nome, data_nascimento) contendo os dados do contato encontrado
  def pesquisar_contato_por_cpf(self, cpf):
    contatos = self.carrega_contatos()
    if contatos:
        if cpf in contatos:
            return contatos[cpf]
        else:
            return None
    else:
        return None

# Classe que integra PessoaValida e ManipulaArquivoTexto
class MyAgenda:
  def __init__(self):
    self.nome_arquivo = "agenda.txt"
    # inicializa o manipulador de arquivo texto
    self.manipuladorArquivoTexto = ManipulaArquivoTexto(self.nome_arquivo)

  def insere_contato(self, pessoa):
    self.manipuladorArquivoTexto.insere_contato(pessoa)

  def remove_contato(self, pessoa):
    self.manipuladorArquivoTexto.remover_contato(pessoa)

  def pesquisa_contato(self, cpf):
    contato = self.manipuladorArquivoTexto.pesquisar_contato_por_cpf(cpf)
    return contato

  def listar_conteudo(self):
    lista = []
    lista = self.manipuladorArquivoTexto.listar_contatos()
    return lista
