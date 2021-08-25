import unittest
from .prepare_test import SetUpTest
from .logger import Logger
from app.main import create_app
app = create_app()

default_chain_name = "Bakers"


def setUpModule():
    _log = Logger(name='test_api.log')
    _test = SetUpTest(_log)
    chain_details_res = _test.get_chain_details(default_chain_name)
    if chain_details_res.status_code == 200:
        _test.delete_chain_record(default_chain_name)


def tearDownModule():
    pass


class TestAPI(unittest.TestCase):
    log = Logger(name='test_chains_api.log')
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
            "name": "Bakers",
            "image_url": "http://imghost.com/2.jpg",
            "country": "US",
            "online_store": "yes"
        }
        try:
            response = self.app.post("/v1/chains", json=payload)
            self.log.info(f"POST RESPONSE: {response}")
            self.log.info(f"COMPARING: {response.status_code} VS {200}")
            self.assertEqual(response.status_code, 200)
        except Exception as error:
            self.log.error(f"{error}")
            raise error

    def test_02_get_chains(self):
        self.log.info("test case 2")
        try:
            response = self.app.get("/v1/chains")
            self.log.info(f"POST RESPONSE: {response}")
            self.log.info(f"COMPARING: {response.status_code} VS {200}")
            self.assertEqual(response.status_code, 200)
        except Exception as error:
            self.log.error(f"{error}")
            raise error

    def test_03_get_chain_locations(self):
        self.log.info("test case 3")
        try:
            response = self.app.get(f"/v1/chains/{default_chain_name}")
            self.log.info(f"POST RESPONSE: {response}")
            self.log.info(f"COMPARING: {response.status_code} VS {200}")
            self.assertEqual(response.status_code, 200)
        except Exception as error:
            self.log.error(f"{error}")
            raise error

    def test_04_delete_chains(self):
        self.log.info("test case 4")
        try:
            response = self.app.delete(f"/v1/chains/{default_chain_name}")
            self.log.info(f"POST RESPONSE: {response}")
            self.log.info(f"COMPARING: {response.status_code} VS {200}")
            self.assertEqual(response.status_code, 200)
        except Exception as error:
            self.log.error(f"{error}")
            raise error
