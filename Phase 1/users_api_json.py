import requests
import json

# Fetch data from API
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()

# Save initial users to a JSON file
with open("users.json", "w") as f:
    json.dump(data, f, indent=4)

# Update the city of the first user
data[0]["address"]["city"] = "New City"
with open("users.json", "w") as f:
    json.dump(data, f, indent=4)

print("First user after update:")
print(json.dumps(data[0], indent=4))

# Add a new custom user (you 😊)
karim = {
    "id": 11,
    "name": "Karim",
    "username": "karim123",
    "email": "karim@example.com",
    "address": {
        "street": "123 Main St",
        "suite": "Apt 4B",
        "city": "Algiers",
        "zipcode": "12345"
    },
    "phone": "555-1234",
    "website": "karim.com"
}

data.append(karim)

# Save after adding the new user
with open("users.json", "w") as f:
    json.dump(data, f, indent=4)

# Remove user with id = 5
data = [user for user in data if user["id"] != 5]

with open("users.json", "w") as f:
    json.dump(data, f, indent=4)

print("✅ Users updated, Karim added, and user with id=5 removed.")
