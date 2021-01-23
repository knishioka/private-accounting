import datetime


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
