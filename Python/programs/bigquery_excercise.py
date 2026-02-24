#from google.cloud import bigquery
from google.oauth2 import service_account

"""
from google.colab import drive
drive.mount("/content/drive")
%cd /content/drive/My Drive/Colab Notebooks/
"""

fkey_file = "g:/My Drive/Data Analyst/Python/data/kodreepython-cbbfcf2b2498.json"

# Set the path to your service account key
credentials = service_account.Credentials.from_service_account_file(fkey_file)
crd = service_account.Credentials.from_service_account_file(fkey_file)


from google.cloud import bigquery

client = bigquery.Client()

dataset_ref = client.dataset("DA", project="data-analytics-mate")
table_ref = dataset_ref.table("session_params")

try:
    client.get_table(table_ref)
    print("Table exists")
except Exception as e:
    print("Table does NOT exist or no access")
    print(e)


# Initialize the BigQuery client
project_id = "kodreepython"
client = bigquery.Client(credentials=crd, project=project_id)

# Define your SQL query
query = """
    SELECT *
    FROM `data-analytics-mate.DA.session_params`
    LIMIT 10
"""

# Run the query and fetch results
query_job = client.query(query)

# Get the result as a dataframe
results = query_job.to_dataframe()

# Print the results
print(results)
