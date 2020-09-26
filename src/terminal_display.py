class UpdateDisplay:

    """changes lists to strings with certain changes"""

    try_dis: str = ''
    word_dis: str = ''

    def __init__(self, word_check: list, tried: list):
        self.word_check = word_check
        self.tried = tried

    def update_try_dis(self):

        """changes the argument 'tried' in to a string with a white
        space between each element
        """

        for i in self.tried:
            self.try_dis += i + ' '
        return self.try_dis

    def update_ans_dis(self):

        """changes argument 'word_check' into a string"""

        self.word_dis = ''
        for i in self.word_check:
            self.word_dis += i
        return self.word_dis
