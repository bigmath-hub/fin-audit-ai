import kaggle
import os

# Authenticate (this usually happens automatically if kaggle.json is in place)
# kaggle.api.authenticate() # Uncomment if explicit authentication is needed

# Define the dataset identifier (e.g., 'user/dataset_name')
dataset_identifier = 'mlg-ulb/creditcardfraud' # Example dataset

# Define the download path
download_path = './data'

# Create the directory if it doesn't exist
os.makedirs(download_path, exist_ok=True)

# Download and unzip the dataset
kaggle.api.dataset_download_files(dataset_identifier, path=download_path, unzip=True)

print(f"Dataset '{dataset_identifier}' downloaded and unzipped to '{download_path}'")