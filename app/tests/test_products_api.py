import unittest
from .prepare_test import SetUpTest
from .logger import Logger
from app.main import create_app

app = create_app()

default_product_name = "Levis Jeans"


class TestAPIlocation(unittest.TestCase):
    log = Logger(name='test_products_api.log')
    test = SetUpTest(log)

    @classmethod
    def setUpClass(cls) -> None:
        cls.log = cls.test.log
        cls.app = cls.test.app
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_01_api(self):
        self.log.info("test case 1")
        payload = {
            "product": default_product_name,
            "product_url": "http://imghost.com/p/3.jpg",
            "cost": 38.11,
            "chains": ["Banana Republic", "Bakers"]}
        try:
            response = self.app.post("/v1/products", json=payload)
            self.log.info(f"POST RESPONSE: {response}")
            self.log.info(f"COMPARING: {response.status_code} VS {200}")
            self.assertEqual(response.status_code, 200)
        except Exception as error:
            self.log.error(f"{error}")
            raise error

    def test_02_get_all_locations(self):
        try:
            response = self.app.get("/v1/products")
            self.log.info(f"GET RESPONSE: {response}")
            self.log.info(f"COMPARING: {response.status_code} VS {200}")
            self.assertEqual(response.status_code, 200)
        except Exception as error:
            self.log.error(f"{error}")
            raise error

    def get_product_associated_chains(self):
        try:
            response = self.app.get(f"/v1/products/{default_product_name}")
            self.log.info(f"GET RESPONSE: {response}")
            self.log.info(f"COMPARING: {response.status_code} VS {200}")
            self.assertEqual(response.status_code, 200)
        except Exception as error:
            self.log.error(f"{error}")
            raise error

    def test_03_delete_location(self):
        try:
            response = self.app.delete(f"/v1/locations/{default_product_name}")
            self.log.info(f"DELETE RESPONSE: {response}")
            self.log.info(f"COMPARING: {response.status_code} VS {200}")
            self.assertEqual(response.status_code, 200)
        except Exception as error:
            self.log.error(f"{error}")
            raise error
