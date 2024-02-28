from azure.cosmos import CosmosClient
import json
import uuid

# Replace these values with your actual Cosmos DB configuration
cosmosdb_endpoint = ""
cosmosdb_key = ""
cosmosdb_database_id = "bank"
cosmosdb_loans_container_id = "loan"

# Initialize Cosmos DB client
client = CosmosClient(cosmosdb_endpoint, cosmosdb_key)

# Get a reference to the database and loans container
database = client.get_database_client(cosmosdb_database_id)
loans_container = database.get_container_client(cosmosdb_loans_container_id)

# Generate loan data
loans_data = [
    {
      "id": "1",
      "loan_id": "L001",
      "loan_type": "Personal Loan",
      "amount": 15000,
      "interest_rate": 8.5,
      "term_months": 24,
      "risk_score": 65
    },
    {
      "id": "2",
      "loan_id": "L002",
      "loan_type": "Auto Loan",
      "amount": 25000,
      "interest_rate": 6.2,
      "term_months": 36,
      "risk_score": 75
    },
    {
      "id": "3",
      "loan_id": "L003",
      "loan_type": "Home Loan",
      "amount": 200000,
      "interest_rate": 4.5,
      "term_months": 240,
      "risk_score": 85
    },
    {
      "id": "4",
      "loan_id": "L004",
      "loan_type": "Education Loan",
      "amount": 30000,
      "interest_rate": 5.8,
      "term_months": 48,
      "risk_score": 70
    },
    {
      "id": "5",
      "loan_id": "L005",
      "loan_type": "Business Loan",
      "amount": 100000,
      "interest_rate": 7.0,
      "term_months": 60,
      "risk_score": 80
    },
    {
      "id": "6",
      "loan_id": "L006",
      "loan_type": "Medical Loan",
      "amount": 20000,
      "interest_rate": 6.5,
      "term_months": 36,
      "risk_score": 72
    },
    {
      "id": "7",
      "loan_id": "L007",
      "loan_type": "Vacation Loan",
      "amount": 8000,
      "interest_rate": 9.2,
      "term_months": 12,
      "risk_score": 68
    },
    {
      "id": "8",
      "loan_id": "L008",
      "loan_type": "Debt Consolidation Loan",
      "amount": 50000,
      "interest_rate": 7.8,
      "term_months": 60,
      "risk_score": 75
    },
    {
      "id": "9",
      "loan_id": "L009",
      "loan_type": "Renovation Loan",
      "amount": 35000,
      "interest_rate": 6.0,
      "term_months": 36,
      "risk_score": 78
    },
    {
      "id": "10",
      "loan_id": "L010",
      "loan_type": "Green Energy Loan",
      "amount": 18000,
      "interest_rate": 5.5,
      "term_months": 24,
      "risk_score": 82
    }
  ]

# Insert loans into Cosmos DB container
for loan in loans_data:
    loans_container.create_item(body=loan)

print("Loans inserted successfully.")
