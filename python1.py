#!/usr/bin/env python3
"""
Personal Finance Tracker
A simple application to track income, expenses, and savings
"""

import json
import datetime
from typing import Dict, List

print("💰 Personal Finance Tracker - Stage 1 Complete!")

# Add this after Stage 1

# Global variables to store financial data
finance_data = {
    "transactions": [],
    "categories": ["Food", "Transportation", "Entertainment", "Bills", "Shopping", "Income"],
    "balance": 0.0
}

print("📊 Data structures initialized - Stage 2 Complete!")

# Add this after Stage 2

def add_transaction(amount: float, category: str, description: str, transaction_type: str):
    """Add a new transaction (income or expense)"""
    transaction = {
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "amount": amount,
        "category": category,
        "description": description,
        "type": transaction_type  # 'income' or 'expense'
    }
    finance_data["transactions"].append(transaction)
    
    if transaction_type == "income":
        finance_data["balance"] += amount
    else:
        finance_data["balance"] -= amount
    
    print(f"✅ Transaction added: {transaction_type} of ${amount}")

# Add this after Stage 3

def display_balance():
    """Display current balance and summary"""
    print(f"\n💰 Current Balance: ${finance_data['balance']:.2f}")
    
    total_income = sum(t['amount'] for t in finance_data['transactions'] if t['type'] == 'income')
    total_expenses = sum(t['amount'] for t in finance_data['transactions'] if t['type'] == 'expense')
    
    print(f"📈 Total Income: ${total_income:.2f}")
    print(f"📉 Total Expenses: ${total_expenses:.2f}")
    print(f"📊 Net Savings: ${total_income - total_expenses:.2f}")

# Add this after Stage 4

def view_transactions(limit: int = 10):
    """Display recent transactions"""
    print(f"\n📝 Recent Transactions (Last {limit}):")
    print("-" * 60)
    
    recent_transactions = finance_data["transactions"][-limit:]
    
    for transaction in recent_transactions:
        symbol = "➕" if transaction["type"] == "income" else "➖"
        print(f"{symbol} {transaction['date']} | ${transaction['amount']:.2f} | {transaction['category']} | {transaction['description']}")
    
    if not recent_transactions:
        print("No transactions found.")

# Add this after Stage 5

def analyze_by_category():
    """Analyze spending by category"""
    print("\n📊 Spending Analysis by Category:")
    print("-" * 40)
    
    category_totals = {}
    
    for transaction in finance_data["transactions"]:
        if transaction["type"] == "expense":
            category = transaction["category"]
            category_totals[category] = category_totals.get(category, 0) + transaction["amount"]
    
    for category, total in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
        print(f"🏷️  {category}: ${total:.2f}")
    
    if not category_totals:
        print("No expense data available.")

# Add this after Stage 6

def save_data(filename: str = "finance_data.json"):
    """Save financial data to JSON file"""
    try:
        with open(filename, 'w') as file:
            json.dump(finance_data, file, indent=2)
        print(f"💾 Data saved to {filename}")
    except Exception as e:
        print(f"❌ Error saving data: {e}")

# Add this after Stage 7

def load_data(filename: str = "finance_data.json"):
    """Load financial data from JSON file"""
    global finance_data
    try:
        with open(filename, 'r') as file:
            finance_data = json.load(file)
        print(f"📂 Data loaded from {filename}")
    except FileNotFoundError:
        print(f"📁 No existing data file found. Starting fresh.")
    except Exception as e:
        print(f"❌ Error loading data: {e}")

# Add this after Stage 8

def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("💰 PERSONAL FINANCE TRACKER")
    print("="*50)
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View Transactions")
    print("5. Category Analysis")
    print("6. Save Data")
    print("7. Load Data")
    print("8. Exit")
    print("-"*50)

def get_user_choice():
    """Get user menu choice"""
    try:
        choice = int(input("Enter your choice (1-8): "))
        return choice
    except ValueError:
        print("❌ Please enter a valid number.")
        return None

print("🎯 Menu system ready - Stage 9 Complete!")

print("📂 Load function ready - Stage 8 Complete!")

print("👀 Transaction viewer ready - Stage 5 Complete!")