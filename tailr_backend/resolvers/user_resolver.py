def resolve_user(id):
    # For simplicity, we'll use a mock dictionary.
    users = {
        1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
        2: {"id": 2, "name": "Bob", "email": "bob@example.com"},
    }
    return users.get(id)
