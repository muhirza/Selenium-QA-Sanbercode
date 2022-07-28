from lib2to3.pgen2 import driver
import os
import unittest
import time
# from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install()) #deklarasi browser
        
    #nama depan def HARUS test
    # menjalankan berdasarkan ABJAD. makanya ada test_a, test_b, dll    
    def test_a_success_login(self): 
        # steps
        # WebElement chooseFile = driver.findElement(By.id("custom-input"));
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div").text
        # response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Sauce', response_data)

    def test_b_failed_login_with_empty_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[3]/h3").text
        # response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Password is required', response_data)


    def test_c_failed_login_with_empty_email_and_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[3]/h3").text
        # response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Username is required', response_data)
        
        
    def test_d_success_logout(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[1]/input").send_keys("m.irza@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[2]/div[2]/input").send_keys("okokokok") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[4]/button").click() # klik tombol sign in
        time.sleep(10)
        browser.find_element(By.XPATH,"/html/body/div/nav/div/div[1]/div/div/div/button").click()
        time.sleep(4)
        browser.find_element(By.XPATH,"/html/body/div/nav/div/div[1]/div/div/div[2]/div/a[5]").click()
        time.sleep(10)
        browser.find_element(By.XPATH,"/html/body/div/section/div[2]/div[4]/button").click() # keluar
        time.sleep(12)

        # validasi
        # browser.get(browser.current_url)
        response_data = browser.find_element(By.XPATH,"/html/body/div/nav/div/div[2]/div[2]/a/button").text
        # response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Masuk', response_data)
        # self.assertEqual(response_message, 'Anda Berhasil Login')

    def test_e_failed_login_with_wrong_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.maximize_window()
        browser.get("https://myappventure.herokuapp.com/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[1]/input").send_keys("m.irza@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[2]/div[2]/input").send_keys("awawawaw") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[4]/button").click() # klik tombol sign in
        time.sleep(5)
        
        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[2]/p").text
        # response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Kata Sandi Salah', response_data)
        # self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def tearDown(self): #close web
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()