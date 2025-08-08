@app.route('/xss')
def xss_vuln()
    name = request.args.get("name")
    return f"<html><body>Hello {name}</body></html>"  # 🚨 XSS
