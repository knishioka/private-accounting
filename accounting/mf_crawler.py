import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


def mf_driver():
    """Return logged in driver.

    Returns
         selenium.webdriver.chrome.webdriver.WebDriver

    """
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
    )
    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://id.moneyforward.com/sign_in/email")
        driver.find_element_by_name("mfid_user[email]").send_keys(os.environ["MF_EMAIL"])
        driver.find_element_by_xpath("//input[@type='submit' and @value='同意してログインする']").click()
        driver.find_element_by_name("mfid_user[password]").send_keys(os.environ["MF_PASSWORD"])
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
        "net_asset": driver.find_element_by_css_selector("heading-radius-box-net").text,
    }
