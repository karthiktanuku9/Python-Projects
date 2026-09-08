"""Bank management system using Python and MySQL."""
import random

import mysql.connector
from tabulate import tabulate


# Connect Python to the bank_system database.
def connect_db():
    mysql_password = input("Enter your MySQL password: ")

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=mysql_password,
        database="bank_system"
    )


# Read a valid amount from the user.
def read_amount(message):
    while True:
        try:
            amount = float(input(message))
            if amount > 0 :
                return amount
            print("Amount cannot be negative or zero.")
        except ValueError:
            print("Enter a valid number.")


# Read an 8-digit account number.
def read_account_number():
    while True:
        account_number = input("Enter account number: ").strip()
        if account_number.isdigit() and len(account_number) == 8:
            return int(account_number)
        print("Enter a valid 8-digit account number.")


# Create a new bank account.
def create_account(cursor):
    name = input("Enter account holder's name: ").strip()
    balance = read_amount("Enter initial deposit amount: ")

    while True:
        phone_number = input("Enter your 10-digit phone number: ").strip()
        if phone_number.isdigit() and len(phone_number) == 10:
            break
        print("Invalid phone number. Enter exactly 10 digits.")

    city_pin = input("Enter city and pincode (city-pincode): ").strip()
    state = input("Enter state: ").strip()
    country = input("Enter country: ").strip()
    address = input("Enter your house address: ").strip()

    # Keep generating until an unused account number is found.
    while True:
        account_number = random.randint(10000000, 99999999)
        cursor.execute(
            "SELECT account_number FROM bank_accounts WHERE account_number = %s",
            (account_number,),
        )
        if cursor.fetchone() is None:
            break

    cursor.execute(
        """
        INSERT INTO bank_accounts (
            account_number,
            name,
            phone_number,
            address,
            city_pin,
            state,
            country,
            balance
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            account_number,
            name,
            phone_number,
            address,
            city_pin,
            state,
            country,
            balance,
        ),
    )

    print("Account created successfully!")
    print("Your account number is:", account_number)


# Deposit money into an account.
def deposit_money(cursor):
    account_number = read_account_number()
    amount = read_amount("Enter amount to deposit: ")

    cursor.execute(
        """
        UPDATE bank_accounts
        SET balance = balance + %s,
            transaction_type = 'Deposit',
            transaction_amount = %s,
            transaction_timestamp = CURRENT_TIMESTAMP
        WHERE account_number = %s
        """,
        (amount, amount, account_number),
    )

    if cursor.rowcount == 0:
        print("Account not found.")
    else:
        print("Deposit successful!")


# Withdraw money if the account has enough balance.
def withdraw_money(cursor):
    account_number = read_account_number()
    amount = read_amount("Enter amount to withdraw: ")

    cursor.execute(
        "SELECT balance FROM bank_accounts WHERE account_number = %s",
        (account_number,),
    )
    result = cursor.fetchone()

    if result is None:
        print("Account not found.")
    elif float(result[0]) < amount:
        print("Insufficient funds.")
    else:
        cursor.execute(
            """
            UPDATE bank_accounts
            SET balance = balance - %s,
                transaction_type = 'Withdrawal',
                transaction_amount = %s,
                transaction_timestamp = CURRENT_TIMESTAMP
            WHERE account_number = %s
            """,
            (amount, amount, account_number),
        )
        print("Withdrawal successful!")


# Display the balance of one account.
def check_balance(cursor):
    account_number = read_account_number()
    cursor.execute(
        "SELECT balance FROM bank_accounts WHERE account_number = %s",
        (account_number,),
    )
    result = cursor.fetchone()

    if result:
        print("Current balance:", result[0])
    else:
        print("Account not found.")


# Display all accounts in a table.
def view_all_accounts(cursor):
    columns = [
        "Account Number",
        "Name",
        "Phone Number",
        "Address",
        "City-Pin",
        "State",
        "Country",
        "Balance",
        "Last Transaction",
        "Transaction Amount",
        "Transaction Time",
    ]

    cursor.execute(
        """
        SELECT account_number, name, phone_number, address, city_pin,
               state, country, balance, transaction_type,
               transaction_amount, transaction_timestamp
        FROM bank_accounts
        """
    )
    accounts = cursor.fetchall()

    if accounts:
        print(tabulate(accounts, headers=columns, tablefmt="grid"))
    else:
        print("No accounts found.")


# Delete an account after confirmation.
def remove_account(cursor):
    confirmation = input(
        "Are you sure you want to remove your account (y/n)? "
    ).lower()

    if confirmation != "y":
        print("Account deletion cancelled.")
        return

    account_number = read_account_number()
    cursor.execute(
        "DELETE FROM bank_accounts WHERE account_number = %s",
        (account_number,),
    )

    if cursor.rowcount == 0:
        print("Account does not exist.")
    else:
        print("Account deleted.")


def main():
    database = None
    cursor = None

    try:
        database = connect_db()
        cursor = database.cursor()

        while True:
            print("\nBank System Menu:")
            print("1. Create an Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. View All Accounts")
            print("6. Delete Account")
            print("7. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                create_account(cursor)
            elif choice == "2":
                deposit_money(cursor)
            elif choice == "3":
                withdraw_money(cursor)
            elif choice == "4":
                check_balance(cursor)
            elif choice == "5":
                view_all_accounts(cursor)
            elif choice == "6":
                remove_account(cursor)
            elif choice == "7":
                print("Exiting the bank system.")
                break
            else:
                print("Invalid choice. Please try again.")
                continue

            database.commit()

    except mysql.connector.Error as error:
        if database is not None:
            database.rollback()
        print("Database error:", error)
    finally:
        if cursor is not None:
            cursor.close()
        if database is not None and database.is_connected():
            database.close()


if __name__ == "__main__":
    main()
