import csv

def read_csv(filename):
    """Read data from a CSV file."""
    try:
        with open(filename, mode='r') as file:
            data = list(csv.DictReader(file))
            return data
    except FileNotFoundError:
        return []

def validate_login(username, password, filename):
    """Validate login credentials against a CSV file."""
    users = read_csv(filename)
    for user in users:
        if user['username'] == username and user['password'] == password:
            return True
    print(f"Login failed for {username}.")  # Debugging line
    return False
