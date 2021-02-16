import os
import shutil
import sys

from accounting.firebase import store_bs
from accounting.formatter import format_bs
from accounting.line_notification import notify
from accounting.mf_crawler import get_balance_sheet


def move_bin(fname: str, src_dir: str = "/var/task/bin", dest_dir: str = "/tmp/bin") -> None:
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    dest_file = os.path.join(dest_dir, fname)
    shutil.copy2(os.path.join(src_dir, fname), dest_file)
    os.chmod(dest_file, 0o775)


def handler(event, context):
    """Send blance sheet to LINE."""
    move_bin("headless-chromium")
    move_bin("chromedriver")

    bs = get_balance_sheet()

    if os.environ.get("GOOGLE_APPLICATION_CREDENTIALS") is not None:
        store_bs(bs)
    else:
        sys.stderr.write("GOOGLE_APPLICATION_CREDENTIAL doesn't exist. Skipped setting firestore.\n")

    notify(format_bs(bs))
