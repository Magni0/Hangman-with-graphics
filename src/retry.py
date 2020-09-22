class Retry:
    def check_retry():
        while True:
            print('Do you want to try again? y/n')
            choice = input('').lower()
            if choice == 'n':
                return False
            elif choice == 'y':
                return True
            else:
                print(f'{choice} is invalid please input n or y')