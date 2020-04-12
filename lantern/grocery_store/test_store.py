import inject

from store_app import app
from fake_storage import FakeStorage


def configure_test(binder):
    db = FakeStorage()
    binder.bind('DB', db)


class Initializer:
    def setup(self):
        inject.clear_and_configure(configure_test)

        app.config['TESTING'] = True
        with app.test_client() as client:
            self.client = client


class TestUsers(Initializer):
    def test_create_new(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe', 'user_id': 1}
        )
        assert resp.status_code == 201
        assert resp.json == {'user_id': 1}

        resp = self.client.post(
            '/users',
            json={'name': 'Andrew Derkach'}
        )
        assert resp.json == {'user_id': 2}

    def test_successful_get_user(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        user_id = resp.json['user_id']
        resp = self.client.get(f'/users/{user_id}')
        assert resp.status_code == 200
        assert resp.json == {'name': 'John Doe'}

    def test_get_unexistent_user(self):
        resp = self.client.get(f'/users/1')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 1'}

    def test_succesfull_update_user(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        # user_id = resp.json['user_id']
        resp = self.client.put(
            '/users/1',
            json={'name': 'Johanna Doe'}
        )
        assert resp.status_code == 200
        assert resp.json == {'status': 'success'}

    def test_unexistent_update_user(self):
        resp = self.client.put(
            f'/users/1',
            json={'name': 'Johanna Doe'}
        )
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 1'}


class TestGoods(Initializer):
    def test_create_new(self):
        resp = self.client.post(
            '/goods',
            json={'name': 'Chocolate_bar', 'price': '10', 'id': '1'}
        )
        assert resp.status_code == 201
        assert resp.json == {'good_id': 1}

        resp = self.client.post(
            '/goods',
            json={'name': 'Rice', 'price': '15', 'id': '2'}
        )
        assert resp.status_code == 201
        assert resp.json == {'good_id': 2}

    def test_successful_get_good(self):
        resp = self.client.post(
            '/goods',
            json={'name': 'Chocolate_bar', 'price': '10', 'id': '1'}
        )
        goods_id = resp.json['good_id']
        resp = self.client.get(f'/goods/{goods_id}')
        assert resp.status_code == 200

    def test_succesfull_update_goods(self):
        resp = self.client.post(
            '/goods',
            json={'name': 'Chocolate_bar', 'price': 10, 'id': 1}
        )
        resp = self.client.put(
            '/goods',
            json={'name': 'Chocolate_bar', 'price': 11, 'id': 1}
        )
        assert resp.status_code == 200
        assert resp.json == ({'successfully_updated': 1,
                              'errors': {'no such id in goods': []}})


class TestStores(Initializer):
    def test_create_new(self):
        resp = self.client.post(
            '/stores',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 2}
        )
        assert resp.status_code == 201
        assert resp.json == {'stores_id': 1}

    def test_successful_get_stores(self):
        resp = self.client.post(
            '/stores',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 2}
        )
        stores_id = resp.json['stores_id']
        resp = self.client.get(f'/stores/{stores_id}')
        assert resp.status_code == 200
        assert resp.json == {'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 2}

    def test_get_unexistent_store(self):
        resp = self.client.get(f'/store/3')
        assert resp.status_code == 404

    def test_succesfull_update_stores(self):
        resp = self.client.post(
            '/stores',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 2}
        )
        resp = self.client.put(
            '/stores/1',
            json={'name': 'Local Taste', 'location': 'Lviv', 'manager_id': 2}
        )

        assert resp.status_code == 200
        assert resp.json == {'status': 'success'}

    def test_unsuccesfull_update_stores(self):
        resp = self.client.get(f'/store/3')
        assert resp.status_code == 404
