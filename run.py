from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType

from fake_useragent import UserAgent
from random import randrange
from random import choice
import pyautogui
import time
import random
import httpagentparser
import math
from pygetwindow import getAllTitles
from win10toast import ToastNotifier
from nordvpn_switcher import initialize_VPN, rotate_VPN

# functions


def nordVpn():
    instructions = initialize_VPN(area_input=["random countries europe 8"])
    for i in range(1):
        rotate_VPN(instructions)  # refer to the instructions variable here
        time.sleep(5)


def display_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=5)


def detect_windows_notifications():
    previous_windows = getAllTitles()
    while True:
        current_windows = getAllTitles()
        new_notifications = [
            win for win in current_windows if win not in previous_windows
        ]
        for notification in new_notifications:
            display_notification(notification, "")
        previous_windows = current_windows


def goto(linenum):
    global line
    line = linenum


def user_agent_detect():
    user_agent = UserAgent()
    random_user_agent = user_agent.random
    return random_user_agent


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


def randMouseControl():
    absolute_x = randrange(25, 125)
    absolute_y = randrange(75, 175)
    pyautogui.moveTo(absolute_x, absolute_y, duration=0.5)
    time.sleep(1.5)


def mouseControl(elm):
    location = elm.location
    size = elm.size
    absolute_x = location["x"] + size["width"] - 25
    absolute_y = location["y"] + size["height"] + 65
    pyautogui.moveTo(absolute_x, absolute_y, duration=0.5)
    time.sleep(1.5)
# if (
#     "Microsoft Internet Explorer"
#     not in httpagentparser.simple_detect(user_agent_detect())[0]
#     or "Windows Vista" not in httpagentparser.simple_detect(user_agent_detect())[1]
#     or httpagentparser.simple_detect(user_agent_detect())[0] == ""
#     or type(httpagentparser.simple_detect(user_agent_detect())[0]) == None
# ):
#     user_agent_detect()

windows = "false"
randtrue = random.randrange(2)
if randtrue == 1:
    windows = "true"

# nordVpn()
# detect_windows_notifications()
# ip, port = get_proxy()

# Configure proxy settings

# proxy = Proxy()
# proxy.proxy_type = ProxyType.MANUAL
# proxy.http_proxy = f"{proxy_host}:{proxy_port}"
# proxy.ssl_proxy = f"{proxy_host}:{proxy_port}"


# print(f'IP: {ip} PORT: {port}')
# exit(1)
def counter(counter):
    counter = counter + 1
try :
    def run_it():
        global channel_back
        channel_back = "false"
        counter = 0  # Initialize the counter
        # arguments
        options = Options()
        options.add_argument(f"user-agent={user_agent_detect()}")
        options.add_argument("--mute-audio")
        if windows == "true":
            options.add_argument("--start-maximized")
        options.add_experimental_option("detach", True)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_argument("--proxy-server=http://"+proxy.ssl_proxy)

        def elem_f(valeur):
            try:
                return WebDriverWait(browser, 20).until(
                    EC.visibility_of_element_located((By.XPATH, valeur))
                )
            except:
                pass

        def r_scroll():
            browser.execute_script(
                "window.scrollTo({ top: " + str(randrange(4020)) + ", behavior: 'smooth' })"
            )
            time.sleep(4)

        def randCursor_ads():
            # Get the screen size
            screen_width, screen_height = pyautogui.size()

            # Set the number of cursor movements
            num_movements = 10

            # Set the delay between movements (in seconds)
            movement_delay = 0.2

            # Move the cursor randomly
            for _ in range(num_movements):
                # Generate random coordinates within the screen boundaries
                x = random.randint(0, screen_width)
                y = random.randint(0, screen_height)
                
                # Move the cursor to the random coordinates
                pyautogui.moveTo(x, y, duration=0.5)
                
                # Wait for a specified time before the next movement
                time.sleep(movement_delay)

        def aggrement():
            try:
                aggrements = elem_f(
                    '//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button'
                )
                # Get the size of the browser window
                mouseControl(aggrements)
                pyautogui.click()
            except :
                pass

        browser = webdriver.Chrome(options=options)
        browser.get("https://youtube.com")

        time.sleep(6)

        try:
            pasteXpath = "//*[@id='return-to-youtube']"
            element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, pasteXpath))
            )
            mouseControl(element)
            pyautogui.click()
        except:
            pass
            # aggrement()
            # browser.close()
            # run_it()

        
        aggrement()

        try:
            aggrements_mobile = browser.find_element(
                By.CSS_SELECTOR,
                "body > div.consent-bump-v2-lightbox > ytm-consent-bump-v2-renderer > div > div.dialog-scrollable-content > div.one-col-dialog-buttons > ytm-button-renderer.eom-accept > button",
            )
            # Get the size of the browser window
            mouseControl(aggrements_mobile)
            pyautogui.click()
        except:
            pass
        # Move the mouse to the element

        time.sleep(3)

        try:
            search = browser.find_element(By.NAME, "search_query")
            mouseControl(search)
            pyautogui.click()
            search_text = "hicham aboud"
            for letter in search_text:
                search.send_keys(letter)
                time.sleep(0.3)
        except:
            browser.close()
            run_it()
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
        # list_videos = []

        def channel_func():
            nonlocal counter
            channel_back = "false"
            time.sleep(3)
            if channel_back == "true":
                pass
                # browser.close()
                # run_it()
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

            pyautogui.click()
            time.sleep(3)
            # list of videos
            # videos = browser.find_elements(By.ID, "video-title-link")
            # if videos:
            #     for video in videos:
            #         href_value = video.get_attribute("href")
            #         if type(href_value) is str and "shorts" not in href_value:
            #             list_videos.append(href_value)
            # check list and click on video
            # if len(list_videos) > 0:
            #     for k in range(6):
            #         choosen_video = choice(list_videos)
            #  hadi tab original 1
            # Simulate the keyboard actions to open the link in a new tab
            # browser.find_element(By.TAG_NAME, "body").send_keys(Keys.LEFT_CONTROL, "t")
            # browser.switch_to.window(browser.window_handles[-1])
            # browser.get(choosen_video)

            try:
                # ads detect
                ads_type = WebDriverWait(browser, 20).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, ".ytp-ad-button"))
                )
                mouseControl(ads_type)
                pyautogui.click()
                time.sleep(4)
                randCursor_ads()
                time.sleep(25)
                pyautogui.hotkey("ctrl", "w")
                # TODO: Increment the counter here
                counter += 1
                print(counter)
            except:
                pass
            finally:
                try:
                    # play_video_after_clicking_on_ads
                    play_video = WebDriverWait(browser, 20).until(
                        EC.visibility_of_element_located(
                            (By.CSS_SELECTOR, ".ytp-play-button")
                        )
                    )
                    mouseControl(play_video)
                    pyautogui.click()
                    time.sleep(4)
                    try:
                        # skip youtube ads
                        skipAds = WebDriverWait(browser, 20).until(
                            EC.visibility_of_element_located(
                                (By.CSS_SELECTOR, "button.ytp-ad-skip-button")
                            )
                        )
                        mouseControl(skipAds)
                        pyautogui.click()
                        time.sleep(30)
                    finally:
                        pass
                    pass
                except:
                    pass
                print("no ads")
                time.sleep(2)
                print("Trying to restart the script.......")
                time.sleep(2)
                browser.close()
                time.sleep(2)
                if (randrange(100) % 2) == 1:
                    time.sleep(3)
                    nordVpn() 
                run_it()
            
            # get youtube length
            try:
                video_length_element = WebDriverWait(browser, 10).until(
                    EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, ".ytp-time-duration")
                    )
                )

                # Extract the video length value
                video_length_value = video_length_element.text
                time.sleep(3)
                # time_to_seconds = timeCalc(video_length_value)
                # watch_time = randrange(180)
            except:
                pass
            finally:
                pass
            try:
                #  check if video is live and remove chat
                group_chat = browser.find_element(
                    By.CSS_SELECTOR,
                    "#show-hide-button > ytd-toggle-button-renderer > yt-button-shape > button",
                )
                group_chat.click()
            except:
                pass
            finally:
                try:
                    # click you dismiss youtube premium
                    youtube_trial = browser.find_element(
                        By.CSS_SELECTOR, "#dismiss-button > yt-button-shape > button"
                    )
                    mouseControl(youtube_trial)
                    pyautogui.click()
                except:
                    pass
                finally:
                    time.sleep(130)
                    # click on owner channel
                    try:
                        current_channel = browser.find_element(
                            By.CSS_SELECTOR, "#owner > ytd-video-owner-renderer > a"
                        )

                        mouseControl(current_channel)
                        pyautogui.click()
                    except:
                        pass
                    finally:
                        # hna tji recursive
                        time.sleep(3)
                        #  re-run the script
                        channel_back = "true"
                        channel_func()

        #  run the script
        channel_func()


    nordVpn()
    run_it()
    print("finished")
except:
    print("somthing wrong ...")
    print("restart ...")
    run_it()