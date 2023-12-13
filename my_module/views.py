from my_module import app

@app.route('/healthcheck')
def healthcheck():
    return 'Server is healthy!'