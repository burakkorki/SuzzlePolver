from selenium import webdriver
import os


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(os.path.abspath(os.curdir)+'/chromedriver 78',options=chrome_options)

browser.get('https://www.nytimes.com/crosswords/game/mini')
browser.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div/main/div[2]/div/div[2]/div[3]/div/article/div[2]/button/div/span')[0].click()
browser.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div/main/div[2]/div/div/ul/div[2]/li[2]/button')[0].click()
browser.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div/main/div[2]/div/div/ul/div[2]/li[2]/ul/li[3]/a')[0].click()
browser.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[2]/article/div[2]/button[2]/div/span')[0].click()
browser.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[2]/span')[0].click()

clues_across = list()
clues_down = list()

clues_across = browser.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div/main/div[2]/div/article/section[2]/div[1]/ol')[0].text.split('\n')
clues_down = browser.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div/main/div[2]/div/article/section[2]/div[2]/ol')[0].text.split('\n')

#print("Across Clues\n",clues_across)
#print("Down Clues\n",clues_down)

solutions = []


for i in range(25):
    css_link = '#xwd-board > g:nth-child(5) > g:nth-child('+str(i+1)+')'
    #print(css_link)
    if not browser.find_elements_by_css_selector(css_link):
        solutions.append('')
    else:
        solutions.append(browser.find_elements_by_css_selector(css_link)[0].text.split("\n"))

#print("Solutions\n",solutions)  # Solutions are listed as increasing order from left to right and top to down                                                      
output = open("output.txt",'w')
output.writelines(str(clues_across))
output.write('\n')
output.writelines(str(clues_down))
output.write('\n')
output.writelines(str(solutions))
output.write('\n')
output.close()
browser.quit()

