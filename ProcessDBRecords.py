import pyodbc


class ExecuteSQLCommand:

    fields = []

    def fieldnames(self):
        return self.fields

    def __init__(self, sqlstring, fieldnames=[]):
        self.sql = sqlstring
        self.fields = fieldnames

    def printsqlstring(self):
        print(self.sql)

    def printfields(self):
        for field in self.fields:
            print(field)


    def ExecuteSQLCommandNoReturnValue(self):

        con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\BiologyDatabase.mdb;')
        cur = con.cursor()

        try:
            cur.execute(self.sql)
            con.commit()
        except Exception as e:
            print(e)

        cur.close()
        con.close()


    def ExecuteSQLCommandReturnRows(self):

        con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\BiologyDatabase.mdb;')
        cur = con.cursor()

        try:
            rows = cur.execute(self.sql).fetchall()
        except Exception as e:
            print(e)

        cur.close()
        con.close()

        return rows


    def ExecuteSQLCommandReturnDictionaryCollection(self):

        return1 = []

        con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\BiologyDatabase.mdb;')
        cur = con.cursor()

        try:
            rows = cur.execute(self.sql).fetchall()

            # Loop through each row returned
            for row in rows:
                counter = 0
                dict1 = {}

                # Loop through each field in each row and convert to a dictionary
                for item in row:
                    keytext = self.fields[counter]
                    valuetext = item
                    dict1[keytext] = valuetext
                    counter += 1

                # Save as a list of dictionaries
                return1.append(dict1)
        except Exception as e:
            print(e)

        cur.close()
        con.close()

        return return1
