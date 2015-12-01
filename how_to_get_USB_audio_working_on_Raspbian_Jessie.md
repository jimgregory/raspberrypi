# How to set up USB audio on Raspberry Pi 2 Raspbian (Jessie)

1. get the card number of the USB audio

        ~:$ aplay -l
        **** List of PLAYBACK Hardware Devices ****
        card 0: ALSA [bcm2835 ALSA], device 0: bcm2835 ALSA [bcm2835 ALSA]
          Subdevices: 7/8
          Subdevice #0: subdevice #0
          Subdevice #1: subdevice #1
          Subdevice #2: subdevice #2
          Subdevice #3: subdevice #3
          Subdevice #4: subdevice #4
          Subdevice #5: subdevice #5
          Subdevice #6: subdevice #6
          Subdevice #7: subdevice #7
        card 0: ALSA [bcm2835 ALSA], device 1: bcm2835 ALSA [bcm2835 IEC958/HDMI]
          Subdevices: 1/1
          Subdevice #0: subdevice #0
        card 1: Set [C-Media USB Headphone Set], device 0: USB Audio [USB Audio]
          Subdevices: 1/1
          Subdevice #0: subdevice #0

    In this case, it's card 1

2. Open the alsa.conf file using a text editor (in this case, vim)

        ~:$ sudo vim /usr/share/alsa/alsa.conf

    Find the lines for defaults.ctl.card and defaults.pcm.card, comment them out, and add two new lines using your USB device's card number instead.

        #defaults.ctl.card 0    <-- old lines commented out
        #defaults.pcm.card 0
        defaults.ctl.card 1    <-- new lines added
        defaults.pcm.card 1
        
    Save the file when you're done.

4.  Edit the .asoundrc file in your home directory:

        ~:$ vim ~/.asoundrc

    At the end of the file, add the lines shown:

        pcm.!default
            type hw
            card 0
        }

        ctl.!default {
            type hw
            card 0
        }
        pcm.default.card 1  <-- add this lines

    Save the file and reboot.

