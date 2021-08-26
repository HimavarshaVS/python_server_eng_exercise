import unittest
from .prepare_test import SetUpTest
from .logger import Logger
from app.main import create_app

app = create_app()

default_location_chain_name = "Banana Republic"


class TestAPIlocation(unittest.TestCase):
    log = Logger(name='test_locations_api.log')
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
            "chain": default_location_chain_name,
            "latitude": 31.3643,
            "longitude": -109.477,
            "postal_code": "55033",
            "enabled": "no",
            "phone": "765-239-1273"
        }
        try:
            response = self.app.post("/v1/locations", json=payload)
            self.log.info(f"POST RESPONSE: {response}")
            self.log.info(f"COMPARING: {response.status_code} VS {200}")
            self.assertEqual(response.status_code, 200)
        except Exception as error:
            self.log.error(f"{error}")
            raise error

    def test_02_get_all_locations(self):
        try:
            response = self.app.get("/v1/locations")
            self.log.info(f"GET RESPONSE: {response}")
            self.log.info(f"COMPARING: {response.status_code} VS {200}")
            self.assertEqual(response.status_code, 200)
        except Exception as error:
            self.log.error(f"{error}")
            raise error

    def test_03_delete_location(self):
        try:
            response = self.app.delete(f"/v1/locations/{default_location_chain_name}")
            self.log.info(f"DELETE RESPONSE: {response}")
            self.log.info(f"COMPARING: {response.status_code} VS {200}")
            self.assertEqual(response.status_code, 200)
        except Exception as error:
            self.log.error(f"{error}")
            raise error