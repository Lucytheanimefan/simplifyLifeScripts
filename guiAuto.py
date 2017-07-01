import pyautogui


def main():
	while True:
		x, y = pyautogui.position()
		print(str(x)+", "+str(y))


if __name__ == '__main__':
	main()