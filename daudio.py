'''
About:  Sets A Default Audio Source For Ubuntu
By:     Mehmet Yilmaz
Date:   11-4-2021

PARAM:
    python3 .daudio.py [float] [str] ["true"_or_"false"]
                         /       |                   |
        [loop delay (sec)]   [target audio source] [show print() or not]

EXAMPLE:
    python3 .daudio.py 1 hdmi true

COMPATIBLE:
    Ubuntu 20.04

HOW-TO-KILL-SCRIPT:
    1) Open System-Monitor.
    2) Filter by "python".
    3) Find the python process containing the name of this script.
    4) Right click on what you found for [3] then click "Kill".
'''

import subprocess
import time
import sys
import os

# [global] bool for logging and/or print messages
show = False

# log/print messages (if enabled)
def log_print(msg, tshow=False):
    global show
    message = "[DAUDIO] " + str(msg)
    if show or tshow:
        print(message)

# save terminal command output
def term_output(cmd):
    proc = subprocess.Popen(str(cmd), shell=True, stdout=subprocess.PIPE,)
    output = proc.communicate()[0].decode("utf-8")
    lines = output.split("\n")
    return lines

def get_all_sources():
    return term_output("pactl list short sinks")

# get 'target' audo source (requires pactl)
def audio_source(target, lines):
    valid_audio = ""
    for line in lines:
        if target in line.lower():
            valid_audio = line.split("\t")[1]
    return valid_audio

# set the default audio source
def set_audio(target_source, lines):

    # find source ID
    source = audio_source(target_source, lines)

    # set audio source using 'pactl' command
    if(source != ""):
        cmd = "pactl set-default-sink " + str(source)
        os.system(cmd)

        # log that an attempt was made to change the audio source
        log_print("Set Audio Source To: " + str(source))
    
    else:
        log_print("Failed To Find Audio Source, So No Changes Made")

# set audio source to target source if need be
def set_audio_calls(target):
    lines = get_all_sources()

    # filter audio source lines by SUSPENDED or RUNNING status
    data = {"SUSPENDED": [], "RUNNING": []}
    for line in lines:
        if "SUSPENDED" in line:
            data["SUSPENDED"].append(line)
        if "RUNNING" in line:
            data["RUNNING"].append(line)

    # only continue if there is an audio source running
    if(len(data["RUNNING"]) != 0):

        # check to see if the running audio source is the target source
        for source in data["RUNNING"]:
            if target not in source:

                # try to change audio source to target
                log_print("Not targeted audio source in use. Attempting to switch to targeted source.")
                set_audio(target, lines)

                break
    
    else:
        log_print("All audo sources are SUSPENDED at the moment")

# main loop for setting the audio to the 'target' audio source
def main_loop(settings):
    global show

    show = settings["show"]

    log_print("Following setting is being applied: " + str(settings))

    try:
        # main (infinate) loop for calls
        while(True):
            set_audio_calls(settings["target"])
            time.sleep(settings["delay"])
    except:
        log_print("Unknown Error Occured")

# main function calls
if __name__ == "__main__":

    # store setting data for script
    settings = {
        "delay": 1,
        "target": "",
        "show": False
    }

    # load arguments called from script
    args = list(sys.argv)
    args.pop(0)

    # only move forward if arguments provided are valid
    if len(args) == 3:
        try:
            settings["delay"] = float(args[0])
            settings["target"] = str(args[1])

            if str(args[2]).lower() == "true":
                settings["show"] = True
            else:
                settings["show"] = False
            
            # main function calls for the script
            main_loop(settings)

        except:
            # invalid arugments provided, so the script will not run
            log_print("Error! Invalid script arguments provided, please check the documentation within the script!", True)
            pass

