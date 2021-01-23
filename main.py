import os
import sys

from accounting.firebase import store_bs
from accounting.formatter import format_bs
from accounting.line_notification import notify
from accounting.mf_crawler import get_balance_sheet


def main():
    """Send blance sheet to LINE."""
    bs = get_balance_sheet()

    if os.environ.get("GOOGLE_APPLICATION_CREDENTIALS") is not None:
        store_bs(bs)
    else:
        sys.stderr("GOOGLE_APPLICATION_CREDENTIAL doesn't exist. Skipped setting firestore.")

    notify(format_bs(bs))


if __name__ == "__main__":
    main()
