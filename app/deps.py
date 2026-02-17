from fastapi import Header, HTTPException

TENANT_KEYS = {
    "tenantA_key": "A",
    "tenantB_key": "B",
}

def get_tenant_id(x_api_key: str = Header(..., alias="X-API-KEY")) -> str:
    tenant_id = TENANT_KEYS.get(x_api_key)
    if not tenant_id:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return tenant_id
