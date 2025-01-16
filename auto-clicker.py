import pyautogui
print("auto-clicker")
screenWidth, screenHeight = pyautogui.size()
print(f"screenWidth {screenWidth} screenHeight {screenHeight}") 
pyautogui.moveTo(1051, 623)
pyautogui.click()