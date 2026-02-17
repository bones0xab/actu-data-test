import pytest
from fastapi.testclient import TestClient
import app.main as main


@pytest.fixture()
def client(monkeypatch) -> TestClient:
    # Keep tests deterministic: override the global STORE loaded at import time
    main.STORE = {
        "A": [
            {"filename": "a_resiliation.txt", "content": "Procedure resiliation: enregistrer dans le CRM."},
            {"filename": "a_rcpro.txt", "content": "Produit RC Pro A: exclusion travaux hauteur plus de 3 metres."},
        ],
        "B": [
            {"filename": "b_sinistre.txt", "content": "Procedure sinistre: declarer dans les 5 jours ouvrables."},
            {"filename": "b_rcpro.txt", "content": "Produit RC Pro B: exclusion sous-traitance non declaree."},
        ],
    }

    return TestClient(main.app)


@pytest.fixture()
def headers_tenant_a() -> dict:
    return {"X-API-KEY": "tenantA_key", "Content-Type": "application/json"}


@pytest.fixture()
def headers_tenant_b() -> dict:
    return {"X-API-KEY": "tenantB_key", "Content-Type": "application/json"}
