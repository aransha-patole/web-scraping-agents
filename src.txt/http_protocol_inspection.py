# src/http_protocol_inspection.py
import requests

r = requests.get("https://example.com")
print(r.status_code)
print(r.headers.get("server"))
