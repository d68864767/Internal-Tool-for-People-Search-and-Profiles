# data_ingestion.py

import requests
from models import db, Profile
from config import DevelopmentConfig

def ingest_data():
    # Fetch data from the data warehouse
    response = requests.get(DevelopmentConfig.DATA_WAREHOUSE_URL)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Iterate over the data and create Profile objects
        for item in data:
            profile = Profile(
                id=item['id'],
                name=item['name'],
                description=item['description'],
                image_url=item['image_url'],
                other_data=item['other_data']
            )

            # Add the profile to the session
            db.session.add(profile)

        # Commit the session to save the changes
        db.session.commit()

    else:
        print(f"Failed to fetch data from the data warehouse. Status code: {response.status_code}")

if __name__ == "__main__":
    ingest_data()
