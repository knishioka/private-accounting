import datetime

import firebase_admin
from firebase_admin import firestore


def _connection():
    """Create connection to firebase."""
    if not len(firebase_admin._apps):
        firebase_admin.initialize_app()
    return firestore.client()


def store_bs(bs, attrs={}):
    """Store balance sheet.

    Args:
        bs (dict): balance sheet dict.

    Returns:
        google.cloud.firestore_v1.types.WriteResult

    """
    db = _connection()
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    doc_ref = db.document(f"bs/{today}")

    return doc_ref.set(bs)
