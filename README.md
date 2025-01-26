# Digital Clock

## Concept

This program shows the current time, date and weekday. It's designed with a Raspberry Pie Zero in mind.

## Preview

<img src="https://github.com/user-attachments/assets/aa0791c6-98a1-4f86-838f-980aa54f1d5f" alt="image" width=45%>
<img src="https://github.com/user-attachments/assets/4cd9ef16-899a-4a98-9059-b27137db9316" alt="image" width=45%>



## Schematics

You will need a [Respberry Pie Zero](https://www.berrybase.de/raspberry-pi-zero-w) (or newer model) and some kind of [RTC](https://www.berrybase.de/ds3231-real-time-clock-modul-fuer-raspberry-pi)-module

## Features

- Shows time, date and weekday
- Darkmode 


## Setup

### Hardware 

1. Connect the RTC-module to your Raspberry Pie. [Video](https://www.youtube.com/watch?v=MthLLRNAGLs)

### Software

1. Install Raspberry Pie OS (32-bit) on a micro SD card.
2. Set up your RCT-module [Video](https://www.youtube.com/watch?v=9aN2ocO2AWY)
3. Copy this repository in your /home/USER directory
4. Create a autostart directory if not present

    > mkdir /home/pi/.config/autostart

5. Create a .desktop file with nano

    > nano /home/pi/.config/autostart/clock.desktop

    Text input :
    ```
    [Desktop Entry]\
    Type=Application\
    Name=Clock\
    Exec=/usr/bin/python3 /home/pi/clock.py
    ```

6. Reboot
