import sys

class Retry:
    def retry():
        while True:
            print('Do you want to try again? y/n')
            choice = input('').lower()
            if choice == 'n':
                return False
            elif choice == 'y':
                return True
            else:
                print(f'{choice} is invalid please input n or y')
    
    def check_if_exit(check):
        if check == True:
            return
        else:
            sys.exit(0)
    
    def full_check():
        check = Retry.retry()
        Retry.check_if_exit(check)