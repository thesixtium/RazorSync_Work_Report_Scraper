def get_run_report_button_xpath():
    return '//*[@id="root"]/div[2]/div/div/div[3]/div/div[3]/div/div/div[1]/div[2]/div[2]/form/div[12]/button[1]'


def get_username_login_xpath():
    return "/html/body/div[3]/div[2]/div[2]/div/div/div/div/div/form/div/fieldset[1]/span[1]/span/input"


def get_password_login_xpath():
    return "/html/body/div[3]/div[2]/div[2]/div/div/div/div/div/form/div/fieldset[2]/span[1]/span/input"


def get_server_login_xpath():
    return "/html/body/div[3]/div[2]/div[2]/div/div/div/div/div/form/div/fieldset[3]/span[1]/span/input"


def get_log_on_button_xpath():
    return "/html/body/div[3]/div[2]/div[2]/div/div/div/div/div/form/div/div/div/span/input"


def get_try_new_experiance_button_xpath():
    return "/html/body/div[10]/div/div[1]/ul/li[5]/div/button"


def get_run_report_button():
    return "/html/body/div[1]/div[2]/div/div/div[3]/div/div[3]/div/div/div[1]/div[2]/div[2]/form/div[12]/button[1]"

def get_report_window_xpath():
    return "/html/body/div[7]/div/div/div/form"


def get_checkmarks_boxes():
    return [
        "//*[text()='Customer Notes']",
        "//*[text()='Customer Attachments']",
        "//*[text()='Service Request Notes']",
        "//*[text()='Work Orders']",
        "//*[text()='Work Orders Service Items']",
        "//*[text()='Work Orders Service Forms']",
        "//*[text()='Work Orders Attachments']",
        "//*[text()='Customer Balance']",
        "//*[text()='Print']"
    ]
