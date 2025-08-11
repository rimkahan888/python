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

print("💸 Transaction function ready - Stage 3 Complete!")