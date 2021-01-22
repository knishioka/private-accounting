import os

import requests


def notify(message):
    """Notify to line.

    Args:
        message (str): message for notification.

    """
    line_token = os.environ["LINE_TOKEN"]
    line_api_url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {line_token}"}
    data = {"message": f"message: {message}"}
    requests.post(line_api_url, headers=headers, data=data)
