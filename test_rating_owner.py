# Another user must not read, change or delete a rating that is not theirs.

def owner_still_has_rating(api, auth, rating):
    """Read the rating as its owner and check that nothing changed."""
    res = api.get(f"/api/ratings/{rating['id']}", headers=auth)
    assert res.status_code == 200
    assert res.json() == rating


# The other user cannot read the rating.
def test_other_user_cannot_read(api, auth, other_auth, rating):
    res = api.get(f"/api/ratings/{rating['id']}", headers=other_auth)
    print("READ status:", res.status_code, res.text)
    assert 400 <= res.status_code <= 499
    owner_still_has_rating(api, auth, rating)


# The other user cannot change the rating.
def test_other_user_cannot_update(api, auth, other_auth, rating):
    res = api.put(f"/api/ratings/{rating['id']}", json={"stars": 1}, headers=other_auth)
    print("UPDATE status:", res.status_code, res.text)
    assert 400 <= res.status_code <= 499
    owner_still_has_rating(api, auth, rating)


# The other user cannot delete the rating.
def test_other_user_cannot_delete(api, auth, other_auth, rating):
    res = api.delete(f"/api/ratings/{rating['id']}", headers=other_auth)
    print("DELETE status:", res.status_code, res.text)
    assert 400 <= res.status_code <= 499
    owner_still_has_rating(api, auth, rating)