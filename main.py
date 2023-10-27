#from read import Read
from create import Create
#from update import Update
#from delete import Delete
import psycopg2

import pandas as pd

conn = psycopg2.connect(
    host="127.0.0.1",
    database='Project-Test',
    user='postgres',
    password='123qw123'
)


def main():
    print('Available Options: C=Create, R=Read, U=Update, D=Delete ')
    choice = input('Choose your option = ')

    if choice == 'C':
        createObj=Create()
        createObj.func_CreateData()
    else:
        print('Wrong choice, You are going exist.')


# Call the main function
main()