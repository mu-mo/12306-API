from app import app

if __name__ == "__main__":
    port = 3031
    host = "0.0.0.0"
    app.run(host=host, port=port, debug=True)
