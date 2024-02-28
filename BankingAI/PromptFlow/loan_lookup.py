from typing import Dict
from promptflow import tool
import json
from azure.cosmos import CosmosClient, exceptions
#from promptflow.connections import CustomConnection

cosmosdb_endpoint = ""
cosmosdb_key = ""
cosmosdb_database_id = "bank"
cosmosdb_loans_container_id = "loan"

@tool
def loan_lookup(loan_id: str) -> Dict:
    client = CosmosClient(url=cosmosdb_endpoint, credential=cosmosdb_key)
    db = client.get_database_client(cosmosdb_database_id)
    container = db.get_container_client(cosmosdb_loans_container_id)

    query_text = "SELECT * FROM c WHERE c.id = @loanid"
    query_result = container.query_items(
        query=query_text,
        parameters=[
            dict(
                name="@loanid",
                value=loan_id,
            )
        ],
        enable_cross_partition_query=True,
    )

    loaninfo = [item for item in query_result]

    if not loaninfo:
        raise ValueError(f"No document found with loan_id {loan_id} in Cosmos DB.")

    # Assuming you want to return the first item in the list
    loanresponse = loaninfo[0]

    return loanresponse