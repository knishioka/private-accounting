import datetime

from accounting.line_notification import notify
from accounting.mf_crawler import get_balance_sheet


def main():
    """Send blance sheet to LINE."""
    bs = get_balance_sheet()
    notify(format_bs(bs))


def format_bs(bs):
    """Format balance sheet dict.

    Args:
        bs (dict): keys are total_asset, liability, and net_asset.

    Returns:
        str: formatted balance sheet with date.

    """
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    bs_values = "\n".join(bs.values())
    return f"{today}\n{bs_values}"


if __name__ == "__main__":
    main()
