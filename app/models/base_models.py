from pydantic import BaseModel


class CreateChains(BaseModel):
    name: str
    image_url: str
    country: str
    online_store: str


class CreateChainsResponse(CreateChains):
    class Config:
        schema_extra = {
            "example": [{
                "online_store": "yes",
                "modified": "2021-08-25T12:03:34.672086",
                "image_url": "http://imghost.com/2.jpg",
                "id": 24,
                "country": "US",
                "created": "2021-08-25T12:03:34.672086",
                "name": "Bakers"
            }]
        }

