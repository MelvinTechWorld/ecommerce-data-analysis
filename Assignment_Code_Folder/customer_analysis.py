"""
E-Commerce Customer Behavior Analysis
Name: Melvin Abraham
Date: 2026-02-08
"""

import csv
from datetime import datetime


def load_transaction_data(filename):
    """
    Load transaction data from CSV and perform basic cleaning.
    """
    transactions = []

    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                if not row["Customer_ID"] or not row["Purchase_Amount"]:
                    continue

                transaction = {
                    "customer_id": row["Customer_ID"].strip(),
                    "name": row["Customer_Name"].strip(),
                    "email": row["Email"].strip(),
                    "signup_date": datetime.strptime(row["Signup_Date"], "%Y-%m-%d"),
                    "transaction_date": datetime.strptime(row["Transaction_Date"], "%Y-%m-%d"),
                    "category": row["Product_Category"].strip(),
                    "amount": float(row["Purchase_Amount"]),
                    "payment_method": row["Payment_Method"].strip(),
                    "device": row["Device"].strip()
                }

                transactions.append(transaction)

            except (ValueError, KeyError):
                continue

    return transactions


def build_customer_profiles(transactions):
    """
    Group transactions by customer and build profiles.
    """
    profiles = {}

    for txn in transactions:
        cid = txn["customer_id"]

        if cid not in profiles:
            profiles[cid] = {
                "customer_id": cid,
                "name": txn["name"],
                "email": txn["email"],
                "signup_date": txn["signup_date"],
                "total_transactions": 0,
                "total_spent": 0.0,
                "transactions": []
            }

        profiles[cid]["transactions"].append(txn)
        profiles[cid]["total_transactions"] += 1
        profiles[cid]["total_spent"] += txn["amount"]

    return profiles


def display_customer_summary(customer_profiles):
    """
    Display overall customer summary statistics.
    """
    total_customers = len(customer_profiles)

    total_transactions = sum(
        p["total_transactions"] for p in customer_profiles.values()
    )

    total_revenue = sum(
        p["total_spent"] for p in customer_profiles.values()
    )

    avg_transactions = total_transactions / total_customers
    avg_spend = total_revenue / total_customers

    most_active = max(
        customer_profiles.values(),
        key=lambda p: p["total_transactions"]
    )

    highest_spender = max(
        customer_profiles.values(),
        key=lambda p: p["total_spent"]
    )

    print("\nCUSTOMER DATABASE SUMMARY")
    print("=" * 30)
    print(f"Total Customers: {total_customers}")
    print(f"Average Transactions per Customer: {avg_transactions:.2f}")
    print(f"Average Customer Lifetime Value: ${avg_spend:.2f}")
    print(
        f"Most Active Customer: {most_active['customer_id']} "
        f"({most_active['total_transactions']} transactions)"
    )
    print(
        f"Highest Spending Customer: {highest_spender['customer_id']} "
        f"(${highest_spender['total_spent']:.2f})"
    )


if __name__ == "__main__":
    transactions = load_transaction_data("customer_transactions.csv")

    if transactions:
        profiles = build_customer_profiles(transactions)
        display_customer_summary(profiles)
    else:
        print("No transaction data loaded.")
