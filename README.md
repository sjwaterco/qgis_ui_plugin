# QGIS UI Plugin

This plugin was developed to support CLWSC's GDI Desktop application. GDI 
Desktop is built on QGIS. The plugin removes all of the toolbars from a default 
install of QGIS and then adds a custom search dialog. The goal of this plugin is 
to greatly dumb-down the QGIS default user interface for people that don't have 
any experience using QGIS let a lone a traditional desktop GIS application.

## Quickstart

In order to make this plugin work for you, you'll need to make several 
modifications to the code. First, we add a search module to QGIS. This search
module queries SJWC databases. Modify [app/clwscdw.py](app/clwscdw.py) and/or 
[app/search.py](app/search.py) depending on what you're trying to accomplish.

Second, we use the Google Maps API to geocode certain addresses. If you want to
use this functionality (used in the searches module) you'll need to modify this 
key (in [app/google.py](app/google.py)).

Finally, we log user feedback from the application in
[http://www.pivotaltracker.com](Pivotal Tracker). If you want to use this
functionality, you'll need your own API key and/or system. Otherwise, you'll
need to remove this functionality. See comments in
[app/clwscdesktopdialog.py](app/clwscdesktopdialog.py).

Note that it will be *critical* to remove the
```
import _winreg
```
from these files if you're running the plugin on a non-windows OS.  

In order to modify the user interface graphically, you'll need to download
[http://www.qt.io/download/](QT). This is freely available (the community
edition should be sufficient) and the learning  curve is not terribly steep.
You'll modify the .ui files in the main directory.

We welcome pull requests and code cleanup. Send inquiries about functionality
and requests to [aaron.gundel@sjwater.com](aaron.gundel@sjwater.com)