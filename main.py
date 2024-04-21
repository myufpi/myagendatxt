# Aplicacao main (principal) da agenda
# Faz a integracao de todos os componentes 
# da aplicacao agenda

import terminal
import entidades

def show_window():
  try: 
    minha_agenda = entidades.MyAgenda() 
    agenda = terminal.Window(minha_agenda)
    agenda.executa()
  except Exception as ex: 
    print(f'Erro: {str(ex)}')

show_window()
