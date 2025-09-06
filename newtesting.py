import os;

app= --main__;
def send_request_to_service(data):
    # VULNERABILITY: hardcoded API key (sensitive secret stored in code)
    API_KEY = "AKIAEXAMPLEHARDCODEDKEY123456"  # <-- vulnerable line
    # pretend we use the key to build an Authorization header
    headers = {"Authorization": f"Bearer {API_KEY}"}
    # simulate request (no network call)
    return {"status": "ok", "sent_headers": headers, "data": data}

if __name__ == "__main__":
    resp = send_request_to_service({"hello": "world"})
    print("Response:", resp)
