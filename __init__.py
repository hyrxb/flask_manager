from app import app, config

if __name__ == "__main__":
    app.run(host=config.read("HOST"), port=int(config.read(
        "PORT")), debug=config.read("DEBUG"))
