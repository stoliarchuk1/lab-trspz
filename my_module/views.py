from my_module import app

@app.route('/')
def healthcheck():
    return 'Server is healthy!'
    
@app.route('/healthcheck')
def healthcheck():
    return 'Server is healthy!'
