class Log:
    def __init__(self):
        """"""

    @staticmethod
    def v(tag, message):
        print(tag, '        ', message)

    @staticmethod
    def e(tag, message):
        print('? xxxxxx ?', tag, message)
