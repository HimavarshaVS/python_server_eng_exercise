from datetime import datetime

from pydantic import BaseModel


class CreateChains(BaseModel):
    name: str
    image_url: str
    country: str
    online_store: str


class CreateChainsResponse(BaseModel):
    name: str
    image_url: str
    country: str
    online_store: str
    created: datetime
    modified: datetime

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "online_store": "yes",
                "modified": "2021-08-25T12:03:34.672086",
                "image_url": "http://imghost.com/2.jpg",
                "id": 24,
                "country": "US",
                "created": "2021-08-25T12:03:34.672086",
                "name": "Bakers"
            }
        }


class ListAllChains(BaseModel):
    class Config:
        # orm_mode = True
        schema_extra = {
            "example": [
                {
                    "online_store": "no",
                    "modified": "2021-08-25T07:19:36.814125",
                    "image_url": "http://imghost.com/2.jpg",
                    "id": 2,
                    "country": "US",
                    "created": "2021-08-25T07:19:36.814125",
                    "name": "Macy's"
                },
                {
                    "online_store": "no",
                    "modified": "2021-08-25T07:31:42.480281",
                    "image_url": "http://imghost.com/2.jpg",
                    "id": 6,
                    "country": "US",
                    "created": "2021-08-25T07:31:42.480281",
                    "name": "Banana Republic"
                },
                {
                    "online_store": "yes",
                    "modified": "2021-08-25T07:47:40.606184",
                    "image_url": "http://imghost.com/2.jpg",
                    "id": 15,
                    "country": "US",
                    "created": "2021-08-25T07:47:40.606184",
                    "name": "Armani"
                },
                {
                    "online_store": "yes",
                    "modified": "2021-08-25T14:57:48.914217",
                    "image_url": "http://imghost.com/2.jpg",
                    "id": 36,
                    "country": "US",
                    "created": "2021-08-25T14:57:48.914217",
                    "name": "Bakers"
                }
            ]
        }


class ListAllChainsLoc(BaseModel):
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                    "country": "US",
                    "created": "2021-08-25T14:57:48.914217",
                    "name": "Bakers",
                    "online_store": "yes",
                    "modified": "2021-08-25T14:57:48.914217",
                    "image_url": "http://imghost.com/2.jpg",
                    "id": 36,
                    "locations": [
                        {
                            "enabled": "yes",
                            "longitude": -84.6859,
                            "chain": "Bakers",
                            "phone": "739-237-2839",
                            "postal_code": "98144",
                            "latitude": 48.38431
                        },
                        {
                            "enabled": "yes",
                            "longitude": -83.63895,
                            "chain": "Bakers",
                            "phone": "384-927-1283",
                            "postal_code": "48178",
                            "latitude": 41.38534
                        },
                        {
                            "enabled": "no",
                            "longitude": -84.648962,
                            "chain": "Bakers",
                            "phone": "386-391-3284",
                            "postal_code": "11364",
                            "latitude": 32.3953
                        }
                    ]
                }}


class CreateProductPost(BaseModel):
    product: str
    product_url: str
    cost: str
    chains: list


class CreateLocationPost(BaseModel):
    chain: str
    latitude: str
    longitude: str
    postal_code: str
    enabled: str
    phone: str


class ListallProdChains(BaseModel):
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "cost": 19.99,
                "product": "Nike shoes",
                "chains": [
                        {
                            "country": "US",
                            "created": "2021-08-25T14:57:48.914217",
                            "name": "Bakers",
                            "online_store": "yes",
                            "modified": "2021-08-25T14:57:48.914217",
                            "image_url": "http://imghost.com/2.jpg",
                            "id": 36
                        },
                        {
                            "country": "US",
                            "created": "2021-08-25T07:31:42.480281",
                            "name": "Banana Republic",
                            "online_store": "no",
                            "modified": "2021-08-25T07:31:42.480281",
                            "image_url": "http://imghost.com/2.jpg",
                            "id": 6
                        },
                        {
                            "country": "US",
                            "created": "2021-08-25T07:47:40.606184",
                            "name": "Armani",
                            "online_store": "yes",
                            "modified": "2021-08-25T07:47:40.606184",
                            "image_url": "http://imghost.com/2.jpg",
                            "id": 15
                        }
                    ],
                    "product_url": "http://imghost.com/p/1.jpg",
                    "id": 1
                }}
