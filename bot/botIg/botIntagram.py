#Observação : é necessário ter o fire fox instalado para rodar o bot

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class instagramBot:
    def __init__(self,username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\gusta\OneDrive\Área de Trabalho\bot\geckodriver\geckodriver.exe')

   

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        time.sleep(3)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.like_photos('programacao') #aqui deve ser passado o nome da hashtag dentro dos parentese para curtir os assuntos

    def like_photos(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(6)
        i = 1
        while i < 3: # numero de paginas que irá decer . "pode ser mudado no while(i < numero de paginas a decer)"
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            break
        
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [element.get_attribute('href') for element in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' fotos: ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_xpath('//button[@class="dCJp8 afkep"]').click()
                time.sleep(20)
            
            except Exception as e:
                time.sleep(5)


myBot = instagramBot('seuNoneDeUsuario','SuaSenha')  # aqui coloque seu login (usuario e senha)
myBot.login()
