from google.cloud import storage
from datetime import datetime, timedelta

KEYFILE = 'ensai-2025-8f3e0d316c90.json'

def ex_1_bucket():
    # Instantiates a client
    client = storage.Client.from_service_account_json(KEYFILE)

    # The name for the new bucket
    bucket_name = "christophe-dates"

    # Creates the new bucket
    if not client.bucket(bucket_name).exists():
        bucket = client.create_bucket(bucket_name, location="EU")
        print(f"Bucket {bucket.name} created.")
    else:
        bucket = client.get_bucket(bucket_name)
        print(f"Bucket {bucket_name} already exists.")

    start = datetime(2025, 1, 1)
    while start < datetime(2026, 1, 1):
        blob = bucket.blob(f'{start.strftime("%Y-%m-%d")}/')
        blob.upload_from_string('', content_type='application/x-www-form-urlencoded;charset=UTF-8')

        start += timedelta(days=1)

if __name__ == "__main__":
    ex_1_bucket()
