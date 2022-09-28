"""
Module containig the "Options" and "CLI" Classes.
"""

from typing import List

from ...domain import Aula, ManipulateAula
from ...infra import Database


class CLI():
    """
    Class to represent a CLI and show all the functionalities to the user.
    """
    options = {
        0: '0 - Encerrar o programa.',
        1: '1 - Inserir uma nova aula no Banco de Dados.',
        2: '2 - Ler todas as aulas que estão no Banco de Dados.',
        3: '3 - Ler uma aula específica do Banco de Dados.',
        4: '4 - Editar uma aula no Banco de Dados.',
        5: '5 - Deletar uma aula do Banco de Dados.'
    }

    def run(self):
        """
        Method to run the CLI.
        """
        self.__show_greetings()
        self.__show_menu()
        self.__show_bye()

    def __show_greetings(self):
        """"""
        print()
        print('Bem vindo a sua aplicação! O que gostaria de fazer?')

    def __show_menu(self):
        """"""
        loop = True

        while loop:
            self.__show_options()
            user_option = self.__get_option()
            loop = self.__execute_option(user_option)

    def __show_options(self) -> None:
        """"""
        print()

        for option in self.options.values():
            print(option)

        print()
        print('Qualquer outra opção irá mostrar o menu novamente.')
        print()

    def __get_option(self) -> str:
        """"""
        return input('Digite a opção desejada: ')

    def __execute_option(self, option: str) -> bool:
        """"""
        # TODO: CHANGE TO PATTERN MATCHING
        database = Database()
        manipulate_aula = ManipulateAula(database, self)

        if option == '0':
            return False

        if option == '1':
            aula = self.__get_aula()
            manipulate_aula.insert(aula)

        if option == '2':
            manipulate_aula.read_all()

        if option == '3':
            assunto = self.__get_assunto()
            manipulate_aula.read_by_assunto(assunto)

        if option == '4':
            assunto = self.__get_assunto()
            new_assunto = self.__get_assunto()
            manipulate_aula.update_by_assunto(assunto, new_assunto)

        if option == '5':
            assunto = self.__get_assunto()
            manipulate_aula.delete_by_assunto(assunto)

        return True

    def __get_aula(self) -> Aula:
        """"""
        print()
        assunto = input('Digite o assunto da aula: ')

        print()
        aluno = input('Digite o nome do aluno: ')

        print()
        professor = input('Digite o nome do professor: ')

        aula = Aula(
            assunto=assunto,
            professor=professor,
            alunos=[aluno]
        )

        return aula

    def __get_assunto(self) -> str:
        """"""
        return input('Digite o assunto da aula desejada: ')

    def __show_bye(self) -> None:
        """"""
        print()
        print('Obrigado por usar nossa aplicação! Nos vemos em breve ;)')

    def show_insert_ok(self) -> None:
        """"""
        print()
        print('Aula inserida no banco de dados com sucesso!')

    def show_insert_error(self) -> None:
        """"""
        print()
        print("Erro ao inserir a aula no banco de dados!")

    def show_all_ok(self, aulas: List[Aula]) -> None:
        """"""
        print()
        print('Essas são as aulas que se encontram salvas no banco:')

        for aula in aulas:
            print(f'AULA: {aula}')
    
    def show_all_error(self) -> None:
        """"""
        print()
        print('Erro ao tentar ler as aulas no banco de dados!')

    def show_one_ok(self, aula: Aula) -> None:
        """"""
        print()
        print(f'AULA: {aula}')

    def show_one_error(self) -> None:
        """"""
        print()
        print('Erro ao tentar ler a aula desejada no banco de dados!')

    def show_update_ok(self) -> None:
        """"""
        print()
        print('Aula alterada no banco de dados com sucesso!')

    def show_update_error(self) -> None:
        """"""
        print()
        print('Erro ao tentar atualizar a aula desejada no banco de dados!')

    def show_delete_ok(self) -> None:
        """"""
        print()
        print('Aula removida do banco de dados com sucesso!')

    def show_delete_error(self) -> None:
        """"""
        print()
        print('Erro ao tentar remover a aula desejada no banco de dados!')
