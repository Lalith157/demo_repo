import socket

HOST = '127.0.0.1'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        data = conn.recv(4096).decode();
        print(f"\n--- Raw HTTP Request ---\n{data}")
        # Naively parse the request (ignores TE vs Content-Length conflicts)
        if "GET" in data:
            response = "HTTP/1.1 200 OK\r\nContent-Length: 11\r\n\r\nHello World"
            conn.sendall(response.encode())
