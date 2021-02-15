import os

import requests

from .aws import kms_decrypt


def notify(message):
    """Notify to line.

    Args:
        message (str): message for notification.

    """
    if encrypted_line_token := os.environ.get("ENCRYPTED_LINE_TOKEN"):
        line_token = kms_decrypt(encrypted_line_token)
    else:
        line_token = os.environ["LINE_TOKEN"]
    line_api_url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {line_token}"}
    data = {"message": f"message: {message}"}
    requests.post(line_api_url, headers=headers, data=data)
