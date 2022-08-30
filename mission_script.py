from xmlrpc import client
import random
from tqdm import tqdm

url = 'http://localhost:8069'
db = 'space'
username = password = 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

uid = common.authenticate(db, username, password, {})

mission_fields = models.execute_kw(db, uid, password,
        'space.spaceship', 'fields_get',
        [], {'attributes': ['string', 'type', 'required']})

for x in tqdm(range(73415, 100000)):
    width = random.randint(1,10000)
    length = random.randint(width, 10001)
    models.execute(db, uid, password,
            'space.spaceship', 'create',
            [
                {
                    'name': f"wadam ship #{x}",
                    'description': 'one of my many ships!',
                    'length': length,
                    'width': width,
                    'passengers': random.randint(1,1000),
                    'active': bool(random.getrandbits(1))
                }
            ]
            )
