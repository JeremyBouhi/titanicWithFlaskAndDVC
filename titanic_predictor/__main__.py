from web.server import Server

if __name__ == "__main__":
    app = Server().bootstrap()
    app.run()
