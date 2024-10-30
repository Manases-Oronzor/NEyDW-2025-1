import requests

# GET request
response = requests.get('http://127.0.0.1:5000/api')
print(response.json())

# POST request
data = {"name": "John"}
response = requests.post('http://127.0.0.1:5000/api', json=data)
print(response.json())

# PUT request
updated_data = {"name": "John"}
response = requests.put('http://127.0.0.1:5000/api', json=updated_data)
print(response.json())

# DELETE request
response = requests.delete('http://127.0.0.1:5000/api')

if response.status_code == 204:
    print("Data deleted successfully!")
else:
    print(f"Failed to delete data. Status code: {response.status_code}")

