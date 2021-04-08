from blog import create_application

app = create_application()
app.debug = True

# set FLASK_APP=
#if __name__ == '__main__':
#    app.run(debug = True)