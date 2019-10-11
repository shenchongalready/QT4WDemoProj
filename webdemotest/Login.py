# -*- coding: utf-8 -*-
import time

from qt4w.browser import Browser
from webdemolib.demopage import LoginPage, ProfilePage
from webdemolib.testcase import TestCase
from testbase.testcase import debug_run_all

class LoginFail(TestCase):
    '''登录失败
    '''
    owner = "shenchong"
    timeout = 5
    priority = TestCase.EnumPriority.High
    status = TestCase.EnumStatus.Ready

    def run_test(self):
        self.start_step('1. 在浏览器中打开测试页面')
        browser = Browser()
        page = browser.open_url('http://beret-zdh.yiye.ai/#/login', LoginPage)
        
        self.start_step('2. 输入账号密码')
        page.login("csyuedao@qq.com", "1111111")
        time.sleep(3)

        self.start_step('3. 检查页面跳转以及内容是否正确')
        page = ProfilePage(page)
        self.assert_equal('检查用户名', page.control('err_msg').inner_text, '用户名或密码错误')


class LoginOK(TestCase):
    '''登陆成功
    '''
    owner = "shenchong"
    timeout = 5
    priority = TestCase.EnumPriority.High
    status = TestCase.EnumStatus.Ready

    def run_test(self):
        self.start_step('1. 在浏览器中打开测试页面')
        browser = Browser()
        page = browser.open_url('http://beret-zdh.yiye.ai/#/login', LoginPage)

        self.start_step('2. 设置信息并提交')
        page.login("csyuedao@qq.com", "11111111")
        time.sleep(3)

        self.start_step('3. 检查页面跳转以及内容是否正确')
        page = ProfilePage(page)
        self.assert_equal('检查用户名', page.control('用户名').inner_text, '南京悦道网络科技有限公司test')

if __name__ == '__main__':
    # LoginOK().debug_run()
    debug_run_all()