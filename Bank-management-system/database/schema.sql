CREATE DATABASE IF NOT EXISTS bank_system;

USE bank_system;

CREATE TABLE IF NOT EXISTS bank_accounts (
    account_number INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    city_pin VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50),
    address VARCHAR(255),
    transaction_type VARCHAR(50) DEFAULT '----',
    transaction_amount DECIMAL(10, 2) DEFAULT 0.00,
    balance DECIMAL(10, 2) DEFAULT 0.00,
    transaction_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
