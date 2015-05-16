Some configuration files that might be useful.

- /boot/config.txt

This controls the video monitor.  By default, it polls the monitor at bootup to see what screen resolution and refresh rate it should use.  If it doesn't find a monitor, it won't output a display.

This means either the monitor **must** be 'on' at boot, or you have to set the settings manually so it knows what to do.  In this file, I've commented out the 'hdmi_mode' and 'hdmi_group' settings I added for my monitor (an Insignia 19.5" TV), as an example of what you might want to do.  See the [raspberry pi documentiation] (https://www.raspberrypi.org/documentation/configuration/config-txt.md) for more information.

- /etc/xdg/lxsession/LXDE-pi/autostart

Add any scripts here that you want to start when your display launches.  In the sample shown, I've added a Python script that monitors my power output on my PedalPC and launches a web browser so I can view it in realtime.
