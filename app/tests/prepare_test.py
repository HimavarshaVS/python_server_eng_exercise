import requests
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import create_app
app = create_app()



class SetUpTest:
    def __init__(self, log):
        self.log = log
        self.app = self.create_test_client()

    def create_test_client(self):
        client = TestClient(app)
        return client

    def get_chain_details(self, chain_name):
        try:
            response = self.app.get(f"/v1/chains/{chain_name}")
            return response
        except Exception as error:
            self.log.info(f"Error while getting chain details: {error}")
            raise error

    def delete_chain_record(self, chain_name):
        try:
            response = self.app.delete(f"/v1/chains/{chain_name}")
            return response
        except Exception as error:
            self.log.info(f"Error while getting chain details: {error}")
            raise error
