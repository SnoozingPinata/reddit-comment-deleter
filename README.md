# reddit-comment-deleter
This script deletes your reddit history without using the reddit API.

# Setup:
1. Install python and pip.
2. Install "pyautogui" library through pip.
3. clone repository.

# How to use:
1. Open your browser
2. Login to reddit
3. click your username
4. run the script (main.py), and then make sure that your browser is the active window
5. repeat step 4 for each sorting method (hot, top, new, controversial)


# Troubleshooting:
If you are using dark mode, a different resolution, or a different zoom setting, you may need to take a screen shot of the "delete" and "yes" buttons and replace the images in the "images" folder. The mouse will move to the center of the screenshot, so the center of your screenshot needs to be in the right position to make your mouse able to click on the buttons.

Some long comments may be so large that the delete button will not show on the screen, and this will cause the script to stop. You will need to manually delete these comments. If you have many of these, you may be able to zoom your browser out and then follow the instructions above to replace the screenshots the script uses.
