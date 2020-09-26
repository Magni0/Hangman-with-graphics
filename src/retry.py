import sys


class Retry:

    """used to ask retry & resposible for exiting the application"""

    def retry():

        """asks for input
        returns true if input == y
        returns false if input == n
        """

        print('Do you want to play again? y/n')
        choice = input('').lower()
        if choice == 'n':
            return False
        elif choice == 'y':
            return True
        else:
            print(f'{choice} is invalid please input n or y')
            Retry.retry()

    def check_if_exit(check: bool):

        """if argument False:
            exits application with exit code 0
        """

        if check:
            return
        else:
            sys.exit(0)

    def retry_or_exit():

        """combines Retry.retry & Retry.check_if_exit
        if input of Retry.retry == 'n' exits application
        """

        check = Retry.retry()
        Retry.check_if_exit(check)
