import time
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from com.android.monkeyrunner.recorder import MonkeyRecorder as recorder

device = MonkeyRunner.waitForConnection()
print device

def backspace(num):
	for i in range(num):
		device.press("KEYCODE_DEL", MonkeyDevice.DOWN_AND_UP)
		time.sleep(0.1)


# Installs the Android package. Notice that this method returns a boolean, so you can test
#apk_path = device.shell('pm path org.nativescript.typescript')
#apk_path = device.shell('pm path com.example.jangyoungsoo.iui_android')
#apk_path = device.shell('pm path com.iui')
'''
if apk_path.startswith('package:'):
    print "Already installed."
else:
    print "No Installed"
'''
### start Main page ###
def main_page_drag():
	print "Test start"
	### Drag Down ###
	device.touch(360, 800, MonkeyDevice.DOWN)
	for i in range(30):
		device.touch(360, 800 -i*10, MonkeyDevice.MOVE)
		time.sleep(0.01)
	device.touch(360, 500, MonkeyDevice.UP)


	### Drag Up ###
	device.touch(360, 500, MonkeyDevice.DOWN)
	for i in range(33):
		device.touch(360, 500 +i*30, MonkeyDevice.MOVE)
		time.sleep(0.01)
	device.touch(360, 800, MonkeyDevice.UP)
	time.sleep(0.2)


def main_drawer_and_about():
	### Press Main navi button ###
	device.touch(60,133, MonkeyDevice.DOWN_AND_UP)
	time.sleep(0.5)

	### Press About tap ###
	device.touch(294,690, MonkeyDevice.DOWN_AND_UP)
	time.sleep(2.0)
	device.touch(49,101, MonkeyDevice.DOWN_AND_UP) # back button click
	time.sleep(1.5)

def layout_page_darg():
	### Press Layout ###
	device.touch(191,354, MonkeyDevice.DOWN_AND_UP)
	time.sleep(0.5)

	for j in range(4):
		device.touch(640, 800, MonkeyDevice.DOWN)
		for i in range(30):
			device.touch(640-i*20, 800, MonkeyDevice.MOVE)
			time.sleep(0.02)
		device.touch(40, 800, MonkeyDevice.UP)
		time.sleep(0.5)

	device.touch(49,101, MonkeyDevice.DOWN_AND_UP) # back button click
	time.sleep(1.0)

def user_profile_test():
	### Press User Profile ###
	device.touch(533,354, MonkeyDevice.DOWN_AND_UP)
	time.sleep(0.5)

	device.touch(328, 440, MonkeyDevice.DOWN_AND_UP) ## Touch TextView
	time.sleep(0.5)

	### Type Hello Test and Delete 5 letters ###
	device.type("Hello")
	time.sleep(0.5)
	device.type("Test")
	time.sleep(0.5)
	backspace(10)
	device.press("KEYCODE_BACK", MonkeyDevice.DOWN_AND_UP)
	time.sleep(1.0)

	### Press checkbox ###
	device.touch(130,784, MonkeyDevice.DOWN_AND_UP)
	time.sleep(1.0)
	device.touch(130,784, MonkeyDevice.DOWN_AND_UP)
	time.sleep(1.0)
	device.touch(400, 1190, MonkeyDevice.DOWN_AND_UP)
	time.sleep(1.0)
	device.touch(49,101, MonkeyDevice.DOWN_AND_UP) # back button click
	time.sleep(1.0)

def conference_agenda_test():
	### Press Conference Agendea ###
	device.touch(200,765, MonkeyDevice.DOWN_AND_UP)
	time.sleep(1.0)
	device.touch(270,700, MonkeyDevice.DOWN_AND_UP)
	time.sleep(1.0)
	device.touch(270,700, MonkeyDevice.DOWN_AND_UP)
	time.sleep(1.0)
	device.touch(303,530, MonkeyDevice.DOWN_AND_UP)
	time.sleep(1.0)
	device.touch(315,845, MonkeyDevice.DOWN_AND_UP)
	time.sleep(1.0)

	### Move to May 4 tab ###
	device.touch(375,218, MonkeyDevice.DOWN_AND_UP)
	time.sleep(1.0)
	device.touch(200,765, MonkeyDevice.DOWN_AND_UP)
	time.sleep(1.0)
	device.touch(375,1030, MonkeyDevice.DOWN_AND_UP)
	time.sleep(1.0)

	### Move to May 5 tab ###
	device.touch(500,218, MonkeyDevice.DOWN_AND_UP)
	time.sleep(1.0)
	### Make Filter ###
	device.touch(380,360, MonkeyDevice.DOWN_AND_UP)
	time.sleep(1.0)
	device.type("mobile")
	time.sleep(1.0)
	backspace(6)
	time.sleep(1.0)
	device.press("KEYCODE_BACK", MonkeyDevice.DOWN_AND_UP) ## press device back button
	time.sleep(1.0)
	device.touch(49,101, MonkeyDevice.DOWN_AND_UP) # back button click
	time.sleep(1.0)


def item_layout_drag_click():
	### Press Item Layouts ###
	device.touch(540, 780, MonkeyDevice.DOWN_AND_UP)
	time.sleep(1.0)

	### Drag Down ###
	device.touch(360, 1200, MonkeyDevice.DOWN)
	for i in range(30):
		device.touch(360, 1200 -i*30, MonkeyDevice.MOVE)
		time.sleep(0.01)
	device.touch(360, 300, MonkeyDevice.UP)
	time.sleep(1.0)

	### Drag Up ###
	device.touch(360, 300, MonkeyDevice.DOWN)
	for i in range(33):
		device.touch(360, 300 +i*30, MonkeyDevice.MOVE)
		time.sleep(0.01)
	device.touch(360, 1200, MonkeyDevice.UP)
	time.sleep(1.0)

	device.touch(670, 100, MonkeyDevice.DOWN_AND_UP)
	time.sleep(1.0)

	### Drag Down ###
	device.touch(360, 1200, MonkeyDevice.DOWN)
	for i in range(30):
		device.touch(360, 1200 -i*30, MonkeyDevice.MOVE)
		time.sleep(0.01)
	device.touch(360, 300, MonkeyDevice.UP)
	time.sleep(1.0)

	### Drag Up ###
	device.touch(360, 300, MonkeyDevice.DOWN)
	for i in range(33):
		device.touch(360, 300 +i*30, MonkeyDevice.MOVE)
		time.sleep(0.01)
	device.touch(360, 1200, MonkeyDevice.UP)
	time.sleep(1.0)

	device.touch(670, 100, MonkeyDevice.DOWN_AND_UP)
	time.sleep(1.0)

	device.touch(49,101, MonkeyDevice.DOWN_AND_UP) # back button click
	time.sleep(1.0)

def selection_test():
	### Drag ###
	device.touch(360, 1200, MonkeyDevice.DOWN)
	for i in range(30):
		device.touch(360, 1200 -i*30, MonkeyDevice.MOVE)
		time.sleep(0.01)
	device.touch(360, 300, MonkeyDevice.UP)
	time.sleep(1.0)
	### Drag END ###
	### Press selection page ###
	device.touch(182, 1040, MonkeyDevice.DOWN_AND_UP) ### click FAVORITE TAB ###
	time.sleep(1)

	device.touch(530, 220, MonkeyDevice.DOWN_AND_UP) ### click FAVORITE TAB ###
	time.sleep(1)
	device.touch(180, 220, MonkeyDevice.DOWN_AND_UP) ### click ALL TAB ###
	time.sleep(1)
	device.touch(333, 445, MonkeyDevice.DOWN_AND_UP)
	time.sleep(1)
	device.touch(567, 100, MonkeyDevice.DOWN_AND_UP) ### click favorite ###
	time.sleep(1)
	device.touch(530, 220, MonkeyDevice.DOWN_AND_UP) ### click FAVORITE TAB ###
	time.sleep(1)
	device.touch(180, 220, MonkeyDevice.DOWN_AND_UP) ### click ALL TAB ###
	time.sleep(1)
	### Hold ###
	device.touch(350, 720, MonkeyDevice.DOWN)
	time.sleep(1)
	device.touch(567, 100, MonkeyDevice.UP)
	time.sleep(1)
	### Hold End ####

	device.touch(350, 1050, MonkeyDevice.DOWN_AND_UP)
	time.sleep(1)
	### Drag ###
	device.touch(360, 1200, MonkeyDevice.DOWN)
	for i in range(30):
		device.touch(360, 1200 -i*30, MonkeyDevice.MOVE)
		time.sleep(0.01)
	device.touch(360, 300, MonkeyDevice.UP)
	time.sleep(1.0)

	### Drag End ###
	device.touch(360, 780, MonkeyDevice.DOWN_AND_UP)
	time.sleep(1.0)
	device.touch(360, 1200, MonkeyDevice.DOWN_AND_UP)
	time.sleep(1.0)
	device.touch(567, 100, MonkeyDevice.DOWN_AND_UP) ### click favorite ###
	time.sleep(1)
	### Drag ###
	device.touch(360, 1200, MonkeyDevice.DOWN)
	for i in range(30):
		device.touch(360, 1200 -i*30, MonkeyDevice.MOVE)
		time.sleep(0.01)
	device.touch(360, 300, MonkeyDevice.UP)
	### Drag End ###

	time.sleep(1)
	device.touch(530, 220, MonkeyDevice.DOWN_AND_UP) ### click FAVORITE TAB ###
	time.sleep(1)
	device.touch(360, 1200, MonkeyDevice.DOWN)
	for i in range(30):
		device.touch(360, 1200 -i*30, MonkeyDevice.MOVE)
		time.sleep(0.01)
	device.touch(360, 300, MonkeyDevice.UP)
	time.sleep(1)
	device.touch(180, 220, MonkeyDevice.DOWN_AND_UP) ### click ALL TAB ###
	time.sleep(1)
	### Hold ###
	device.touch(350, 450, MonkeyDevice.DOWN)
	time.sleep(1)
	device.touch(350, 450, MonkeyDevice.UP)
	time.sleep(1)
	### Hold End ####
	device.touch(350, 830, MonkeyDevice.DOWN_AND_UP)
	time.sleep(1)
	device.touch(350, 1100, MonkeyDevice.DOWN_AND_UP)
	time.sleep(1)
	device.touch(670, 110, MonkeyDevice.DOWN_AND_UP) ### click delete icon ###
	time.sleep(1)
	device.touch(530, 220, MonkeyDevice.DOWN_AND_UP) ### click FAVORITE TAB ###
	time.sleep(2)

	device.touch(49,101, MonkeyDevice.DOWN_AND_UP) # back button click
	time.sleep(1.0)

def naver_web_test():
	### Drag ###
	device.touch(360, 1200, MonkeyDevice.DOWN)
	time.sleep(2)
	for i in range(30):
		device.touch(360, 1200 -i*30, MonkeyDevice.MOVE)
		time.sleep(0.01)
	device.touch(360, 300, MonkeyDevice.UP)
	time.sleep(2.0)
	### Drag END ###
	### Press Naver page ###
	device.touch(540, 1040, MonkeyDevice.DOWN_AND_UP) 
	time.sleep(5)
	device.touch(40, 800, MonkeyDevice.DOWN)
	### Drag navi drawer ###
	for i in range(30):
		device.touch(40+i*20, 800, MonkeyDevice.MOVE)
		time.sleep(0.02)
	device.touch(640, 800, MonkeyDevice.UP)
	time.sleep(3.5)
	### click mail button ###
	device.touch(100, 330, MonkeyDevice.DOWN_AND_UP) 
	time.sleep(5)
	### click floating back button ###
	device.touch(85, 1185, MonkeyDevice.DOWN_AND_UP) 
	time.sleep(3)
	### Drag navi drawer ###
	device.touch(40, 800, MonkeyDevice.DOWN)
	for i in range(30):
		device.touch(40+i*20, 800, MonkeyDevice.MOVE)
		time.sleep(0.02)
	device.touch(640, 800, MonkeyDevice.UP)
	time.sleep(3.5)
	### click blog button ###
	device.touch(450, 330, MonkeyDevice.DOWN_AND_UP) 
	time.sleep(2)
	### click floating back button ###
	device.touch(85, 1185, MonkeyDevice.DOWN_AND_UP) 
	time.sleep(2)
	### press tab button ###
	device.touch(220, 340, MonkeyDevice.DOWN_AND_UP) 
	time.sleep(2)
#user_profile_test()
#conference_agenda_test()
#item_layout_drag_click()
#selection_test()
naver_web_test()

print "Test Done"
