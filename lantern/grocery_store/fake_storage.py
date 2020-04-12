from itertools import count
from store_app import NoSuchUserError, NoSuchGoodsError, NoSuchStoresID, NoSuchManagerID


class FakeStorage:
    def __init__(self):
        self._users = FakeUsers()
        self._goods = FakeGoods()
        self._stores = FakeStores()

    @property
    def users(self):
        return self._users

    @property
    def goods(self):
        return self._goods

    @property
    def stores(self):
        return self._stores

class FakeUsers:
    def __init__(self):
        self._users = {}
        self._id_counter = count(1)

    def add(self, user):
        user_id = next(self._id_counter)
        self._users[user_id] = user
        return user_id

    def get_user_by_id(self, user_id):
        try:
            return self._users[user_id]
        except KeyError:
            raise NoSuchUserError(user_id)

    def update_user_by_id(self, user_id, user):
        if user_id in self._users:
            self._users[user_id] = user
        else:
            raise NoSuchUserError(user_id)


class FakeGoods:
    def __init__(self):
        self._goods = {}
        self._id_counter = count(1)

    def add(self, good):
        goods_id = next(self._id_counter)
        self._goods[goods_id] = good
        return goods_id

    def get_good_by_id(self, good_id):
        try:
            return self._goods[good_id]
        except KeyError:
            raise NoSuchUserError(good_id)

    def update_goods(self, goods):
        no_id = []
        upd = 0
        g_key = self._goods.items()
        for x, y in g_key:
            if goods['id'] == y.get('id'):
                y = goods
                upd += 1
            elif goods['id'] != y.get('id'):
                no_id.append(goods['id'])
        return upd, no_id


class FakeStores:
    def __init__(self):
        self._stores = {}
        self._id_counter = count(1)

    def add(self, stores):
        stores_id = next(self._id_counter)
        self._stores[stores_id] = stores
        return stores_id

    def get_stores_by_id(self, stores_id):
        try:
            return self._stores[stores_id]
        except KeyError:
            raise NoSuchStoresID(stores_id)

    def update_stores(self, stores, stores_id):
        if stores_id in self._stores:
            self._stores[stores_id] = stores
        else:
            return NoSuchStoresID(stores['stores_id'])


