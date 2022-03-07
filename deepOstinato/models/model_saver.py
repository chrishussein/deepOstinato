import joblib
from google.cloud import storage

STORAGE_LOCATION = "models/testing/model.joblib"
BUCKET_NAME = "deep_ostinato"

def upload_model_to_gcp(bucket_name=BUCKET_NAME, storage_location=STORAGE_LOCATION):
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(storage_location)
        blob.upload_from_filename('model.joblib')

def save_model(model, bucket_name=BUCKET_NAME, storage_location=STORAGE_LOCATION):
        """method that saves the model into a .joblib file and uploads it on Google Storage /models folder
        HINTS : use joblib library and google-cloud-storage"""

        joblib.dump(model, 'model.joblib')
        upload_model_to_gcp(bucket_name, storage_location)
