## **Environment**
### **Hardware**
Raspberry Pi 3

### **OS**
Raspbian Buster Lite:
- Version: February 2020
- Release date: 2020-02-05
- Kernel version: 4.19
- Size: 433 MB

## **Python requierments**
Minimum python version requierment 3.7.x

### **Python packages requierments**
**pip**
``` bash
$ sudo apt install python3-pip -y
```

**[python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)**
``` bash
$ pip install python-telegram-bot --upgrade
```

**[requests](https://github.com/psf/requests)**
``` bash
$ pip install requests
```

**[googleapiclient](https://developers.google.com/docs/api/quickstart/python)**
``` bash
$ pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

**[oauth2client](https://github.com/googleapis/oauth2client)**
``` bash
$ pip install --upgrade oauth2client
```

**[python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)**
``` bash
$ pip install python-telegram-bot --upgrade
```

**[smbus2](https://www.gotronic.fr/pj2-sbc-lcd20x4-fr-1440.pdf)**
``` bash
# GPIO library
$ sudo apt-get install python-pip python-dev build-essential
$ sudo pip install RPi.GPIO

# Python library
$ sudo apt-get install python-imaging

# I2C library
$ sudo apt-get install python-smbus i2c-tools

# Enable I2C bus in Raspberry Pi configuration
$ sudo raspi-config # select 'Advanced options' > 'I2C'

# Update modules file
$ sudo nano /etc/modules
# Paste the lines
i2c-bcm2708
i2c-dev

# Restart Raspberry Pi
$ sudo shutdown -hr now

# Get memory address of i2c display
$ sudo i2cdetect -y 1 # if number display 27 in the console, the address is 0x27
```


## **Use project**

### **Get project**
```bash
# SSH
git clone git@github.com:maximedezette/systeme-embarque.git
# HTTPS
git clone https://github.com/maximedezette/systeme-embarque.git
# Curl
curl https://github.com/maximedezette/systeme-embarque/archive/master.zip -o python-telegram-bot.zip
```
