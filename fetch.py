import sys

try:
    import requests
except ImportError:
    print("requests not installed; run: pip install -r requirements.txt")
    sys.exit(1)

resp = requests.get("https://httpbin.org/get", timeout=5)
print(resp.json())
