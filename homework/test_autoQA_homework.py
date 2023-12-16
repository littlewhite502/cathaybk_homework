import logging
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Testhomework(): 
  def setup_method(self, method):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation',{'deviceName':'iPhone X'})
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()

  @pytest.mark.cscreenshoot_client_portal
  def test_screenshoot_client_portal(self):
    #設定網址
    self.driver.get("https://www.cathaybk.com.tw/cathaybk/")
    #截圖
    self.driver.save_screenshot('client_portal.png')

  @pytest.mark.calculation_product
  def test_calculation_product(self):
    #設定網址
    self.driver.get("https://www.cathaybk.com.tw/cathaybk/")
    #點擊左上角menu
    WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@class,'cubre-a-burger')]")))
    self.driver.find_element(By.XPATH, "//*[contains(@class,'cubre-a-burger')]").click()
    #點擊產品介紹按鈕
    WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='產品介紹']")))
    self.driver.find_element(By.XPATH, "//*[text()='產品介紹']").click()
    #計算產品數量
    WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='cubre-o-menu__content'][@style='display: block;']")))
    product_elements = self.driver.find_elements(By.XPATH, "//*[@class='cubre-o-menu__content'][@style='display: block;']//*[@class='cubre-a-menuSortBtn']")
    product_count = len(product_elements)
    assert product_count == 5
    print(f"網頁上的產品數量為: {product_count}")
    logging.info("網頁上的產品數量為: %d", product_count)
    self.driver.save_screenshot('client_portal2.png')

  @pytest.mark.calculation_stop_credit_card
  def test_calculation_stop_credit_card(self):
    #設定網址
    self.driver.get("https://www.cathaybk.com.tw/cathaybk/")
    #點擊左上角menu
    WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@class,'cubre-a-burger')]")))
    self.driver.find_element(By.XPATH, "//*[contains(@class,'cubre-a-burger')]").click()
    #點擊產品介紹按鈕
    WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='產品介紹']")))
    self.driver.find_element(By.XPATH, "//*[text()='產品介紹']").click()
    #點擊信用卡按鈕
    WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='信用卡']")))
    self.driver.find_element(By.XPATH, "//*[text()='信用卡']").click()
    #點擊卡片介紹按鈕
    WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='卡片介紹']")))
    self.driver.find_element(By.XPATH, "//*[text()='卡片介紹']").click()
    #點開每一張停用信用卡並且截圖
    stop_credit_card_element = self.driver.find_element(By.XPATH, "//*[@class='cubre-a-iconTitle__text'][text()='停發卡']")
    self.driver.execute_script("arguments[0].scrollIntoView();",stop_credit_card_element)
    WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='cubre-a-iconTitle__text'][text()='停發卡']")))
    stop_credit_card_elements = self.driver.find_elements(By.XPATH, "//*[@class='cubre-a-iconTitle__text'][text()='停發卡']/../../../..//span[contains(@aria-label,'Go to slide')]") 
    #重複點擊停用信用卡直到最後一張停用信用卡
    for i, slide in enumerate(stop_credit_card_elements, start=1):
      slide.click()
      sleep(1) #確認有完整截到圖
      self.driver.save_screenshot(f'stop_credit_card_{i}.png')
    #確認停用信用卡張數與截圖張樹一樣
    stop_credit_card_count = len(stop_credit_card_elements)
    assert i == stop_credit_card_count
    print(f"停發信用卡數量為: {stop_credit_card_count}")
    logging.info("停發信用卡數量為: %d", stop_credit_card_count)


