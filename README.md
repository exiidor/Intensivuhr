# Digital Clock

## Concept

This program shows the current time, date and weekday. It's designed with a Raspberry Pie Zero in mind.

## Preview

<img src="https://github.com/user-attachments/assets/aa0791c6-98a1-4f86-838f-980aa54f1d5f" alt="image" width=45%>
<img src="https://github.com/user-attachments/assets/4cd9ef16-899a-4a98-9059-b27137db9316" alt="image" width=45%>

(Dark/Lightmode)



## Schematics

You will need a [Respberry Pie Zero](https://www.berrybase.de/raspberry-pi-zero-w) and a [RTC-module](https://www.berrybase.de/ds3231-real-time-clock-modul-fuer-raspberry-pi)

## Features

- Shows time, date and weekday
- Darkmode 


## Setup

### __Hardware__ 

1. Connect the RTC-module to your Raspberry Pie\
 /// [Tutorial](https://www.youtube.com/watch?v=MthLLRNAGLs) ///

### __Software__

1. Install Raspberry Pie OS (32-bit) on a micro SD card
2. Set up your RCT-module\
 /// [Tutorial](https://www.youtube.com/watch?v=9aN2ocO2AWY) ///
3. Copy `clock.py` in your /home/USER directory
4. Create a autostart directory (if not present) and do not use `sudo`

    > mkdir /home/pi/.config/autostart

5. Create a .desktop file with `nano`

    > nano /home/pi/.config/autostart/clock.desktop

    Content :
    ```
    [Desktop Entry]\
    Type=Application\
    Name=Clock\
    Exec=/usr/bin/python3 /home/pi/clock.py
    ```

6. Reboot
