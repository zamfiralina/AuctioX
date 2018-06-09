import cx_Oracle

from Backend.DBController.SyntaxFormatter import SyntaxFormatter


class DBConnection:

    def __init__(self, address):
        self.__dbAddress = address
        self.__dbConnection = cx_Oracle.connect(self.__dbAddress)
        self.__dbCursor = self.__dbConnection.cursor()
        self.__statementResult = []

        self._DEBUG_dbCursor = self.__dbCursor

    @staticmethod
    def connect(username, password, dbAddress):
        return DBConnection(str(username + "/" + password + "@" + dbAddress))

    def close(self):
        self.__dbCursor.close()
        self.__dbConnection.close()

    def version(self):
        return self.__dbConnection.version

    def execute(self, *command):
        # executes the string as an SQL command, returning a list of tuples corresponding to the result
        try:
            if type(command) is tuple:
                args = command[1:]
                command = command[0]
                command = SyntaxFormatter.formatCommand(command)
                self.__dbCursor.execute(command, *args)
                self.__statementResult = self.__dbCursor.fetchall()
            else:
                command = SyntaxFormatter.formatCommand(command)
                self.__dbCursor.execute(command)
                self.__statementResult = self.__dbCursor.fetchall()
            return self.__statementResult

        except cx_Oracle.Error as e:
            e, = e.args

            if str(command).startswith("select") or str(command).startswith("SELECT"):
                print("Error" + e.message)
                return "Error" + e.message


    def getResults(self, n):
        # Returns a list of tuples corresponding to the first n results of the last executed command
        try:

            return self.__statementResult[:n - 1]

        except cx_Oracle.Error as e:
            e, = e.args
            print("Error" + e)
            return e

    def getResultsAll(self):
            # Returns a list of tuples corresponding to the results of the last executed command
        try:
            return self.__statementResult

        except cx_Oracle.Error as e:
            e, = e.args
            print("Error" + e)
            return e

    def getResultsInRange(self, start, stop):
            # Returns a list of tuples corresponding to the results of the last executed command, with an index in the [start, stop] range
        try:
            return self.__statementResult[start:stop]

        except cx_Oracle.Error as e:
            e, = e.args
            print("Error" + e)
            return e

    def getResultsInPagesOf(self, pageSize):
            # Returns a list of "pages", lists of tuples, corresponding to the results of the last executed command
        try:
            pages = int(len(self.__statementRestul)/pageSize)
            resultPages = []

            for i in range(pages):
                resultPages.append(self.__statementRestul[pages * pageSize : i * pageSize + pageSize])

            resultPages.append(self.__statementRestul[pages * pageSize :])
            return resultPages

        except cx_Oracle.Error as e:

            e, = e.args
            print("Error" + e)
            return e

    def callFunction(self, funcName, returnType, parameters):
            # Calls the DB function with the given name and arguments, returning the result as a variable of the given type
        try:
            return self.__dbCursor.callfunc(funcName, returnType, parameters)

        except cx_Oracle.Error as e:
            e, = e.args
            print("Error" + e)
            return e

    def callProcedure(self, procName, parameters):
            # Calls the provided procedure with the provided arguments, returning a copy of the parameres list, with the "out" parameters modified
        try:
            return self.__dbCursor.callproc(procName, parameters)

        except cx_Oracle.Error as e:
            e, = e.args
            print("Error" + e)
            return e
