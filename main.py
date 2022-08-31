from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)


def send_message(phone_number, text, count):
    try:
        driver.get(url='https://web.whatsapp.com/')
        sleep(60)
        driver.get(url=f'https://web.whatsapp.com/send?phone={phone_number}')
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                          '//*[@id="main"]/footer/div[1]/div/span['
                                                                          '2]/div/div[2]/div[1]/div/div[1]')))

        text_box = driver.find_element(By.XPATH,
                                       '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')

        for _ in range(count):
            text_box.send_keys(text)
            text_box.send_keys('\n')
        # 89671086876
        print(f'Сообщение отправлено {count} раз')
        sleep(5)

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()

    return 'Атака завершена'


def main():
    phone_number = input('Введите номер для атаки: ')
    text = input('Введите текст сообщения: ')
    count = int(input('Сколько сообщений отправить? '))
    send_message(phone_number, text, count)


if __name__ == '__main__':
    main()
