def test_invalid_api_key_returns_401(client):
    r = client.post(
        "/query",
        headers={"X-API-KEY": "wrong_key", "Content-Type": "application/json"},
        json={"question": "anything"},
    )
    assert r.status_code == 401
    data = r.json()
    assert data["detail"] == "Invalid API key"
