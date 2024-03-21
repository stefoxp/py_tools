import sys


class PromptOptions:
    def __init__(self, choice: int = -1):
        self.option = choice

        if (sys.argv is not None and len(sys.argv) > 1):
            self.option = int(sys.argv[1])

        result = self.prompt(self.option)

        # return result

    def prompt(self, choice: int):
        result = ''

        if choice > 0:
            result = self.exec_choice(choice)
        else:
            while choice != 0:
                print('Per favore, scegli una delle opzioni seguenti:')
                print('0. Esci')
                print('1. Mostra il token di accesso')
                print('2. Visualizza Posta in arrivo')

                try:
                    choice = int(input())
                except ValueError:
                    choice = -1

                result = self.exec_choice(choice)

        return result

    def exec_choice(self, choice: int):
        result = ''

        try:
            print('Debug - choice =', choice)
            result = str(choice)

            if choice == 0:
                print(' - Arrivederci...')
            elif choice == 1:
                pass
            elif choice == 2:
                pass
            else:
                print(' - Scelta NON valida!\n')
        except:
            print('Errore')

        return result


if __name__ == '__main__':
    prompt_options = PromptOptions()
    # asyncio.run(main.main())