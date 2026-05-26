from http.server import HTTPServer, SimpleHTTPRequestHandler

if __name__ == "__main__":
    print("Serving on http://localhost:8000")
    HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler).serve_forever()
