import uuid


def new_user():
    """A user body with a name that nobody has used before."""
    name = "lab-" + uuid.uuid4().hex[:12]
    return {"username": name, "password": "Pizza-2026"}


# A second user with a name that is already taken is refused with 400.
def test_username_already_taken(api):
    user = new_user()
    res = api.post("/api/users", json=user)
    assert res.status_code == 201
    res = api.post("/api/users", json=user)
    assert res.status_code == 400
    assert res.json() == {"error": "username already taken"}


# Logging in with a wrong password is refused with 401.
def test_login_with_wrong_password(api):
    user = new_user()
    res = api.post("/api/users", json=user)
    assert res.status_code == 201
    wrong = {"username": user["username"], "password": "Wrong-Password"}
    res = api.post("/api/users/token/login", json=wrong)
    assert res.status_code == 401
    assert res.json() == {"error": "authentication failed"}


# A user with an empty name is refused with 400.
def test_empty_username(api):
    user = {"username": "", "password": "Pizza-2026"}
    res = api.post("/api/users", json=user)
    assert res.status_code == 400
    assert res.json() == {"error": "username field is empty"}