import requests


class FileClient:
    def __init__(self, base_url="http://localhost:8910"):
        self.base_url = base_url

    def store_file(self, file_id, file_data):
        """Store a file on the server"""
        try:
            response = requests.post(
                f"{self.base_url}/store",
                json={"file_id": file_id, "file_data": file_data},
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error storing file: {e}")
            return None

    def retrieve_file(self, file_id):
        """Retrieve a file from the server"""
        try:
            response = requests.get(f"{self.base_url}/retrieve/{file_id}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving file: {e}")
            return None


def main():
    client = FileClient()

    # Test storing a file
    print("Storing file...")
    result = client.store_file("test_file_1", "This is test data for the file")
    if result:
        print(f"Store result: {result}")

    # Test retrieving the file
    print("\nRetrieving file...")
    result = client.retrieve_file("test_file_1")
    if result:
        print(f"Retrieve result: {result}")


if __name__ == "__main__":
    main()
