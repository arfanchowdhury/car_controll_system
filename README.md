
## Car Control System Over Internet using Raspberry Pi

### Description
- This controller software is designed to run on your robot and will connect with our development server. It's tuned to support Raspberry Pi based robots, however there is extensive support for other hardware configurations.

- Car Control System Over Internet using Raspberry Pi the robot which can be used for video surveillance & monitoring which can be controlled through a Graphical User Interface and inexpensive surveillance system as well as a spy tool.

- Challenges -
   - The control mechanism is provided with a video transmission facility.
   Initially, the robot will be equipped with a camera which will capture the scenes and transfer the images to the server on which the user will be controlling and watching the live feed.

### Technologies 
- [Python 3](https://www.python.org/downloads)
- [web-socket](https://websockets.readthedocs.io/en/stable/index.html)
- [remo-tv](https://remo.tv)
- [raspbian OS](https://www.raspberrypi.com/documentation/computers/getting-started.html#installing-the-operating-system)

### Hardware 
- [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b)
- [Pi-Camera](https://picamera.readthedocs.io/en/release-1.13)
- [Motor Driver L298n](https://maker.pro/raspberry-pi/tutorial/how-to-control-a-dc-motor-with-an-l298-controller-and-raspberry-pi)
- DC Motor
- RC Car Chassis
- Battery etc.


### Basic setup guide
If this is your first time working with a Raspberry Pi or Linux, we recommend following our [initializtion tutorial](https://github.com/remotv/controller/wiki/Initializing-the-Raspberry-Pi) to get started.

### Installing remotv control scripts on a Raspberry Pi

If doing things manually isn't your style, we made an [optional guided installation](https://github.com/remotv/controller/wiki/Optional-Guided-Installation-Script) script that handles mostly everything for you.

The RasPi will need the following things install so it can talk to your motors and talk to the internet. Make sure you don’t get any errors in the console when doing the step below. If you have an issue, you can run this line again, and that will usually fix it!

1. Install the required software libraries and tools. Make sure you don’t get any errors in the console when doing the step below. If you have an issue, you can run this line again, and that will usually fix it!

   ```sh
   sudo apt update
   sudo apt upgrade -y
   sudo apt install ffmpeg python-serial python-dev libgnutls28-dev espeak python-smbus python-pip git
   ```

2. Download the remotv control scripts from our github

   ```sh
   git clone https://github.com/car_controll_system/controller.git ~/car_controll_system
   ```

3. Install python requirements

   ```sh
   sudo python -m pip install -r ~/car_controll_system/requirements.txt
   ```

4. Open the new `car_controll_system` directory

   ```sh
   cd car_controll_system
   ```

5. Copy `controller.sample.conf` to `controller.conf`

   ```sh
   cp controller.sample.conf controller.conf
   ```

#### Configure the controller

1. Edit the `controller.conf` file created in the previous section.
   ```sh
   nano controller.conf
   ```
2. Configure the `[robot]` section

   - `owner` should be the username you have registered the robot under on the remo.tv site.
   - `robot_key` is the API key for your robot that you made on the site.
      - Your API key is LONG. It should look something like `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6InJib3QtNTVjZjJmMjUtNjBhNS00ZDJkLTk5YzMtOGZmOGRiYWU4ZDQ1IiwiaWF0IjoxNTczNTExMDA2LCJzdWIiOiIifQ.LGXSBSyQ4T4X5xU_w3QJD6R3lLjrrkw_QktOIDzRW5U`. If it is not this long, you have not copied the full key.
   - `turn_delay` is only used by the `motor_hat` and `mdd10`. This changes how long your bot turns for. I suggest you leave this at the default value until after you bot is moving.
   - `straight_delay` is only used by the `motor_hat` and `mdd10`. This changes how long your bot turns for. I suggest you leave this at the default value until after you bot is moving.
   - `type` should be the hardware type for the motor controller of your bot. Available types are currently.
     - `adafruit_pwm`
     - `cozmo`
     - `gopigo2`
     - `gopigo3`
     - `l298n`
     - `maestro-serv`
     - `max7219`
     - `mc33926`
     - `mdd10`
     - `motor_hat`
     - `motozero`
     - `none`
     - `owi_arm`
     - `pololu`
     - `serial_board`
     - `telly`
     - `thunderborg`
   - Configure your hardwares section. Each hardware type can have their own section it the controller. Look through the file for a section named the same as your hardware controller. If the section exists, read through it and adjust the variable as required.

3. Configure the `[camera]` section
   - `no-mic` This allows the microphone to be disabled.
   - `no-camera` This allows the camera to be disabled.
   - `type` This sets the audio / video handler to use. Currently only ffmpeg and ffmpeg-arecord are supported.
   - `x_res` Sets the resolution for the x axis.
   - `y_res` Sets the resolution for the y axis.
   - `camera_device` Sets the device name for the camera.
   - `audio_hw_num` Set the audio hardware number for the microphone.
4. Configure the `[tts]` section
   - `tts_volume` This is the volume level you want your bot to start with.
   - `anon_tts` This allows you to enable or disable anonymous users access to your bots TTS features.
   - `filter_url_tts` This option allows URLs pasted into chat to be blocked from the TTS function.
   - `ext_chat` This enables or disables the extended chat functions.
   - `hw_hum` This is the ALSA hardware number for your pi. 0 is the first sound card and should work for most bots.
   - `type` should be the type of TTS software you are using. The currently supported TTS types are. espeak was installed in the previous steps, and makes a good default tts.
     - `espeak`
     - `fesitval`
     - `pico`
     - Amazon Polly (`polly`)
     - `cozmo_tts`
     - `google_cloud`

### Setting up your start_robot file on the Raspberry Pi

1. Copy the `start_robot` script to your home directory.

   ```sh
   cp ~/car_controll_system/scripts/start_robot ~
   ```

2. Add the startup script to the `crontab`

   ```sh
   crontab -e
   ```

   Note: If you accidently use the wrong editor try

   ```sh
   EDITOR=nano crontab -e
   ```

3. Insert the following text at the bottom

   ```sh
   @reboot /bin/bash /home/pi/start_robot
   ```

   Example:

   ```sh
   # Edit this file to introduce tasks to be run by cron.
   #
   # Each task to run has to be defined through a single line
   # indicating with different fields when the task will be run
   # and what command to run for the task
   #
   # To define the time you can provide concrete values for
   # minute (m), hour (h), day of month (dom), month (mon),
   # and day of week (dow) or use '*' in these fields (for 'any').#
   # Notice that tasks will be started based on the cron's system
   # daemon's notion of time and timezones.
   #
   # Output of the crontab jobs (including errors) is sent through
   # email to the user the crontab file belongs to (unless redirected).
   #
   # For example, you can run a backup of all your user accounts
   # at 5 a.m every week with:
   # 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
   #
   # For more information see the manual pages of crontab(5) and cron(8)
   #
   # m h  dom mon dow   command

   @reboot /bin/bash /home/pi/start_robot
   ```

4. Now just plug in the Camera and USB Speaker and reboot

   ```sh
   sudo reboot
   ```


### Block Diagram
<p align="center">
   <img src="./images/block_diagram.png" alt="Block Diagram" style="width:80%;text-align:justify;"/>
</p>

### Circuit Diagram
<p align="center">
   <img src="./images/circuit_diagram.png" alt="Circuit Diagram" style="width:75%;text-align:justify;"/>
</p>

### Assembled Model

<p align="center">
   <img src="./images/assemble_demo_1.jpg" alt="Assembled Model" style="width:75%;text-align:justify;"/>
</p>

<p align="center">
   <img src="./images/assemble_demo_2.jpg" alt="Assembled Model" style="width:75%;text-align:justify;"/>
</p>

### Controller Ui
<p align="center">
   <img src="./images/controller_ui_with_video_1.png" alt="controller ui" style="width:75%;text-align:justify;"/>
</p>

<p align="center">
   <img src="./images/controller_ui_with_video_2.png" alt="controller ui" style="width:75%;text-align:justify;"/>
</p>
