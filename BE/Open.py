class setting():
    def conectionsstr(self):
        with open("ConnectionString.txt") as S:
            return str(S.read())