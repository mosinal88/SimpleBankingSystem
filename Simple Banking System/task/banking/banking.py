# Write your code here
import random
import sqlite3
import sys

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS '
            'card(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
            ' number TEXT,'
            ' pin TEXT,'
            ' balance INTEGER DEFAULT 0)')
conn.commit()


class Card:

    def __init__(self):
        self.card_number = '0'
        self.pin = 0
        self.operation = 0
        self.user_id = 0

    def main_menu(self):
        while True:
            print('1. Create an account')
            print('2. Log into account')
            print('0. Exit')

            self.operation = int(input('>'))

            if self.operation == 0:
                print('Bye!')
                sys.exit(0)
            elif self.operation == 1:
                self.create_card()
            elif self.operation == 2:
                self.login_card()

    def create_card(self):
        print('Your card has been created')
        iin = random.randint(100000000, 999999999)
        number_summa = 0
        self.card_number = '400000' + str(iin)
        i = 1
        for number in self.card_number:
            if i % 2 != 0:
                number_summa += int(number) * 2
                if int(number) * 2 > 9:
                    number_summa -= 9
            else:
                number_summa += int(number)
            i += 1
        check_card = 10 - (number_summa % 10)
        if check_card == 10:
            check_card = 0
        self.card_number = '400000' + str(iin) + str(check_card)
        self.pin = random.randint(1000, 9999)
        print('Your card number:')
        print(self.card_number)
        print('Your card PIN:')
        print(self.pin)
        cur.execute('INSERT INTO card (number, pin) VALUES (?, ?)', (self.card_number, self.pin))
        conn.commit()

    def login_card(self):
        print('Enter your card number:')
        user_card = input('>')
        print('Enter your PIN:')
        user_pin = input('>')
        cur.execute('SELECT COUNT(*) FROM card WHERE number = ' + user_card + ' AND pin = ' + user_pin)
        if cur.fetchone()[0] == 1:
            print('You have successfully logged in!')
            cur.execute('SELECT id FROM card WHERE number = ' + user_card + ' AND pin = ' + user_pin)
            self.user_id = cur.fetchone()[0]
            self.user_menu()
        else:
            print('Wrong card number or PIN!')

    def user_menu(self):
        while True:
            print('1. Balance')
            print('2. Add income')
            print('3. Do transfer')
            print('4. Close account')
            print('5. Log out')
            print('0. Exit')

            self.operation = int(input('>'))

            if self.operation == 0:
                sys.exit(0)
            elif self.operation == 1:
                cur.execute('SELECT balance FROM card WHERE id = ?', (self.user_id,))
                print('Balance: {}'.format(cur.fetchone()[0]))
            elif self.operation == 2:
                self.add_income()
            elif self.operation == 3:
                self.do_transfer()
            elif self.operation == 4:
                self.close_account()
            elif self.operation == 5:
                self.main_menu()

    def add_income(self):
        print('Enter income:')
        summa = int(input('>'))
        cur.execute('UPDATE card SET balance = balance + ? WHERE id = ?', (summa, self.user_id))
        conn.commit()
        print('Income was added!')
        self.user_menu()

    def do_transfer(self):
        print('Transfer')
        print('Enter card number:')
        transfer_card = input('>')
        i = 1
        number_summa = 0
        for number in transfer_card:
            if i % 2 != 0 and i != 16:
                number_summa += int(number) * 2
                if int(number) * 2 > 9:
                    number_summa -= 9
            else:
                number_summa += int(number)
            i += 1
        if (number_summa % 10) != 0:
            print('Probably you made a mistake in the card number. Please try again!')
            self.user_menu()
        else:
            cur.execute('SELECT COUNT(*) FROM card WHERE number = ?', (transfer_card,))
            if cur.fetchone()[0] == 1:
                print('Enter how much money you want to transfer:')
                transfer_summa = int(input('>'))
                cur.execute('SELECT balance FROM card WHERE id = ?', (self.user_id,))
                if cur.fetchone()[0] >= transfer_summa:
                    cur.execute('UPDATE card SET balance = balance - ? WHERE id = ?', (transfer_summa, self.user_id))
                    cur.execute('UPDATE card SET balance = balance + ? '
                                'WHERE number = ?', (transfer_summa, transfer_card))
                    conn.commit()
                    print('Success!')
                    self.user_menu()
                else:
                    print('Not enough money!')
                    self.user_menu()
            else:
                print('Such a card does not exist.')

    def close_account(self):
        cur.execute('DELETE FROM card WHERE id = ?', (self.user_id,))
        conn.commit()
        print('The account has been closed!')
        self.user_menu()


user_operation = Card()
user_operation.main_menu()
conn.close()
