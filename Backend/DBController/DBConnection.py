import cx_Oracle

class DBConnection:

    def __init__(self, address):
        self.__dbAddress = address
        self.__dbConnection = cx_Oracle.connect(self.__dbAddress)
        self.__dbCursor = self.__dbConnection.cursor()
        self.__statementResult = []

    @staticmethod
    def connect(username, password, dbAddress):
        return DBConnection(str(username + "/" + password + "@" + dbAddress))

    def close(self):
        self.__dbCursor.close()
        self.__dbConnection.close()

    def version(self):
        return self.__dbConnection.version

    def execute(self):
        pass