import os
import shutil
import uuid

# Function to check if the filename starts with a UUID
def is_uuid_start(filename):
    try:
        uuid_part = filename.split('.')[0]  # Assuming UUID is the first part of the filename, separated by '_'
        uuid.UUID(uuid_part)  # Try to convert the first part to a UUID
        return True
    except ValueError:
        return False

# Function to move images that start with a UUID and aren't in the list of given UUIDs
def move_images_to_course_directory(image_directory, excluded_uuids, destination_directory):
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)  # Create the destination directory if it doesn't exist

    # Get the list of all files in the image directory
    for filename in os.listdir(image_directory):
        if os.path.isfile(os.path.join(image_directory, filename)) and is_uuid_start(filename):
            uuid_part = filename.split('.')[0]
            if uuid_part not in excluded_uuids:
                source = os.path.join(image_directory, filename)
                destination = os.path.join(destination_directory, filename)
                shutil.move(source, destination)  # Move the file
                print(f"Moved: {filename}")

# List of UUIDs to exclude
excluded_uuids = [
    "a3ae724e-9cc1-4325-bb92-4d442b11de69",
    "b28e1e19-a3ef-47d1-b737-a361a54692bc",
    "a8e2a03a-a6c4-4cfd-b52d-63d8c72455e7",
    "3174b224-06d7-4e5f-9a4b-196ad0d619db",
    "56f052a0-f96d-4847-8123-c486f8edad5b",
    "2a73ec7a-64fa-4e1a-a8b6-ef5a546df75f",
    "83d70056-b5b6-492e-ae8b-f4fc1d52f477",
    "1c573a27-a91a-4e63-9dba-53eec84be5ae",
    "9e6b3b81-c123-49ba-9677-c4efd8fe02f6",
    "80392782-dfd2-4787-a9a3-567364ea0cbe",
    "1c8b8375-f5f1-4539-82c2-75395f261981",
    "56cd9378-81bb-4452-b6ec-2f7117eadfe0",
    "c4954a62-2a03-4c2f-8547-df3a5832c093",
    "fa00517b-1042-4b9c-b4ff-5bcac2c160bc",
    "38fe8f4a-8411-46d9-b94f-f2c357d4fe29",
    "86746e33-5710-4898-a516-8a6b6870bc6a",
    "ea084567-f492-4888-a467-7ad4eeea0ae7",
    "d3b04ca0-b7e0-4599-b86c-85f993d145ea",
    "849d4127-5978-4191-b329-4d4f9b16081f",
    "42595fa8-26d3-475b-abe9-9dbe719def4f",
    "02c94fb2-ca4f-40c4-b1a9-7cae35f76aa1",
    "68736bff-f66b-442a-836e-bf6af767f86e",
    "4037cb81-fd7a-472b-bb08-00071454c5b6",
    "1055a874-1f6f-4657-826a-e3b7458d63ce",
    "c0c56560-5927-4d40-9cd0-cb95e412a061",
    "5ad3e8f7-577d-484e-a645-7569bed2cb22",
    "5f7d8f8a-f30c-4604-ac28-ee48d2b72528",
    "d53086ed-b0e8-4515-b9f0-6d5eebf0cc40",
    "ad9aeda1-5df9-4485-983c-02046ff5610e",
    "8557d347-6515-4cd0-9366-ff6b92c0c93d"
]

# Example usage:
image_directory = '.'  # Current working directory
destination_directory = 'course_images'  # Directory where images will be moved

move_images_to_course_directory(image_directory, excluded_uuids, destination_directory)
