from flask import Flask, jsonify, request

import inject


class NoSuchUserError(Exception):
    def __init__(self, user_id):
        self.message = f'No such user_id {user_id}'


class NoSuchGoodsError(Exception):
    def __init__(self, user_id):
        self.message = f'No such goods_id {goods_id}'


class NoSuchStoresID(Exception):
    def __init__(self, store_id):
        self.message = f'No such store_id {store_id}'


class NoSuchManagerID(Exception):
    def __init__(self, manager_id):
        self.message = f'No such manager_id {manager_id}'


app = Flask(__name__)


@app.errorhandler(NoSuchUserError)
def my_error_handler(e):
    return jsonify({'error': e.message}), 404


@app.errorhandler(NoSuchGoodsError)
def my_error_handler(e):
    return jsonify({'error': e.message}), 404


@app.errorhandler(NoSuchStoresID)
def my_error_handler(e):
    return jsonify({'error': e.message}), 404


@app.errorhandler(NoSuchManagerID)
def my_error_handler(e):
    return jsonify({'error': e.message}), 404


@app.route('/users', methods=['POST'])
def create_user():
    db = inject.instance('DB')
    user_id = db.users.add(request.json)
    return jsonify({'user_id': user_id}), 201


@app.route('/users/<int:user_id>')
def get_user(user_id):
    db = inject.instance('DB')
    user = db.users.get_user_by_id(user_id)
    return jsonify(user)


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    db = inject.instance('DB')
    db.users.update_user_by_id(user_id, request.json)
    return jsonify({'status': 'success'})


@app.route('/goods', methods=['POST'])
def create_good():
    db = inject.instance('DB')
    user_id = db.goods.add(request.json)
    return jsonify({'good_id': user_id}), 201


@app.route('/goods/<int:good_id>')
def get_good(good_id):
    db = inject.instance('DB')
    good = db.goods.get_good_by_id(good_id)
    return jsonify(good)


@app.route('/goods', methods=['PUT'])
def update_good():
    db = inject.instance('DB')
    new = db.goods.update_goods(request.json)
    return jsonify({'successfully_updated': new[0],
                    'errors': {'no such id in goods': new[1]}}), 200


@app.route('/stores', methods=['POST'])
def create_stores():
    db = inject.instance('DB')
    id = db.stores.add(request.json)
    return jsonify({'stores_id': id}), 201


@app.route('/stores/<int:stores_id>')
def get_stores(stores_id):
    db = inject.instance('DB')
    stores = db.stores.get_stores_by_id(stores_id)
    return jsonify(stores)


@app.route('/stores/<int:stores_id>', methods=['PUT'])
def update_store(stores_id):
    db = inject.instance('DB')
    db.stores.update_stores(request.json, stores_id)
    return jsonify({'status': 'success'}), 200



