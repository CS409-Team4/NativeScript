from __future__ import with_statement

import os
import shutil
import subprocess
import threading
import time
import re
import sys

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from com.android.monkeyrunner.recorder import MonkeyRecorder as recorder

sdk_path = None
device = None
device_id = None
dest_dir = None
package_name = None

###################
# helper          #
###################

time_sleep = 1.0

log_names = ['main_page', 'layouts', 'user_profile', 'conference_agenda', 'item_layouts', 'selection', 'naver_main']
log_nums = [0, 0, 0, 0, 0, 0, 0]

def click_back_button(device):
    device.touch(70, 200, MonkeyDevice.DOWN_AND_UP)

def backspace(device, num):
    for i in range(num):
        device.press("KEYCODE_DEL", MonkeyDevice.DOWN_AND_UP)
        time.sleep(0.1)

# def mid_process(t, sdk_path, device, device_id, dest_dir, package_name, layout_num):
def mid_process(t, layout_num):
    global sdk_path, device, device_id, dest_dir, package_name
    log_name = log_names[layout_num] + str(log_nums[layout_num]) + ".log"
    log_nums[layout_num] += 1
    run_dumpsys(sdk_path, device, device_id, dest_dir, package_name, log_name)
    time.sleep(t)
    reset_graphics_dumpsys(device, package_name)

###################

def main_page_drag(device):
    # drag down
    device.drag((540, 1500), (540, 800), 0.5, 10)
    mid_process(time_sleep, 0)

    # drag up
    device.drag((540, 800), (540, 1500), 0.5, 10)
    mid_process(time_sleep, 0)

def layout_page_drag(device):
    ### Press Layout ###
    device.touch(360, 400, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 1)

    for i in range(4):
        device.drag((800, 1000), (100, 1000), 0.1, 20)
        mid_process(time_sleep, 1)

    for i in range(4):
        device.drag((100, 1000), (800, 1000), 0.1, 20)
        mid_process(time_sleep, 1)

    click_back_button(device)
    mid_process(time_sleep, 1)

def user_profile_test(device):
    ### Press User Profile ###
    device.touch(720, 400, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 2)

    # edit username
    device.touch(540, 660, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 2)

    ## Type Hello Test and Delete 5 letters ###
    backspace(device, 12)
    device.type("Hello ")
    mid_process(time_sleep, 2)
    device.type("Test")
    mid_process(time_sleep, 2)
    device.press("KEYCODE_BACK", MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 2)

    ### Press checkbox ###
    device.touch(200, 1120, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 2)
    device.touch(200, 1120, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 2)

    # click switch
    device.touch(840, 1380, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 2)
    device.touch(840, 1380, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 2)

    # click update
    device.touch(540, 1600, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 2)

    click_back_button(device)
    mid_process(time_sleep, 2)

def conference_agenda_test(device):
    ### Press Conference Agendea ###
    device.touch(360, 1250, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 3)

    # drag down
    device.drag((540, 1600), (540, 800), 0.3, 10)
    mid_process(time_sleep, 3)

    # drag up
    device.drag((540, 800), (540, 1600), 0.3, 10)
    mid_process(time_sleep, 3)

    # click second item
    device.touch(540, 1000, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 3)
    device.touch(540, 1000, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 3)

    # click third item
    device.touch(540, 1300, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 3)

    ### Move to May 4 tab ###
    device.touch(540, 340, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 3)

    # click first item
    device.touch(540, 800, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 3)

    ### Move to May 5 tab ###
    device.touch(890,240, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 3)

    ### Search ###
    device.touch(550, 540, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 3)

    device.type("mobile")
    device.press("KEYCODE_BACK", MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 3)

    ### Move to May 4 tab ###
    device.touch(540, 340, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 3)

    ### Move to May 4 tab ###
    device.touch(180, 340, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 3)

    click_back_button(device)
    mid_process(time_sleep, 3)

def item_layout_drag_click(device):
    time_sleepi = 2.0

    ### Press Item Layouts ###
    device.touch(800, 1250, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleepi, 4)

    ### Drag Down ###
    for i in range(5):
        device.drag((540, 1600), (540, 400), 0.1, 20)
        mid_process(time_sleepi, 4)

    ### Drag Up ###
    for i in range(5):
        device.drag((540, 400), (540, 1600), 0.1, 20)
        mid_process(time_sleepi, 4)

    # change mode
    device.touch(990, 160, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleepi, 4)

    ### Drag Down ###
    for i in range(3):
        device.drag((540, 1600), (540, 400), 0.1, 20)
        mid_process(time_sleepi, 4)

    ### Drag Up ###
    for i in range(3):
        device.drag((540, 400), (540, 1600), 0.1, 20)
        mid_process(time_sleepi, 4)

    click_back_button(device)
    mid_process(time_sleepi, 4)

def selection_test(device):
    # drag down
    device.drag((540, 1500), (540, 800), 0.5, 10)
    mid_process(time_sleep, 5)

    ### Press selection page ###
    device.touch(360, 1400, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 5)

    device.touch(810, 280, MonkeyDevice.DOWN_AND_UP) ### click FAVORITE TAB ###
    mid_process(time_sleep, 5)
    device.touch(259, 280, MonkeyDevice.DOWN_AND_UP) ### click ALL TAB ###
    mid_process(time_sleep, 5)

    # click first item
    device.touch(690, 520, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 5)
    # click favorite
    device.touch(890, 140, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 5)

    ### long click second item (edit mode) ###
    device.touch(490, 890, MonkeyDevice.DOWN)
    mid_process(time_sleep, 5)
    device.touch(490, 890, MonkeyDevice.UP)
    mid_process(time_sleep, 5)

    # click second item
    device.touch(480, 1100, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 5)
    # click third item
    device.touch(480, 1600, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 5)

    ### Drag ###
    device.drag((540, 1200), (540, 300), 0.5, 20)
    mid_process(time_sleep, 5)

    device.touch(480, 1000, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 5)
    device.touch(480, 1600, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 5)

    # click favorite
    device.touch(890, 140, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 5)

    # move to favorite tab
    device.touch(810, 280, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 5)

    # move to all tab
    device.touch(259, 280, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 5)

    # click 4th item
    device.touch(350, 1100, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 5)

    # click delete button
    device.touch(1000, 150, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 5)

    # move to favorite tab
    device.touch(810, 280, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 5)

    # click reorder button
    device.touch(1030, 130, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 5)

    ### Drag first item to second position ###
    device.drag((100, 670), (100, 1600), 1.0, 30)
    mid_process(time_sleep, 5)

    # back to selection page
    click_back_button(device)

    # back to main page
    click_back_button(device)

def naver_web_test(device):
    time_sleepn = 3.0
    # drag down
    device.drag((540, 1500), (540, 800), 0.5, 10)
    mid_process(time_sleep, 6)

    ### Press naver main page ###
    device.touch(800, 1400, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleepn, 6)

    # drag down
    device.drag((540, 1700), (540, 660), 0.1, 20)
    mid_process(time_sleepn, 6)

    # drag down
    device.drag((540, 1700), (540, 660), 0.1, 20)
    mid_process(time_sleepn, 6)

    # drag up
    device.drag((540, 660), (540, 1700), 0.1, 20)
    mid_process(time_sleepn, 6)

    # click sports tab
    device.touch(540, 500, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleepn, 6)

    # open drawer
    device.touch(90, 160, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleepn, 6)

    # close drawer
    device.touch(960, 200, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleepn, 6)

    # reopen drawer
    device.touch(90, 160, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleepn, 6)

    ### click cafe button ###
    device.touch(400, 500, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleepn, 6)

    ### click floating back button ###
    device.touch(140, 1650, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleepn, 6)

    # reopen drawer
    device.touch(90, 160, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleepn, 6)

    ### click blog button ###
    device.touch(680, 500, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleepn, 6)

    ### click floating back button ###
    device.touch(140, 1650, MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleepn, 6)

    device.press("KEYCODE_BACK", MonkeyDevice.DOWN_AND_UP)
    mid_process(time_sleep, 6)



### Functions used in testing ###
def clean_test_files(dest_dir):
    """Removes the test files that are generated during a test run."""

    print 'Cleaning data files'
    folders = [os.path.join(dest_dir, 'testdata'),
               os.path.join(dest_dir, 'logs')]
    for the_folder in folders:
        if os.path.isdir(the_folder):
            for the_file in os.listdir(the_folder):
                file_path = os.path.join(the_folder, the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except IOError, exception:
                    print exception
    for the_folder in folders:
        if not os.path.isdir(the_folder):
            try:
                os.makedirs(the_folder)
            except OSError:
                print 'ERROR Could not create directory structure for tests.'

# Enable the DUMP permission on the debuggable test APK (test APK because
# we declared the permission in the androidTest AndroidManifest.xml file.
def enable_dump_permission(sdk_path, device_id, dest_dir, package_name):
    """Enable the DUMP permission on the specified and installed Android
    app.
    """

    print 'Starting dump permission grant'
    perm_command = [os.path.join(sdk_path, 'platform-tools', 'adb'),
                    '-s', device_id,
                    'shell',
                    'pm', 'grant', package_name,
                    'android.permission.DUMP']
    log_file_path = os.path.join(dest_dir, 'logs', 'enable_dump_perm.log')
    with open(log_file_path, 'w') as log_file:
        try:
            subprocess.call(perm_command,
                            stdout=log_file,
                            stderr=subprocess.STDOUT,
                            shell=False)
        except OSError:
            print 'ERROR executing permission grant.'


# Enable the Storage permission on the debuggable test APK (test APK because
# we declared the permission in the androidTest AndroidManifest.xml file.
def enable_storage_permission(sdk_path, device_id, dest_dir, package_name):
    """Enable the WRITE_EXTERNAL_STORAGE permission on the specified and
    installed Android app.
    """

    print 'Starting storage permission grant'
    perm_command = [os.path.join(sdk_path, 'platform-tools',
                                 'adb'),
                    '-s', device_id,
                    'shell',
                    'pm', 'grant', package_name,
                    'android.permission.WRITE_EXTERNAL_STORAGE']
    log_file_path = os.path.join(dest_dir, 'logs', 'enable_storage_perm.log')
    with open(log_file_path, 'w') as log_file:
        try:
            subprocess.call(perm_command,
                            stdout=log_file,
                            stderr=subprocess.STDOUT,
                            shell=False)
        except OSError:
            print 'ERROR executing permission grant.'

def open_app(device, package_name):
    """Open the specified app on the device."""

    device.shell('am start -n ' + package_name + '/' + package_name +
                 '.MainActivity')

def reset_graphics_dumpsys(device, package_name):
    """Reset all existing data in graphics buffer."""
    print 'Clearing gfxinfo on device'
    device.shell('dumpsys gfxinfo ' + package_name + ' reset')

def perform_dumpsys(sdk_path, device_id, dest_dir, package_name, log_name):
    dumpsys_command = ['adb', 'shell', 'dumpsys', 'gfxinfo', package_name]
    print 'Executing dumpsys'
    dumpsys_log_path = os.path.join(dest_dir, 'logs', log_name)
    with open(dumpsys_log_path, 'w') as dumpsys_log:
        try:
            subprocess.call(dumpsys_command,
                            stdout=dumpsys_log,
                            stderr=subprocess.STDOUT,
                            shell=False)
        except OSError:
            print 'ERROR executing dumpsys ' + os_error

    print 'Done dumpsys logging'

def run_dumpsys(sdk_path, device, device_id, dest_dir, package_name, log_name):
    """Create and start threads to run tests and collect tracing information."""
    dumpsys_thread = threading.Thread(name='DumpsysThread', target=perform_dumpsys, args=(sdk_path, device_id, dest_dir, package_name, log_name))
    dumpsys_thread.start()

    dumpsys_thread.join()
    dumpsys_time_completion = int(time.time())
    print 'Dumpsys Thread Done'


def pull_device_data_files(sdk_path, device_id, source_dir, dest_dir, package_name, log_suffix):
    """Extrace test files from a device after a test run."""

    print 'Starting adb pull for test files'
    test_data_location = (source_dir + package_name +
                          '/files/testdata')
    pull_test_data_command = [os.path.join(sdk_path, 'platform-tools',
                                           'adb'),
                              '-s', device_id, 'pull', test_data_location,
                              dest_dir]
    log_file_path = os.path.join(dest_dir, 'logs', 'pull_test_files' + log_suffix + '.log')
    with open(log_file_path, 'w') as pull_test_data_log_file:
        try:
            subprocess.call(pull_test_data_command,
                            stdout=pull_test_data_log_file,
                            stderr=subprocess.STDOUT,
                            shell=False)
        except OSError:
            print 'ERROR extracting test files.'


def parse_dump_file(filename):
    """Parse dump file data."""
    with open(filename, 'r') as dump_file:
        results = dict()
        for line in dump_file:
            match = re.search(r'Janky frames: (\d+) \(([\d\.]+)%\)', line)
            if match is not None:
                results['jankNum'] = int(match.group(1))
                results['jank_percent'] = float(match.group(2))
        return results

def analyze_data_files(dest_dir):
    """Analyze data files for issues that indicate a test failure."""
    overall_passed = True
    test_data_dir = os.path.join(dest_dir, 'testdata')
    for dir_name, sub_dir_list, file_list in os.walk(test_data_dir):
        if dir_name == os.path.join(dest_dir, 'testdata'):
            # in the root folder
            for fname in file_list:
                if fname == 'batterystats.dumpsys.log':
                    # pylint: disable=fixme
                    # TODO(developer): process battery data.
                    continue
                elif fname == 'locationRequests.dumpsys.log':
                    # pylint: disable=fixme
                    # TODO(developer): process location requests information.
                    continue
        else:
            # in a test folder
            print '\nAnalysing test: ' + dest_dir
            passed = True

            for fname in file_list:
                full_filename = os.path.join(dir_name, fname)
                if fname == 'gfxinfo.dumpsys.log':
                    # process gfxinfo for janky frames
                    dump_results = parse_dump_file(full_filename)
                    jank_perc = dump_results['jank_percent']
                    if jank_perc:
                        if jank_perc > JANK_THRESHOLD:
                            print ('FAIL: High level of janky frames ' +
                                   'detected (' + str(jank_perc) + '%)' +
                                   '. See trace.html for details.')
                            passed = False
                    else:
                        print 'ERROR: No dump results could be found.'
                        passed = False
                elif fname == 'test.failure.log':
                    # process test failure logs
                    print ('FAIL: Test failed. See ' + full_filename +
                           ' for details.')
                    passed = False
            if passed:
                print 'PASS. No issues detected.'
            else:
                overall_passed = False
    test_complete_file = os.path.join(dest_dir, 'testdata',
                                      'testRunComplete.log')
    if not os.path.isfile(test_complete_file):
        overall_passed = False
        print ('\nFAIL: Could not find file indicating the test run ' +
               'completed. Check that the TestListener is writing files to external storage')
    if overall_passed:
        print '\nOVERALL: PASSED.'
        return 0
    else:
        print '\nOVERALL: FAILED. See above for more information.'
        return 1

def main():
    """Run this script with
    monkeyrunner testing_code.py <DEST_DIR> <DEVICE_ID> <PACKAGE_NAME>
    """

    global sdk_path, device, device_id, dest_dir, package_name

    dest_dir = sys.argv[1:][0] or '.'
    print 'Writing logs to: ' + dest_dir

    device_id = sys.argv[1:][1] or null
    print 'Using device_id: ' + device_id

    package_name = sys.argv[1:][2]
    print 'Running package name: ' + package_name

    dest_dir = os.path.join(dest_dir, "perftesting", device_id)
    android_home = os.environ['ANDROID_HOME']
    print 'Your ANDROID_HOME is set to: ' + android_home

    platform_tools = os.path.join(android_home, 'platform-tools')
    current_path = os.environ.get('PATH', '')
    os.environ['PATH'] = (platform_tools if current_path == '' else current_path +
                          os.pathsep + platform_tools)

    if not os.path.isdir(android_home):
        print 'Your ANDROID_HOME path do not appear to be set in your environment'
        sys.exit(1)

    # Your SDK path. Adjust this to your needs.
    sdk_path = android_home

    clean_test_files(dest_dir)

    # Connects to the current device, returning a MonkeyDevice object
    print 'Waiting for a device to be connected.'
    device = MonkeyRunner.waitForConnection(5, device_id)
    print 'Device connected.'

    enable_dump_permission(sdk_path, device_id, dest_dir, package_name)
    enable_storage_permission(sdk_path, device_id, dest_dir, package_name)

    # open_app(device, package_name)

    # Clear the dumpsys data for the next run must be done immediately
    # after open_app().
    # Empty dumpsys
    

    # open_app(device, package_name)

    # Calling automation functions
    print "Test start"
    
    reset_graphics_dumpsys(device, package_name)
    main_page_drag(device)
    layout_page_drag(device)
    user_profile_test(device)
    conference_agenda_test(device)
    item_layout_drag_click(device)
    selection_test(device)
    naver_web_test(device)

    # Device files could be in either location on various devices.
    # pull_device_data_files(sdk_path, device_id,
    #     '/storage/emulated/0/Android/data/',
    #     dest_dir, package_name, '1')
    # pull_device_data_files(sdk_path, device_id,
    #     '/storage/emulated/0/Android/data/',
    #     dest_dir, package_name, '2')

    # analyze_data_files(dest_dir)


if __name__ == '__main__':
    main()
# user_profile_test()
# conference_agenda_test()
# item_layout_drag_click()
# selection_test()
# print "Test Done"
