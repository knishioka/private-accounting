import os
from tempfile import mkdtemp

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

from .aws import kms_decrypt


def mf_driver():
    """Return logged in driver.

    Returns
         selenium.webdriver.chrome.webdriver.WebDriver

    """
    options = Options()
    options.binary_location = "/opt/chrome/chrome"
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--no-zygote")
    options.add_argument(f"--user-data-dir={mkdtemp()}")
    options.add_argument(f"--data-path={mkdtemp()}")
    options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    options.add_argument("--remote-debugging-port=9222")

    driver = webdriver.Chrome("/opt/chromedriver", chrome_options=options)
    try:
        driver.get("https://id.moneyforward.com/sign_in/email")
        driver.find_element_by_name("mfid_user[email]").send_keys(email())
        driver.find_element_by_xpath("//input[@type='submit' and @value='同意してログインする']").click()
        driver.find_element_by_name("mfid_user[password]").send_keys(password())
        driver.find_element_by_xpath("//input[@type='submit' and @value='ログインする']").click()
        driver.get("https://moneyforward.com/sign_in")
        driver.find_element_by_xpath("//input[@type='submit' and @value='このアカウントを使用する']").click()
    except NoSuchElementException as e:
        print(driver.page_source)
        raise e
    return driver


def get_balance_sheet():
    """Get the latest assets.

    Returns:
        dict: dict with total asset, liability, and net asset.

    """
    driver = mf_driver()
    driver.get("https://moneyforward.com/bs/balance_sheet")
    return {
        "total_asset": driver.find_element_by_css_selector(".heading-radius-box-asset").text,
        "liability": driver.find_element_by_css_selector(".heading-radius-box-liability").text,
        "net_asset": driver.find_element_by_css_selector(".heading-radius-box-net").text,
    }


def email():
    """Get email from an env variable.

    Returns:
        str: mf email.

    """
    if encrypted_line_token := os.environ.get("ENCRYPTED_MF_EMAIL"):
        return kms_decrypt(encrypted_line_token)
    else:
        return os.environ["MF_EMAIL"]


def password():
    """Get password from an env variable.

    Returns:
        str: mf password

    """
    if encrypted_line_token := os.environ.get("ENCRYPTED_MF_PASSWORD"):
        return kms_decrypt(encrypted_line_token)
    else:
        return os.environ["MF_PASSWORD"]
