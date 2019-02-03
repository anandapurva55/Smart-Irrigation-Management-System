# Smart-Irrigation-Management-System

Idea - We have local nodes situated on the field and a remote central server. Local nodes collect soil data such as soil moisture and stagnant water level through soil moisture sensors and stagnant water level sensors respectively and send to the central server using any appropriate medium like email. The central server analyzes the data and sends back instructions to irrigate with the required amount of water. Now coming back to the field, motors start and irrigation is performed.

Prototyped model:-

We developed a basic prototype using Arduino Uno and Raspberry Pi 3 Model B+. Arduino Uno acted as a local node and Pi as the central server. Soil moisture sensor and DC water motor were also used. Soil moisture data were collected in Arduino and was being sent to the Pi and then power to the water motor(which was connected to the local node) was provided depending on the instructions from the Pi to perform the irrigation. Serial communication was established for communication between the Arduino and Raspberry Pi using PyFirmata library file in Arduino Ide.

Implementation steps :-

1) Install Arduino Ide on Raspberry Pi by typing the following command on it's command line:

          sudo apt-get -y install arduino python-serial mercurial

2) Install pyFirmata files on Raspberry Pi using the following commands :

          git clone https://github.com/tino/pyFirmata

          cd pyFirmata

          sudo python setup.py install

3) Upload PyFirmata file on Arduino Board  by clicking File -> Examples ->  Firmata -> Standard Firmata and then click upload button .

4) Run the code uploaded in the file raspberryPi.py on Raspberry Pi.









