# KATALYST


### Why we started?

* Repetition of Design Work
* Difficulties in sharing of specifications between Designers and Developers


### Architecture:

![Architecture](architecture.png?raw=true)

### Output:
Not only layouts, we generated almost all resources required for Android Development:
* Colors
* Strings
* Dimensions
* Image Assets and Drawables


### Design mock-up:
![Design mock-up](mockup.png?raw=true)


### Actual outcome:

![Actual outcome](output.png?raw=true)


### Requirements:
* python 2.x
* [lxml](http://lxml.de/)
* [cario](https://www.cairographics.org/pycairo/)
* [python-rsvg](http://packages.ubuntu.com/xenial/python-rsvg)

```bash
$ sudo apt-get install python-lxml
$ sudo apt-get install python-cairo python-gobject-2 python-gtk2
# python-rsvg for ubuntu 16.04 - 64bit
$ wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gnome-python-desktop/python-rsvg_2.32.0+dfsg-3_amd64.deb
$ sudo dpkg -i python-rsvg_2.32.0+dfsg-3_amd64.deb
```


### Usage:
```bash
$ python main.py
```