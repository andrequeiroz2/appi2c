# appi2c
MQTT device administrator

Technology.
  - Flask
  - Sqlite
  - SQLAlchemy
  - Python
  - Bulma
  - jquery-confirm, jquery-UI, jquery Finger, Ajax
  - ApexChart
  - MQTT

### What does it really do?
Register your MQTT Brokers, register your mqtt devices can be sensors or actuators.
Distribute your devices in groups and manage information in real time.
Drag and position the representation of your devices on a blue print,
click on them to publish commands, double-click and follow the information.
![](img/blue_print.jpg)

![](img/data_sensor.jpg)

### Installation

Clone the project.
```sh
git clone https://github.com/andrequeiroz2/appi2c.git
```
Install and activate virtulenv
```sh
$ cd appi2c
$ pip install virtualenv
$ source env/bin/activate
```
Insttal requeriments
```sh
$ pip install -r requirements.txt 
```
Starting Data Base and Populate tables
```sh
$ cd appi2c
$ flask populate-type
$ flask populate-icon
```
Run appi2c
```sh
$ flask run
```

### Todos

 - More Tests.
 - Add new type devices.
 - Triggers.
 - Alert.
 - etc..

License
----

MIT


**Free Software, Hell Yeah!**
