# -*- coding: utf-8 -*-

'''demo页面封装
'''

from qt4w import XPath
from qt4w.webcontrols import WebPage, WebElement, InputElement, SelectElement
from qt4c.keyboard import Keyboard


class LoginPage(WebPage):
    '''Demo页面
    '''
    ui_map = {
        'username': {'type': InputElement, 'locator': XPath('//*[@id="app"]/div/div[2]/div/div[2]/form/div[1]/div/div/input')},
        'password': {'type': InputElement,'locator': XPath('//*[@id="app"]/div/div[2]/div/div[2]/form/div[2]/div/div/input')},
        'login': XPath('//*[@id="app"]/div/div[2]/div/div[2]/form/button'),
    }

    def set_username(self, username):
        '''输入用户名
        '''
        self.control('username').value = username

    def set_password(self, password):
        '''输入密码
        '''
        self.control('password').value = password

    def submit(self):
        '''点击登录
        '''
        self.control('login').click()

    def login(self, username, password):
        self.control('username').value = username
        self.control('password').value = password
        self.control('login').click()

# class LandingPage(WebPage):
#     '''落地页页面
#     '''
#     ui_map = {
#         ''
#     }
#     def
#
# class DataPage(WebPage):
#     '''数据页面
#     '''
#     ui_map = {
#         ''
#     }
#     def

class ProfilePage(WebPage):
    '''个人资料页
    '''
    ui_map = {
        '用户名': XPath('//*[@id="home-container"]/div[2]/div[2]/span/span[1]'),
        'err_msg': XPath('/html/body/div[3]/div/p')
    }
