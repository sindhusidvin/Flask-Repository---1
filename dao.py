import psycopg2

class DataAccessObject:
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    def establish_db_connection(self):
        conn = ""
        cursor = ""
        try:
            conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            cursor = conn.cursor()
        except Exception as err:
            print("Exception occurred", err)
        return [cursor, conn]

    def closing_connection(self):
        cursor, conn = self.establish_db_connection()
        cursor.close()
        conn.close()

    def table_creation(self):
        cursor, conn = self.establish_db_connection()
        query = '''CREATE TABLE employee(FirstName VARCHAR(50),LastName VARCHAR(100), EId INTEGER, UserId VARCHAR(100), password VARCHAR(50),
         MobileNo VARCHAR(15), EmailId VARCHAR(50), DOB VARCHAR(50), Address VARCHAR(50), Gender VARCHAR(10),DOJ VARCHAR(50), Technology VARCHAR(50))'''
        cursor.execute(query)
        conn.commit()
        self.closing_connection()
        return "Table is created"

    def data_insertion(self):
        cursor, conn = self.establish_db_connection()
        records = self.data_frm_service
        query = "INSERT INTO employee_information values(%s, %s, %s, %s)"
        count = 0
        for record in records:
            cursor.execute(query, record)
            count += 1
            print("query executed")
        print("Query executed", count)
        conn.commit()
        print("Table entries inserted")
        self.closing_connection()



def db_ucheck(a1,a2):
    # Get db connection
    # cursor ojbect
    # select query
    # if records == 0: return False
    # else return True
    pass

