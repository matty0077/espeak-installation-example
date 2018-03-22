# espeak-installation-example

Copied n pasted from https://www.peterbeard.co/blog/post/making-your-raspberry-pi-talk-to-you-with-espeak/


Prerequisites
eSpeak requires a few things to be done before it will work.
First of all, 
Raspbmcdoes not load the audio HAL for the Broadcom SOC by default and eSpeak (or mplayer, not sure which) needs it to output sound. To enable it just do

sudo modprobe snd_bcm2835

To make that permanent add snd_bcm2835 to the end of /etc/modules.

Next, you need to install alsa-libs, mplayer, and of course, eSpeak.

sudo apt-get update
sudo apt-get install alsa-libs mplayer espeak

mplayer supports LIRC by default, which is neat, but it seems to make it impossible to run mplayer from the terminal. To disable it, add nolirc=yes (why isn't it lirc=no?) to the end of /etc/mplayer/mplayer.conf.

Using eSpeak
Using eSpeak from the terminal is very easy. I've found the default options to work fine for me, so I just do this when I want to hear some words:

espeak "Some words."
**(To use it in a script, follow the example.)**

eSpeak has a lot of options to play with, but I'm perfectly happy with the defaults. You can read eSpeak's man page for more details.
