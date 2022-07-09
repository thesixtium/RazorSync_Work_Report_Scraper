import requests
import json
import re
import credentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import webpage_xpaths
import os.path
import os


def process_result(result):
    replace_and_splice = result[14:].replace('","Id":', ":")
    comma_phone_number = re.sub("[,][\s][0-9]{3}[-][0-9]{3}[-][0-9]{4}", "", replace_and_splice)
    non_comma_phone_number = re.sub("[\s][0-9]{3}[-][0-9]{3}[-][0-9]{4}", "", comma_phone_number)
    return non_comma_phone_number


def get_all_clients():
    result_returns = []

    url = credentials.get_url("/ApiService.svc/Customer/List")

    payload = json.dumps({
        "FromModifiedDate": "/Date(1342705616670)/",
        "ToModifiedDate": "/Date(1654023361136)/"
    })
    headers = {
        'Content-Type': 'application/json',
        'Token': credentials.token(),
        'Host': credentials.host(),
        'Connection': 'Keep-Alive',
        'ServerName': credentials.server_name()
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    for result in re.findall("[D][i][s][p][l][a][y][N][a][m][e][\"][:][\"][^\"]+[\"][,][\"][I][d][\"][:][0-9]+",
                             response.text):
        processed_result = process_result(result)
        result_name = re.findall("^[^:]*", processed_result)
        result_id = re.findall("\:(.*)", processed_result)
        result_returns.append([result_name, result_id])

    return result_returns


def get_all_client_reports(all_clients):
    options = webdriver.ChromeOptions()
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument("--test-type")
    options.binary_location = ""
    driver = webdriver.Chrome(chrome_options=options)

    # Login
    driver.get(credentials.get_login_page())

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, webpage_xpaths.get_username_login_xpath())))
    username_space = driver.find_elements_by_xpath(webpage_xpaths.get_username_login_xpath())[0]
    password_space = driver.find_elements_by_xpath(webpage_xpaths.get_password_login_xpath())[0]
    servername_space = driver.find_elements_by_xpath(webpage_xpaths.get_server_login_xpath())[0]
    logon_button = driver.find_elements_by_xpath(webpage_xpaths.get_log_on_button_xpath())[0]
    login_info = credentials.login_information()

    username_space.send_keys(login_info["user"])
    password_space.send_keys(login_info["password"])
    servername_space.send_keys(login_info["server"])
    logon_button.click()

    # Go to React RazorSync
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, webpage_xpaths.get_try_new_experiance_button_xpath())))
    experience_button = driver.find_elements_by_xpath(webpage_xpaths.get_try_new_experiance_button_xpath())[0]
    experience_button.click()
    time.sleep(5)

    # Get all customer things

    for client in all_clients[0:50]:
        number = client[1][0]
        print(number)
        driver.get(credentials.get_customer_page(number))

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, webpage_xpaths.get_run_report_button_xpath())))
        run_report_button = driver.find_elements_by_xpath(webpage_xpaths.get_run_report_button_xpath())[0]

        customer_id = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div/div/div[3]/div/div[3]/div/div/div[1]/div[2]/div[2]/form/div[4]/div")
        customer_name = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div/div/div[3]/div/div[3]/div/div/div[1]/div[2]/div[2]/form/div[1]/div")

        run_report_button.click()

        check_boxes = webpage_xpaths.get_checkmarks_boxes()

        for box in check_boxes:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, box))
            )
            checkbox = driver.find_elements_by_xpath(box)[0]
            checkbox.click()

        current_file_name = "C:\\Users\\Sixtium\\Downloads\\Customer #" + customer_id[0].text + " Work Report.pdf"
        new_file_name = "C:\\Users\\Sixtium\\Downloads\\" + customer_name[0].text + " Work Report.pdf"

        while not os.path.isfile(current_file_name):
            time.sleep(5)

        os.rename(current_file_name, new_file_name)


def main():
    get_all_client_reports(get_all_clients())


if __name__ == '__main__':
    main()
