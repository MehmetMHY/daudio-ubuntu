<h1 align="center">DAUDIO UBUNTU README</h1>
<p align="center">
  <img width="300" src="https://user-images.githubusercontent.com/15916367/140458625-cbde3203-11cb-43f8-a614-5a60b35cdcc6.png">
</p>

## Acknowledge:
- This entire project/script was made to address a bug I encountered with my Ubuntu 20.04 setup. This bug worked like this, Ubuntu would always default to an audio source that did not output any audio and for some reason, every time I tried to change the audio source to my targeted audio source, Ubuntu would just default back to the bad audio source. 

## About:
- On my Ubuntu install, I had this issue where Ubuntu would always default to an audio source that had no output. So I would always have to go into settings and change the audio source back to my monitor speakers. I had to do this everytime I restarted my PC, everytime I woke up my PC from sleep mode, and everytime I paused audio (like pause a YouTube video). This was really annoying, so I made this daudio.py script.
- Currently, the daudio.py script has only been tested and proven to work on Ubuntu 20.04. So it would be best to run this script in Ubuntu 20.04.
- This script does the following, givening the params pause-time & audio-source-target:
	- [1] First, the script checks which audio source is running/being-used.
	- [2] If the audio source, that is running, is not (atleast contains) the audio-source-target, the script will attempt to change the audio source to the audio-source-target.
	- [3] If the running audio source is the audio-source-target, then nothing is changed.
	- [4] Steps 1 to 3 is applied every pause-time seconds (I recommend 1 sec).
- This script, if need be, needs to be ran as a start up script which can be set with the 'Startup Applications Preferences' application.

## Requirements:
- Ubuntu 20.04
- Pactl (included in Ubuntu)
- Python3 (included in Ubuntu)
- 'Startup Applications Preferences' Ubuntu App (included in Ubuntu)

## How To Run:
- Daudio Params:
```
python3 .daudio.py [float] [str] ["true"_or_"false"]
                     /       |                  \
     [loop delay (sec)] [target audio source]  [print logs for debugging]
```

- Daudio Example Command Run:
```
python3 .daudio.py 1 hdmi true
```
