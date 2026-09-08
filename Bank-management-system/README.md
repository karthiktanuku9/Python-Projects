# Bank Management System

A simple command-line project that connects Python to MySQL and performs basic
bank-account operations.

> This is an educational project. Use only dummy information. It is not a real
> banking application.

## Features

- Create an account with a random 8-digit account number
- Deposit money
- Withdraw money after checking the balance
- Check an account balance
- View all accounts in a table
- Delete an account

## Project Structure

```text
bank-management-system/
|-- bank_management.py
|-- requirements.txt
|-- README.md
`-- database/
    `-- schema.sql
```

## Setup on Windows

### 1. Create the database

Open `database/schema.sql` in MySQL Workbench and run the complete script.

You can also open the MySQL command-line client from this project folder:

```powershell
mysql -u root -p
```

Then run:

```sql
SOURCE database/schema.sql;
```

### 2. Install the required packages

```powershell
py -m pip install -r requirements.txt
```

### 3. Run the program

Run it in a terminal because the program needs keyboard input:

```powershell
python bank_management.py
```

The program will ask for your local MySQL password. The password is not stored
in the source code.

## How It Works

1. `connect_db()` connects Python to MySQL.
2. `main()` repeatedly displays the seven-option menu.
3. The selected function runs a SQL command through the cursor.
4. `database.commit()` permanently saves database changes.
5. The cursor and database connection close when the program ends.

### Command Meanings

* `mysql -u root -p` -> Opens the MySQL command-line client using the `root` user and asks for the MySQL password.
Meaning:
mysql -> open the MySQL command-line client.
-u -> specify the username.
root -> your MySQL username.
-p -> ask for your MySQL password

* `SOURCE database/schema.sql;` -> Runs the SQL commands inside `schema.sql`. Enter this command after opening the MySQL client.
Meaning:
SOURCE -> open an SQL file and execute all commands inside it.
database/schema.sql -> location of your schema file.
; -> ends the MySQL command.

* `python -m pip install -r requirements.txt` -> Installs the Python packages listed in `requirements.txt`.
Meaning:
py -> start Python on Windows.
-m pip -> run Python's package installer.
install -> install packages.
-r -> read packages from a file.
requirements.txt -> the file containing your dependencies.

* `python bank_management.py` -> Runs the Bank Management System program.

> On Windows, `py` can be used instead of `python` if the `python` command is unavailable.

### Check for formatting errors
* `python -m py_compile bank_management.py` -> This checks Python syntax without starting the banking menu.If there is no output, the syntax is valid.
