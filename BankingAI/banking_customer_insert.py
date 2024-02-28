from azure.cosmos import CosmosClient
import uuid
import random
import names
import json

# Replace these values with your actual Cosmos DB configuration
cosmosdb_endpoint = ""
cosmosdb_key = ""
cosmosdb_database_id = "bank"
cosmosdb_container_id = "customer"

# Define a list of valid loan IDs that the bank offers
valid_loan_ids = ["L001", "L002", "L003", "L004", "L005", "L006", "L007", "L008", "L009", "L010"]

# Initialize Cosmos DB client
client = CosmosClient(cosmosdb_endpoint, cosmosdb_key)

# Get a reference to the database and container
database = client.get_database_client(cosmosdb_database_id)
container = database.get_container_client(cosmosdb_container_id)

# Generate and insert 500 unique customers with valid loan IDs
customers = []
for i in range(1, 501):
    customer_id = str(uuid.uuid4())
    name = names.get_full_name()
    loan_id = random.choice(valid_loan_ids)
    credit_score = random.randint(600, 850)
    income = random.randint(30000, 120000)
    outstanding_balance = random.randint(0, 50000)

    customer = {
        "id": str(i),
        "customer_id": customer_id,
        "name": name,
        "loan_id": loan_id,
        "credit_score": credit_score,
        "income": income,
        "outstanding_balance": outstanding_balance
    }

    customers.append(customer)

# Insert customers into Cosmos DB container
for customer in customers:
    container.create_item(body=customer)

print("Customers inserted successfully.")
