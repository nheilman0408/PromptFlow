from typing import Dict
from promptflow import tool
import json
from azure.cosmos import CosmosClient, exceptions
from promptflow.connections import CustomConnection

cosmosdb_endpoint = ""
cosmosdb_key = ""
cosmosdb_database_id = "bank"
cosmosdb_customer_container_id = "customer"

@tool
def loan_lookup(customer_name: str) -> Dict:
    client = CosmosClient(url=cosmosdb_endpoint, credential=cosmosdb_key)
    db = client.get_database_client(cosmosdb_database_id)
    container = db.get_container_client(cosmosdb_customer_container_id)

    query_text = "SELECT * FROM c WHERE c.name = @name"
    query_result = container.query_items(
        query=query_text,
        parameters=[
            dict(
                name="@name",
                value=customer_name,
            )
        ],
        enable_cross_partition_query=True,
    )

    customerinfo = [item for item in query_result]

    if not customerinfo:
        raise ValueError(f"No document found with name {customer_name} in Cosmos DB.")

    # Assuming you want to return the first item in the list
    customerresponse = customerinfo[0]

    return customerresponse