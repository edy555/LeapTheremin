Leap Theremin
============================================================

Simple Sample using Leap Motion and PyAudio

### Requirement ###

* Leap Motion device
* LeapSDK
* PyAudio
* portaudio

### Preparation ###

* portaudio and PyAudio

Install them as follows.

    $ brew install portaudio
    $ sudo pip install PyAudio

* LeapSDK

Download LeapSDK from https://www.leapmotion.com/developers, then copy files into your project folder.

    $ cd LeapSDK/lib
    $ cp Leap.py LeapPython.so libLeap.dylib {your folder}


### Execution ###

1. Attach your Leap Motion with USB connector.

2. In Terminal, run as follows.

   $ cd {your folder}
   $ ./leaptheremin.py


### Demonstration ###

* YouTube: http://youtu.be/Reoc-c9Ulto


### Attention ###

* LeapSDK fails on brew-installed-python, so you should use preinstalled python  of Mac OSX.
* tested on Mac OSX(10.8.2) only

