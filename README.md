## LGSM_webpanel

A webpanel for Linux Game Server Manager which works even better with source servers.


## Features

For every servers supported by LGSM:

* Start
* Stop
* Restart
* Update
* Responsive AI

For source based servers (even the ones not using LGSM):

* Players stats monitoring
* Current map (TBA)
* More (TBA)

## Installation

**1. Installing dependencies**

```sh
sudo apt-get update && sudo apt-get install apache2 python3 python3-pip libapache2-mod-wsgi-py3
```

**2. Installing Python modules**

Create a file named 'requirements.txt' in your home directory

```sh
cd
nano requirements.txt
```

Paste this, then save and exit by pressing Ctrl+O then Ctrl+X
```
Django==3.0.5
django-chartjs==2.0.0
django-common-helpers==0.9.2
django-crispy-forms==1.9.0
django-cron==0.5.1
django-crontab==0.7.1
django-picklefield==2.1.1
django-q==1.2.1
django-suit==2.0a1
python-a2s==1.1.4
valve==0.0.0
python-a2s
```

Then install the modules
```
sudo pip3 install -r requirements.txt
```


**3. Adding the LGSM_webpanel files to your server**
```
sudo mkdir /var/www/LGSM_webpanel
cd /var/www/LGSM_webpanel
sudo git clone 
```
