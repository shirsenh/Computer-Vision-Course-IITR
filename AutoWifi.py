import sched,time
from selenium import webdriver
s = sched.scheduler(time.time, time.sleep)

def mainfunction(sc):
	driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
	driver.get('https://1.1.1.1/login.html')

	try: 
		username = driver.find_element_by_name('username')
		username.click()
		username.clear()
		username.send_keys('govind')
		password = driver.find_element_by_name('password')
		password.click()
		password.clear()
		password.send_keys('Govind@123')	
		button = driver.find_element_by_name('Submit')
		button.click()
		print('done')

	except Exception as e:
		print('Exception')
	s.enter(1800, 1, mainfunction, (sc,))
	driver.close()
s.enter(0, 1, mainfunction, (s,))
s.run()
