def test_query_no_hits_returns_no_answer(client, headers_tenant_a):
    r = client.post("/query", headers=headers_tenant_a, json={"question": "unrelated question"})
    assert r.status_code == 200

    data = r.json()
    assert data["no_answer"] is True
    assert data["answer"] is None
    assert data["sources"] == []
    assert data["reason"] == "No relevant documents for this tenant."


def test_query_hits_returns_sources_for_tenant_a(client, headers_tenant_a):
    r = client.post("/query", headers=headers_tenant_a, json={"question": "resiliation procedure"})
    assert r.status_code == 200

    data = r.json()
    assert data["no_answer"] is False
    assert isinstance(data["answer"], str) and len(data["answer"]) > 0
    assert len(data["sources"]) >= 1
    assert data["sources"][0]["filename"].startswith("a_")


def test_tenant_isolation_same_question_diff_results(client, headers_tenant_a, headers_tenant_b):
    qa = client.post("/query", headers=headers_tenant_a, json={"question": "sinistre procedure"})
    qb = client.post("/query", headers=headers_tenant_b, json={"question": "sinistre procedure"})

    assert qa.status_code == 200
    assert qb.status_code == 200

    a = qa.json()
    b = qb.json()

    # Tenant A should not see tenant B docs for this query in our controlled STORE
    assert a["no_answer"] is True
    assert b["no_answer"] is False
    assert any(src["filename"].startswith("b_") for src in b["sources"])
