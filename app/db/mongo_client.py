import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.environ.get("MONGO_URI")

client = pymongo.MongoClient(MONGO_URI)
#  host: Optional[Union[str, Sequence[str]]] = None,
# port: Optional[int] = None,
# document_class: Optional[Type[_DocumentType]] = None,
# tz_aware: Optional[bool] = None,
# connect: Optional[bool] = None,
# type_registry: Optional[TypeRegistry] = None,
db = client.get_database("db_name")
