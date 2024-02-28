# Generating Sample Data
This guide will walk you through the steps required to run the provided Python script locally on your machine. The scripts generate dummy data and insert the records into Azure Cosmos DB to be referenced by Prompt Flow. 

## Create Cosmos DB
1. Create a NoSQL Cosmos DB instance following the directions [here](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/quickstart-portal).
2. You can use 'Serverless' for the consumption mode to easily keep costs down
3. Create a database with a name of 'bank'.
4. Create TWO containers within the database called 'customer' & 'loan'
5. 'customer' container should use '/customer_id' as the Partition Key, and 'loan' should use '/loan_id' as the Partition Key.
6. Once you have these created, simply clone the scripts below and copy your unique URL and Key values into it! 

## Running the Python Script Locally

Before running the script, ensure you have the following prerequisites installed on your machine:

- [Visual Studio Code (VSCode)](https://code.visualstudio.com/download)
- [Python](https://www.python.org/downloads/)
- [Azure Cosmos DB SDK for Python](https://pypi.org/project/azure-cosmos/)
- [Git](https://git-scm.com/downloads)

## Installation

1. **Install Visual Studio Code (VSCode)**

   If you haven't already, download and install Visual Studio Code from the [official website](https://code.visualstudio.com/download).

2. **Install Python**

   Download and install Python from the [official Python website](https://www.python.org/downloads/). Make sure to check the box that adds Python to your system's PATH during installation.

3. **Install Azure Cosmos DB SDK for Python**

   Open a terminal or command prompt and run the following command to install the Azure Cosmos DB SDK for Python: pip install azure-cosmos
    
## Running the Script

1. **Clone the Repository**

Clone this repository to your local machine using Git: git clone <repository_url>

You can also download the files individually by selecting 'download' in the top right corner of the file. 

