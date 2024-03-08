from azure.cosmos import CosmosClient, PartitionKey

# Initialize the Cosmos client
endpoint = "your_cosmos_db_endpoint"
key = "your_cosmos_db_key"
client = CosmosClient(endpoint, key)

# Define your database and container
database_name = "contoso"
container_name = "customers"

# Create a database if it doesn't exist
database = client.create_database_if_not_exists(id=database_name)

# Create a container if it doesn't exist
container = database.create_container_if_not_exists(
    id=container_name,
    partition_key=PartitionKey(path="/customerId")
)

# Define your records
records = [
    {"id":"1", "customerId": 1, "firstName": "John", "lastName": "Smith", "age": 35, "email": "johnsmith@example.com",
     "phone": "555-123-4567", "address": "123 Main St, Anytown USA, 12345", "membership": ""},
    {"id":"2", "customerId": 2, "firstName": "Jane", "lastName": "Doe", "age": 28, "email": "janedoe@example.com",
     "phone": "555-987-6543", "address": "456 Oak St, Another City USA, 67890", "membership": "Gold"},
    {"id":"3", "customerId": 3, "firstName": "Michael", "lastName": "Johnson", "age": 45, "email": "michaelj@example.com",
     "phone": "555-555-1212", "address": "789 Elm St, Smallville USA, 34567", "membership": ""},
    {"id":"4", "customerId": 4, "firstName": "Sarah", "lastName": "Lee", "age": 38, "email": "sarahlee@example.com",
     "phone": "555-867-5309", "address": "321 Maple St, Bigtown USA, 90123", "membership": "Platinum"},
    {"id":"5", "customerId": 5, "firstName": "David", "lastName": "Kim", "age": 42, "email": "davidkim@example.com",
     "phone": "555-555-5555", "address": "654 Pine St, Suburbia USA, 23456", "membership": "Gold"},
    {"id":"6", "customerId": 6, "firstName": "Emily", "lastName": "Rodriguez", "age": 29, "email": "emilyr@example.com",
     "phone": "555-111-2222", "address": "987 Oak Ave, Cityville USA, 56789", "membership": ""},
    {"id":"7", "customerId": 7, "firstName": "Jason", "lastName": "Brown", "age": 50, "email": "jasonbrown@example.com",
     "phone": "555-222-3333", "address": "456 Cedar Rd, Anytown USA, 12345", "membership": ""},
    {"id":"8", "customerId": 8, "firstName": "Melissa", "lastName": "Davis", "age": 31, "email": "melissad@example.com",
     "phone": "555-333-4444", "address": "789 Ash St, Another City USA, 67890", "membership": "Gold"},
    {"id":"9", "customerId": 9, "firstName": "Daniel", "lastName": "Wilson", "age": 47, "email": "danielw@example.com",
     "phone": "555-444-5555", "address": "321 Birch Ln, Smallville USA, 34567", "membership": ""},
    {"id":"10", "customerId": 10, "firstName": "Amanda", "lastName": "Perez", "age": 26, "email": "amandap@example.com",
     "phone": "555-123-4567", "address": "654 Pine St, Suburbia USA, 23456", "membership": "Gold"},
    {"id":"11", "customerId": 11, "firstName": "Robert", "lastName": "Johnson", "age": 36, "email": "robertj@example.com",
     "phone": "555-555-1212", "address": "123 Main St, Anytown USA, 12345", "membership": ""},
    {"id":"12", "customerId": 12, "firstName": "Karen", "lastName": "Williams", "age": 29, "email": "karenw@example.com",
     "phone": "555-987-6543", "address": "456 Oak St, Another City USA, 67890", "membership": "Gold"}
]

# Upload records to the container
for record in records:
    container.create_item(body=record)

print("Records uploaded successfully.")
