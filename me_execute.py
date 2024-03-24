from os import system
from webbrowser import open as open_browser
from types import FunctionType


# All user possibles commands {'key': ('prompt name', 'command')}
COMMANDS = {
    '0': ('Sair', 'exit'),
    '1': ('Limpar Tela', 'clear_screen'),
    '2': ('Criar Ambiente Virtual', 'create_env'),
    '3': ('Abrir Site', 'start_server')
}


class Commands:
    def exit():
        quit()
        
        
    def clear_screen():
        """
        Clear the cmd window
        """
        
        system('cls')


    def create_venv() -> int:
        """
        This function start the virtual env and install the dependencies to aplication works

        Returns:
            int: 0 if everything works right; 1 if some thing get wrong
        """
        
        try:
            print('Iniciando a Máquina Virtual\n\n')
            system('python -m venv .venv')
            print('\n\nMáquina Virtual Instalada com Sucesso\nInstalando o Django 5.0.3\n\n')
            system('pip install django == 5.0.3')
            
            return 0

        except Exception as e:
            print(e)
            return 1


    def start_server() -> int:
        """
        This function start the django server and open it on browser

        Returns:
            int: 0 if everything works right; 1 if some thing get wrong
        """
        
        try:
            system('.venv/Scripts/activate.bat')
            system('python manage.py runserver')
            open_browser('http://127.0.0.1:8000/')
            return 0
        except Exception as e:
            print(e)
            return 1


    def print_users_action() -> int:
        for key in COMMANDS:
            print('%s: %s' % (key, COMMANDS[key][0]))


    def get_user_action(command_list) -> int:
        """
        This function gets the user action based on possibles actions

        Args:
            command_list: The COMMANDS constrain keys

        Returns:
            int: the user action
        """
        
        command: int;
        
        while True:
            command = input('\nSeu Comando: ')

            if command in command_list:
                return command
            else:
                print('Por favor, escolha apenas os comando acima listados')
            
    
def main():
    command: int;  # Contains the user action
    
    while True:
        Commands.print_users_action()
        command = Commands.get_user_action(COMMANDS.keys())
        action = getattr(Commands, COMMANDS[command][1])
        action()
        
        
        


if __name__ == "__main__":
    main()
    
    