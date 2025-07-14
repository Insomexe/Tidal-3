import pyautogui
import pyperclip
import time
import random
import os


TIDAL_EXE = r"C:\Users\insom\AppData\Local\TIDAL\TIDAL.exe"

EMAIL= {1: "comsir@ccqu.top", 
        2: "43l5mln222@xkxkud.com", 
        3: "womexo9659@ofacer.com"}

PASSWORD = "4rfv3edc"

PLAYLISTS = [
    "Gas Station Vibes"
]

def get_random_playlist():
    return random.choice(PLAYLISTS)

rest_time = 120 # Dinleme süresi (saniye)

def open_tidal():
    os.startfile(TIDAL_EXE)
    time.sleep(10)
    
def search_and_play_playlist():
    playlist = get_random_playlist()
    print(f">>> Playlist aranıyor: {playlist}")
    pyautogui.click(800, 80, duration=1)
    pyautogui.write(playlist)
    time.sleep(4)
    pyautogui.press("enter")
    pyautogui.click(600, 250, duration=1)
    time.sleep(3)
    pyautogui.click()
    time.sleep(3)
    pyautogui.click(600, 430, duration=2)
    time.sleep(10)
    
def music_like():
    pyautogui.click(1015, 430, duration=1)
    time.sleep(2)
    for i in range(1):
        print(f"{(i+1)*1}. dakika...")
        pyautogui.click(950, 530 + (i % 3 - 1) * 90, duration=1)
        time.sleep(10)
        
def listen_playlist_for(duration):
    seconds= duration * 60
    elapsed = 0
    while elapsed < seconds:
        pyautogui.click(950, 530 + (elapsed % 3 - 1) * 90, duration=1)
        time.sleep(10)
        elapsed += 10
        print(f"Dinlenme süresi: {elapsed // 60} dakika {elapsed % 60} saniye")

def logout_user():
    pyautogui.click(100, 120, duration=1)
    time.sleep(4)
    pyautogui.click(200, 60, duration=1)
    time.sleep(2)
    pyautogui.click(250, 280, duration=1)
    time.sleep(10)

def login_user(EMAIL):
    pyautogui.click(950, 85, duration=1)
    time.sleep(10)
    pyautogui.click(455, 350, duration=1)
    pyperclip.copy(EMAIL)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(5)
    pyautogui.click(455, 420, duration=1)
    time.sleep(2)
    pyautogui.write(PASSWORD, interval=0.1)
    time.sleep(5)
    pyautogui.click(455, 500, duration=1)
    time.sleep(5)
    
def listen_playlist_for(_ignored):
    hours = random.randint(6, 23)
    seconds = hours * 60 * 60
    print(f">>> Dinlenme süresi belirlendi: {hours} saat")

    elapsed = 0
    while elapsed < seconds:
        pyautogui.click(950, 530 + (elapsed % 3 - 1) * 90, duration=1)
        time.sleep(10)
        elapsed += 10
        print(f"   Geçen süre: {elapsed // 60 // 60} saat {elapsed // 60 % 60} dakika {elapsed % 60} saniye")


def run_multi_user_rotation():
    while True:
        user = random.choice(list(EMAIL.values()))
        print(f"\n>>> {user} hesabına geçiliyor...")
        
        open_tidal()
        login_user(user)
        search_and_play_playlist()
        music_like()
        listen_playlist_for(0)  # burada artık random 6-23 saat çalışacak
        logout_user()
        login_user(user)


if __name__ == "__main__":
    run_multi_user_rotation()
    print("Otomasyon tamamlandı.")