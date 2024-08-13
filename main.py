from website import create_app

app = create_app()

if __name__ == '__main__':   # only run our app if this file is ran first
    app.run(debug=True)    # run our flask application and start up webserver

