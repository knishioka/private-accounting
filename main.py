from accounting.formatter import format_bs
from accounting.line_notification import notify
from accounting.mf_crawler import get_balance_sheet


def main():
    """Send blance sheet to LINE."""
    bs = get_balance_sheet()
    notify(format_bs(bs))


if __name__ == "__main__":
    main()
