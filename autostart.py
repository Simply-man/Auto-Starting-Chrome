from selenium import webdriver
import json
import time


class AutoStart:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        # Add logged chrome account  
        self.chrome_options.add_argument(r"user-data-dir=YOUR:PATH TO YOUR CHROME FOLDER\Google\Chrome\User Data")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.urls = []
        self.elements = []
        self.func = self.reading_json_file()
        self.count = 0

    def reading_json_file(self):

        with open(r"json.json") as json_file:
            data = json.load(json_file)

            for elements in data['sites']:
                urls = elements['website']
                element = elements['element']
                self.urls.append(urls)
                self.elements.append(element)

                if "jsos" in elements['website']:
                    second_element = elements['second_element']
                    self.elements.append(second_element)

        return self.urls, self.elements

    def open_sites(self):

        for i in range(len(self.func[0])):
            self.driver.execute_script("window.open('about:blank', 'tab{}');".format(i + 1))
            self.driver.switch_to.window("tab{}".format(i + 1))
            self.driver.get(self.urls[i])

    def log_into_email(self):

        self.driver.switch_to.window("tab1")

        items = self.func[1]
        try:
            self.driver.find_element_by_xpath(items[0]).click()
        except Exception as error_email:
            print(f"You are already logged in. If error is different than 'Unable to locate element' you should change\
                your code.\nError from email function detail: {error_email}")

        print("Correctly logged into email!")
        self.count += 1

    def log_into_jsos(self):
        self.driver.switch_to.window("tab2")
        try:
            items = self.func[1]
            href = self.driver.find_elements_by_link_text(items[1])
            time.sleep(1)
            href[0].click()
            time.sleep(1)
            self.driver.find_element_by_name(items[2]).submit()
        except Exception as error_jsos:
            print(f"You are already logged in. If error is different than 'Unable to locate element' you should change\
                            your code.\nError from jsos function detail: {error_jsos}")

        print("Correctly logged into jsos!")
        self.count += 1

    def log_into_studens_email(self):
        self.driver.switch_to.window("tab3")
        try:
            items = self.func[1]
            self.driver.find_element_by_id(items[3]).click()
        except Exception as error_students_email:
            print(f"You are already logged in. If error is different than 'Unable to locate element' you should change\
                your code.\nError from email function detail: {error_students_email}")

        print("Correctly logged into student mail!")
        self.count += 1

    def log_into_edukacjaCL(self):
        self.driver.switch_to.window("tab4")
        try:
            items = self.func[1]
            self.driver.find_element_by_xpath(items[4]).click()
        except Exception as error_edukacja:
            print(f"You are already logged in. If error is different than 'Unable to locate element' you should change\
                            your code.\nError from edukacja function detail: {error_edukacja}")

        print("Correctly logged into EdukacjaCL!")
        self.count += 1

    def running_function(self):
        self.open_sites()
        self.log_into_email()
        self.log_into_jsos()
        self.log_into_studens_email()
        self.log_into_edukacjaCL()

        if self.count == 4:
            print(f"Correctly logged into all sites. Count = {self.count}")
        else:
            print(f"Logged only to {self.count} sites.")


if __name__ == "__main__":
    try:
        driver = AutoStart()
        driver.running_function()
    except Exception as error:
        print(f"Some error occurred: {error}")
