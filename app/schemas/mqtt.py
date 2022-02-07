from http import client
from pydoc_data.topics import topics
import pydantic
import gmqtt.client


class Mqtt(pydantic.BaseModel, gmqtt.client.Subscription):
    pass
