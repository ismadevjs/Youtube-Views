from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from random import randrange
from random import choice
import pyautogui
import time
import random
import httpagentparser
import math
import os
def run_vpn():
    os.system(r'"C:\Program Files\NordVPN\NordVPN.exe" -c')
    progress_message = "Delay in progress: {} seconds remaining."
    for remaining_seconds in range(10, 0, -1):
        print(progress_message.format(remaining_seconds))
        time.sleep(1)  # Delay execution for 1 second

    print("Delay complete. This message will be printed in the terminal.")

# functions
def userAgent(file):
    with open(file, "r") as f:
        lines = f.readlines()
        return random.choice(lines)


def goto(linenum):
    global line
    line = linenum


def user_agent_detect():
    user_agent = UserAgent()
    random_user_agent = user_agent.random
    return random_user_agent


print(httpagentparser.simple_detect(user_agent_detect())[1])


if (
    httpagentparser.simple_detect(user_agent_detect())[0] == "Unknown OS"
    or "Microsoft Internet Explorer"
    not in httpagentparser.simple_detect(user_agent_detect())[1]
    or httpagentparser.simple_detect(user_agent_detect())[0] == "Windows Vista"
):
    user_agent_detect()

windows = "false"
randtrue = random.randrange(2)
print(randtrue)
if randtrue == 1:
    windows = "true"


# run nordVPN
run_vpn()

# arguments
chrome_options = Options()
chrome_options.add_argument(f"user-agent={user_agent_detect()}")
chrome_options.add_argument("--mute-audio")
if windows == "true":
    chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])


browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get("http://youtube.com/")

time.sleep(3)

# functions


def timeCalc(val):
    tm = val.split(":")
    if len(tm) == 2:
        resultat = int(tm[0]) * 60
        resultat = resultat + int(tm[1])
        return resultat
    if len(tm) == 3:
        resultat = int(tm[0]) * 3600
        resultat = resultat + (int(tm[1]) * 60)
        resultat = resultat + int(tm[2])
        return resultat


def elem_f(valeur):
    return WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.XPATH, valeur))
    )


def r_scroll():
    browser.execute_script(
        "window.scrollTo({ top: " + str(randrange(2000)) + ", behavior: 'smooth' })"
    )
    time.sleep(4)


def mouseControl(elm):
    location = elm.location
    size = elm.size
    absolute_x = location["x"] + size["width"] - 25
    absolute_y = location["y"] + size["height"] + 65
    pyautogui.moveTo(absolute_x, absolute_y, duration=0.5)
    time.sleep(1.5)


def click_on_current_youtube_channel():
    return


time.sleep(3)

try:
    pasteXpath = "//*[@id='return-to-youtube']"
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, pasteXpath))
    )
    mouseControl(element)
    pyautogui.click()
except:
    print("not found")


aggrements = elem_f(
    '//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button'
)

if aggrements:
    # Get the size of the browser window
    mouseControl(aggrements)
    pyautogui.click()

try:
    aggrements_mobile = browser.find_element(
        By.CSS_SELECTOR,
        "body > div.consent-bump-v2-lightbox > ytm-consent-bump-v2-renderer > div > div.dialog-scrollable-content > div.one-col-dialog-buttons > ytm-button-renderer.eom-accept > button",
    )
    # Get the size of the browser window
    mouseControl(aggrements_mobile)
    pyautogui.click()
except:
    print("not mobile")
# Move the mouse to the element

time.sleep(3)

search = browser.find_element(By.NAME, "search_query")
if search:
    mouseControl(search)
    pyautogui.click()
    search_text = "hicham aboud"
    for letter in search_text:
        search.send_keys(letter)
        time.sleep(0.3)

# go to search and type
searchBtn = browser.find_element(By.ID, "search-icon-legacy")
if searchBtn:
    time.sleep(3)
    mouseControl(searchBtn)
    pyautogui.click()

time.sleep(3)

# click on channel profile

profile = WebDriverWait(browser, 20).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="avatar-section"]/a'))
)
if profile:
    mouseControl(profile)
    pyautogui.click()

time.sleep(3)
list_videos = []


def channel_func():
    time.sleep(3)

    # click on video tab
    videoTab = browser.find_element(
        By.XPATH, '//*[@id="tabsContent"]/tp-yt-paper-tab[2]'
    )
    if videoTab:
        mouseControl(videoTab)
        pyautogui.click()

    time.sleep(3)
    # scroll up and down
    for i in range(3):
        r_scroll()
        time.sleep(2)
    # list of videos
    videos = browser.find_elements(By.ID, "video-title-link")
    if videos:
        for video in videos:
            href_value = video.get_attribute("href")
            if type(href_value) is str and "shorts" not in href_value:
                list_videos.append(href_value)
    # check list and click on video
    if len(list_videos) > 0:
        choosen_video = choice(list_videos)
        browser.get(choosen_video)
        time.sleep(3)
    try:
        # skip youtube ads
        skipAds = WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "button.ytp-ad-skip-button")
            )
        )
        mouseControl(skipAds)
        pyautogui.click()
    finally:
        time.sleep(3)
        # get youtube length
        video_length_element = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".ytp-time-duration"))
        )

        # Extract the video length value
        video_length_value = video_length_element.text
        time.sleep(3)
        time_to_seconds = timeCalc(video_length_value)
        watch_time = time_to_seconds * 0.1
        try:
            #  check if video is live and remove chat
            group_chat = browser.find_element(
                By.CSS_SELECTOR,
                "#show-hide-button > ytd-toggle-button-renderer > yt-button-shape > button",
            )
            group_chat.click()
        except:
            print("no live detected")
        finally:
            try:
                # click you dismiss youtube premium
                youtube_trial = browser.find_element(
                    By.CSS_SELECTOR, "#dismiss-button > yt-button-shape > button"
                )
                mouseControl(youtube_trial)
                pyautogui.click()
            finally:
                time.sleep(math.floor(watch_time))
                # click on owner channel
                current_channel = browser.find_element(
                    By.CSS_SELECTOR, "#owner > ytd-video-owner-renderer > a"
                )
                if current_channel:
                    mouseControl(current_channel)
                    pyautogui.click()
                # hna tji recursive
                time.sleep(3)
                #  re-run the script
                channel_func()


#  run the script
channel_func()

print("finished")
