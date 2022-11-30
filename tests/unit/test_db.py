import unittest
from shop_app import db, product, auth

class TestApplication(unittest.TestCase):
    def test_db_conf(self):
        self.assertIsInstance(db.get_db_config(), dict)

    def test_get_deb(self):
        self.assertTrue(db.get_db)

    def test_init_app(self):
        self.assertTrue(db.init_app)

    def test_include_column_names(self):
        self.assertTrue(product.include_column_names)

    def test_index(self):
        self.assertTrue(product.index)

    def test_logout(self):
        self.assertTrue(auth.logout)

    def test_load_logges_in_user(self):
        self.assertTrue(auth.load_logged_in_user)

    def test_register(self):
        self.assertTrue(auth.register)
