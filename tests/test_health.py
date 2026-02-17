def test_health_ok(client):
    r = client.get("/health")
    assert r.status_code == 200

    data = r.json()
    assert data["ok"] is True
    assert "docs" in data
    assert data["docs"]["A"] == 2
    assert data["docs"]["B"] == 2
