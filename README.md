<p align="center">
# LGSM_webpanel
</p>
A webpanel for Linux Game Server Manager which works even better with source servers.


## Features

For every servers supported by LGSM:

* Start
* Stop
* Restart
* Update
* Responsive UI

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
```

Then install the modules
```
sudo pip3 install -r requirements.txt
```


**3. Adding the LGSM_webpanel files to your server**
```
sudo mkdir /var/www/LGSM_webpanel
cd /var/www/LGSM_webpanel
sudo git clone https://github.com/Sarrus1/LGSM_webpanel.git
sudo chown www-data:www-data -R /var/www/LGSM_webpanel
```


**4. Configuring the Apache server**

Edit the default Apache2 website config
```
sudo nano /etc/apache2/sites-available/000-default.conf
```

Then copy this at the bottom.
```
Listen 1337

<VirtualHost *:1337>
        <Directory /var/www/LGSM_webpanel/LGSM_webpanel>
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>

        ErrorLog ${APACHE_LOG_DIR}/LGSM-error.log
        CustomLog ${APACHE_LOG_DIR}/LGSM-access.log combined
        WSGIScriptAlias / /var/www/LGSM_webpanel/LGSM_webpanel/wsgi.py
        WSGIDaemonProcess LGSM_webpanel python-path=/var/www/LGSM_webpanel
        WSGIprocessGroup LGSM_webpanel
        DocumentRoot /var/www
</VirtualHost>

WSGIPythonPath /var/www/LGSM_webpanel
```

Press Ctrl+O then Ctrl+X to save and exit.

**5. Changing the permissions for the game server**

For each game server, give ownership of the server files to www-data.
```
sudo chown www-data -R /home/gameserver
```

**6. Create a user for the webinterface**

Type this command to add a superuser to the webinterface.
```
sudo python3 /var/www/LGSM_webpanel/manage.py createsuperuser
```
And then enter new credentials for the user.


**7. Create a Secret Key for the webinterface**

Create a Secret Key on https://miniwebtool.com/fr/django-secret-key-generator/, then paste it in settings.py
```
sudo nano /var/www/LGSM_webpanel/LGSM_webpanel/settings.py
```

**8. Restart Apache2 and enable changes**

Restart Apache and give enable wsgi.
```
sudo a2enmod wsgi
sudo service apache2 restart
```

**You can now access the webinterface at http://ipadress:1337**
