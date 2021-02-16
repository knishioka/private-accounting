import base64

import boto3


def kms_decrypt(encrypted_txt):
    """Decrypt cipher text.

    Args:
        encrypted_txt (str): text encrypted by kms.

    Returns:
        str: decrypted cipher text.

    """
    client = boto3.client("kms")
    return client.decrypt(CiphertextBlob=base64.b64decode(encrypted_txt))["Plaintext"].decode("utf-8")
