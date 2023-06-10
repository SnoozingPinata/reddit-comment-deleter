import pyautogui
import time


def refresh_browser():
    print("Refreshing browser")
    pyautogui.press('f5')
    print("Waiting 5 seconds for browser refresh before continuing.")
    time.sleep(5)


def delete_all():
    deleted_comment_counter = 0
    refresh_counter = 0
    in_progress = True
    while in_progress:
        delete_position = pyautogui.locateCenterOnScreen('images/delete_button.png')
        if delete_position == None:
            print("Delete button not found. ")
            refresh_browser()
            refresh_counter += 1
        else:
            print("Deleting comment.")
            pyautogui.moveTo(delete_position)
            pyautogui.click()
            time.sleep(1)
            yes_position = pyautogui.locateCenterOnScreen('images/confirm_button.png')
            pyautogui.moveTo(yes_position)
            pyautogui.click()
            deleted_comment_counter += 1
            refresh_counter = 0
        if refresh_counter >= 5:
            in_progress = False
        print("Waiting to avoid rate limiting")
        time.sleep(3)
    print("Could not find new comment to delete after 5 browser refresh attempts. Exiting program.")
    print(f"Deleted {deleted_comment_counter} comments.")


if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    print("Starting reddit-comment-deleter program.")
    print("Move your mouse to the top left corner of your screen to exit the program.")
    print("Program starting in 3 seconds. Stop interacting with the keyboard and mouse.")
    time.sleep(3)
    delete_all()