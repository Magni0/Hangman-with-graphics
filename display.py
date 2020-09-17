class UpdateDisplay:
    try_dis = ''
    word_dis = ''

    def __init__(self, word_check, tried):
        self.word_check = word_check
        self.tried = tried

    def update_try_dis(self): # function that makes tried object print neatly in terminal
        for i in self.tried:
            self.try_dis += i + ' '
        return self.try_dis

    def update_ans_dis(self): # function that makes word_check print neatly in terminal
        for i in self.word_check:
            self.word_dis += i
        return self.word_dis