import time
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from com.android.monkeyrunner.recorder import MonkeyRecorder as recorder

# Connects to the current device, returning a MonkeyDevice object

device = MonkeyRunner.waitForConnection()

print device

# Installs the Android package. Notice that this method returns a boolean, so you can test
#apk_path = device.shell('pm path org.nativescript.typescript')
apk_path = device.shell('pm path com.example.jangyoungsoo.iui_android;')

if apk_path.startswith('package:'):
    print "XXXYY already installed."
else:
    print "XXXYY app is not installed, installing APKs..."

recorder.start(device)
#device.touch(249,248, MonkeyDevice.DOWN_AND_UP)

#device.touch(100, 500, MonkeyDevice.DOWN)                                           
#device.type('text')
#device.type('\b\b\b')
'''
device.press('KEYCODE_DEL',  MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL',  MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL',  MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL',  MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL',  MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL',  MonkeyDevice.DOWN_AND_UP)
'''
# Move from 100, 500 to 300, 500
'''
for i in range(1, 31):                                                              
    device.touch(100 + 20 * i, 500, MonkeyDevice.MOVE)                              
    print "move ", 100 + 20 * i, 500                                                
    time.sleep(0.1)             
'''
'''
# Move from (300, 500 to 200, 500)                                                    
for i in range(1, 31):                                                              
    device.touch(300, 500 - 10 * i, MonkeyDevice.MOVE)                              
    print "move ", 300, 500 - 10 * i                                                
    time.sleep(0.05)                                                                 

# Remove finger from screen
device.touch(300, 400, MonkeyDevice.UP)
'''
'''
device.touch(100, 500, MonkeyDevice.DOWN)
for i in range(1, 21):                                                              
	device.touch(100 + 20 * i, 500, MonkeyDevice.MOVE)                              
	print "move ", 100 + 20 * i, 500                                                
	MonkeyRunner.sleep(0.1)             
device.touch(500, 500, MonkeyDevice.UP)
'''
'''
for i in range(1, 11):                                                              
	device.touch(300, 300+i*30, MonkeyDevice.MOVE)                              
	print "move ", 300, 300 + 30 * i
	MonkeyRunner.sleep(0.1)             
device.touch(300, 600, MonkeyDevice.UP)
'''
'''
device.touch(249,248, MonkeyDevice.DOWN_AND_UP)
device.touch(100, 500, MonkeyDevice.DOWN) 
for i in range(1, 11):                                                              
	device.touch(100 + 20 * i, 500, MonkeyDevice.MOVE)                              
	print "move ", 100 + 20 * i, 500                                                
	time.sleep(0.1)             

for i in range(1, 11):                                                              
    device.touch(300, 500 - 10 * i, MonkeyDevice.MOVE)                              
    print "move ", 300, 500 - 10 * i                                                
    time.sleep(0.1)                                                                 


device.touch(300, 400, MonkeyDevice.UP) 
'''
