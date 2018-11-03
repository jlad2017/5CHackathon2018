"""
gathering Pomona College Computer Science Data
"""

# importing libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def get_browser():
    """

    :return:
    """
    # adding incognito to the browser
    option = webdriver.ChromeOptions()
    option.add_argument("incognito")

    # creating an instance of Chrome
    browser = webdriver.Chrome(executable_path="C:/ProgramData/chocolatey/bin/chromedriver.exe", chrome_options=option)

    return browser


def navigate_to_courses(browser):
    # passing in the URL
    url = "http://catalog.pomona.edu/"
    browser.get(url)

    # Wait 20 seconds for page to load
    timeout = 20
    try:
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//select[@name='catalog']")))

    except TimeoutException:
        print("Timed out waiting for page to load")
        browser.quit()

    # finding and clicking on "Courses"
    select_courses = browser.find_elements_by_xpath("//a[contains(text(), 'Courses')]")
    select_courses[1].click()


def select_department(browser, dept):
    """
    Uses the selenium object select the type of

    :param browser: (selenium)
    :param dept: (int) number corresponding to the department in the XPath
    :return:
    """

    # selecting the dropdown menu
    browser.find_element_by_xpath("//*[@id='coursetype']").click()

    # selecting the department
    type_xpath = "//*[@id='coursetype']/option[" + str(dept) + "]"
    browser.find_element_by_xpath(type_xpath).click()

    # clicking the Filter button
    select_filter = browser.find_element_by_xpath("//*[@id='search-with-filters']")
    browser.execute_script("arguments[0].click();", select_filter)


def click_on_courses(browser):
    """

    :param browser:
    :return:
    """
    table = pd.read_html(browser.current_url)

    # gets the number of rows in each table
    row_num = table[7].shape[0]

    for i in range(3, row_num):
        type_xpath1 = "//*[@id='table_block_n2_and_content_wrapper']/table/tbody/tr[2]/td[1]/table/tbody/tr/td/table[2]/tbody/tr[" + str(i) + "]/td[2]/a"
        browser.find_element_by_xpath(type_xpath1).click()

        # makes sure the next element is loaded, it was skipping a couple of courses (trade-off: much slower)
        try:
            WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='table_block_n2_and_content_wrapper']/table/tbody/tr[2]/td[1]/table/tbody/tr/td/table[2]/tbody/tr[" + str(i) + "]/td[2]/table")))

        except TimeoutException:
            print("Timed out waiting for page to load")
            browser.quit()

    return browser.page_source


def get_ids_titles(soup):
    """

    :param soup:
    :return:
    """

    total_course_names = []
    for course in soup.find_all("div", {"class": "ajaxcourseindentfix"}):
        total_course_name = course.find("h3")
        total_course_names.append(total_course_name.text)

    splitted = []
    for course in total_course_names:
        splitted.append(course.split(" - "))

    course_ids = []
    course_titles = []
    for k in range(0, len(splitted)):
        course_ids.append(splitted[k][0])
        course_titles.append(splitted[k][1])

    return [course_ids, course_titles]


def main():
    browser = get_browser()

    navigate_to_courses(browser)

    select_department(browser, 17)

    html = click_on_courses(browser)

    soup = BeautifulSoup(html, features="lxml")

    course_ids_titles = get_ids_titles(soup)
    print(course_ids_titles)


if __name__ == "__main__":
    main()


