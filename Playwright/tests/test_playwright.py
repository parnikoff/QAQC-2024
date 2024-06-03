import re
from playwright.sync_api import Page, expect

email = 'gbfyumgumw@vvrgby.rc'
password = '12345'

def test_login_page(page: Page):
    #открываем страницу
    page.goto("https://demo.opencart.com/admin")
    #ждем 5 секунд(5000)
    page.wait_for_load_state('load')
    #ждем элемент "username" по атрибуту placeholder, и дальше применяем метод .fill для заполнения текстом demo 
    page.get_by_placeholder ('Username').fill('demo')
    page.get_by_placeholder ('Password').fill('demo')
    #ищем элемент по роли "кнопка"
    page.get_by_role("button", name= "Login").click()
    page.wait_for_timeout(3000)
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
    
    
def test_registration_page (page: Page):
    page.goto('http://users.bugred.ru')
    page.wait_for_load_state('load')
    page.get_by_text ('Войти').click()
    page.wait_for_load_state('domcontentloaded')
    page.locator("input[name=\"name\"]").fill("Dima")
    page.locator("input[name=\"email\"]").fill(email)
    page.locator("tbody").filter(has_text="Имя Email").locator("input[name=\"password\"]").fill(password)
    page.get_by_role('button',name='Зарегистрироваться').click()
    
def test_auth_page(page: Page): 
    page.goto('http://users.bugred.ru/')
    page.wait_for_load_state('load')
    page.get_by_text('Войти').click()
    page.wait_for_load_state('domcontentloaded')
    page.locator("input[name=\"login\"]").fill(email)
    page.locator("tbody").filter(has_text="Email Пароль Авторизоваться").locator("input[name=\"password\"]").fill(password)  
    page.get_by_role('button', name='Авторизоваться').click()
    page.wait_for_load_state('domcontentloaded')
    expect(page.get_by_role("heading", name="Пользователи")).to_be_visible()
    page.get_by_placeholder("Введите email или имя").fill('Daevy@gmail.com')
    page.get_by_role("button", name= "Найти").click()
    page.get_by_role('link', name= 'Посмотреть').click()
    
    
    
    
    #expect(page.get_by_role("heading", name="Пользователи")).to_be_visible()
    #<a class="btn btn-success" href="/user/admin/view/65eb0ea39f1b66384c8b459c.html">Посмотреть</a>
    
    
    
    
    
    
    
    
   