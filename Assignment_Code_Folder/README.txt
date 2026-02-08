E-COMMERCE CUSTOMER BEHAVIOR ANALYSIS
====================================

Author: Melvin Abraham  
Course: Data Science, AI & Machine Learning Bootcamp  
Date: February 2026


PROJECT OVERVIEW
----------------
This project analyzes customer transaction data from an e-commerce platform
with the goal of understanding customer behavior, retention patterns, and
revenue drivers.

The analysis was completed using core Python concepts such as dictionaries,
loops, functions, and date handling. No external data analysis libraries
(pandas, numpy, etc.) were used, as this assignment was designed to strengthen
fundamental Python data analysis skills.


DATASET
-------
File used:
- customer_transactions.csv

Each record represents a single customer transaction and includes:
- Customer_ID
- Customer_Name
- Email
- Signup_Date
- Transaction_Date
- Product_Category
- Purchase_Amount
- Payment_Method
- Device


PROJECT STRUCTURE
-----------------
customer_analysis.py
    Main Python script containing all analysis logic and reusable functions.

Customer_Behavior_Analysis.ipynb
    Jupyter Notebook version of the analysis with step-by-step explanations,
    outputs, and insights.

customer_transactions.csv
    Raw transaction data provided for the assignment.

marketing_insights.txt
    Text-based report summarizing key findings and actionable marketing insights.

customer_segments.csv
    Exported customer segmentation data based on spending behavior.

retention_campaign_targets.csv
    List of at-risk customers identified for potential retention campaigns.


ANALYSIS SUMMARY
----------------

Part 1: Customer Database Setup
- Loaded and cleaned transaction data from CSV
- Built customer profiles grouped by Customer_ID
- Calculated total spend and transaction counts per customer
- Generated a high-level customer database summary

Part 2: Purchase Behavior Analysis
- Categorized customers by purchase frequency
- Calculated Customer Lifetime Value (CLV)
- Identified top customers by total spend
- Analyzed product category performance

Part 3: Customer Segmentation
- Segmented customers into VIP, High, Medium, and Low value groups
- Identified customers at risk of churn based on inactivity
- Analyzed loyal customers based on transaction frequency

Part 4: Payment & Device Analytics
- Analyzed preferred payment methods
- Compared average order values across devices
- Identified usage and spending trends by device type

Part 5: Time-Based Patterns
- Grouped transactions by month
- Analyzed monthly transaction volume and revenue
- Calculated customer retention based on repeat purchases

Part 6: Reports & Exports
- Generated a marketing insights report for stakeholders
- Exported customer segments for business use
- Created a retention campaign target list


KEY TAKEAWAYS
-------------
- A small group of high-value customers contributes a large portion of revenue
- Desktop users tend to place higher-value orders than mobile users
- Certain customers show strong loyalty through repeated purchases
- Inactive customers represent a measurable revenue risk that can be addressed
  through targeted retention campaigns


TOOLS & TECHNOLOGIES
--------------------
- Python (csv, datetime, collections)
- Jupyter Notebook
- Visual Studio Code


FINAL NOTE
----------
This project was completed as part of my learning journey in data science.
It helped reinforce how raw transactional data can be transformed into
meaningful business insights using structured logic and clean code.

