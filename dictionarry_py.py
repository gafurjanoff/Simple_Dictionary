import mysql.connector


class mydictionary():
       db = "longman_dictionary"
       table ="en_uz"

       def __init__(self):
              self.conn = mysql.connector.connect(
              host="localhost",
              user="root",
              password="Saman_dar77"
              )
              self.__create_database()
              self.__create_table()

       def __create_database(self):
              self.conn.cursor().execute(f"CREATE DATABASE IF NOT EXISTS {self.db}")
              self.conn.cursor().execute(f"USE {self.db}")

       def __create_table(self):
              self.conn.cursor().execute(f"""CREATE TABLE IF NOT EXISTS {self.table}(
              ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
              UZB varchar(64),
              ENG varchar(64)
              );""")

       def add_words(self, en, uz):
              
              query = f"""INSERT INTO {self.table} (UZB,ENG) values ("{uz}", "{en}")"""
              self.conn.cursor().execute(query)
              self.conn.commit()

       def get_all(self):
              
              cursor = self.conn.cursor()
              cursor.execute(f"SELECT ENG, UZB FROM {self.table} ORDER BY UZB ASC")
              a = cursor.fetchall()
              return a
    
       def search(self , uz):
              
              cursor = self.conn.cursor()
              cursor.execute(f"SELECT ENG FROM {self.table} WHERE UZB = '{uz}'")
              a = cursor.fetchall()
              for i in a:
                  f = list(i)
                  return f[0]  
        
       def search_2(self, en):
           
              cursor = self.conn.cursor()
              cursor.execute(f"""SELECT UZB FROM {self.table} WHERE ENG = '{en}' """)
              a = cursor.fetchall()
              for i in a:
                  f = list(i)
                  return f[0] 
              
              
              
            
if __name__ == "__main__" :
       d = mydictionary()

