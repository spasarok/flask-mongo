from api.main import app

@app.route('/stores', methods=['GET', 'POST'])
def stores():
    pass

@app.route('/stores/<int:id>', methods=['GET'])
def store_by_id(id):
    pass
