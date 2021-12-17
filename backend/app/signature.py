import base64
import io

from config.models import SiteConfiguration
from Cryptodome.Hash import SHA
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import PKCS1_v1_5


def create_signature(message=""):
    config = SiteConfiguration.get_solo()
    keystream = io.BytesIO(config.private_key.encode("utf-8"))
    pub_key = RSA.importKey(keystream.read(), None)
    data_hash = SHA.new(message.encode("utf-8"))
    _signer = PKCS1_v1_5.new(pub_key)
    return base64.b64encode(_signer.sign(data_hash))
