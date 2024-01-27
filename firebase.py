import os
import firebase_admin
from firebase_admin import credentials


def init_firebase():
    print(os.getenv("PRIVATE_KEY"))
    cred = credentials.Certificate(
        {
            "type": os.getenv("TYPE"),
            "project_id": os.getenv("PROJECT_ID"),
            "private_key_id": os.getenv("PRIVATE_KEY_ID"),
            "private_key": os.getenv("PRIVATE_KEY"),
            "client_email": os.getenv("CLIENT_EMAIL"),
            "client_id": os.getenv("CLIENT_ID"),
            "auth_uri": os.getenv("AUTH_URI"),
            "token_uri": os.getenv("TOKEN_URI"),
            "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
            "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL"),
        }
    )
    firebase_admin.initialize_app(
        cred,
        {
            "databaseURL": "https://house-crawler-api-2851f-default-rtdb.europe-west1.firebasedatabase.app"
        },
    )
