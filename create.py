import psycopg2
import datetime

class Create:
    def func_CreateData(self):
        
        conn = psycopg2.connect(
        host="127.0.0.1",
        database='Project-Test',
        user='postgres',
        password='123qw123'
        )
        
        season = input('Enter season= ')
        start_date= input('Enter Start Date (dd-dd-yyyy); ')
        year, month, day = map(int, start_date.split('-'))
        start_date=datetime.date(year,month,day)
        end_date= input('Enter End Date (mm-dd-yyyy): ')
        year, month, day = map(int, end_date.split('-'))
        end_date=datetime.date(year,month,day)
        try:
            cursor = conn.cursor()
            QUERY="INSERT INTO seasons VALUES (%s,%s,%s);"
            DATA=(season,start_date,end_date)
            cursor.execute(QUERY,DATA)
            
            print("Data was suscessfully inserted")
            conn.commit()

        except:
            print("OPS, something went wrong. Please check the data")

        finally:
            conn.close()