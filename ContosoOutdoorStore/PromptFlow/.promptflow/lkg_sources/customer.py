from typing import Dict
from promptflow import tool
import json
from azure.cosmos import CosmosClient, exceptions
from promptflow.connections import CustomConnection

cosmosdb_endpoint = "https://nhaoaicosmos.documents.azure.com:443/"
cosmosdb_key = "HTzi7pws30Njj9qjtWHo75pcCmYR6d5C40Ivj8rqKzXmsVx8CZcoJE1QL8UO6LE8B6tUDcxXZnOtACDbM6zINw=="
cosmosdb_database_id = "contoso"
cosmosdb_customer_container_id = "customers"

@tool
def loan_lookup(customerId: int) -> Dict:
    client = CosmosClient(url=cosmosdb_endpoint, credential=cosmosdb_key)
    #client = CosmosClient(url=conn.configs["endpoint"], credential=conn.secrets["key"])
    db = client.get_database_client(cosmosdb_database_id)
    container = db.get_container_client(cosmosdb_customer_container_id)

    query_text = "SELECT * FROM c WHERE c.customerId = @customerId"
    query_result = container.query_items(
        query=query_text,
        parameters=[
            dict(
                name="@customerId",
                value=customerId,
            )
        ],
        enable_cross_partition_query=True,
    )

    customerinfo = [item for item in query_result]

    if not customerinfo:
        raise ValueError(f"No document found with name {customerId} in Cosmos DB.")

    # Assuming you want to return the first item in the list
    customerresponse = customerinfo[0]

    return customerresponse