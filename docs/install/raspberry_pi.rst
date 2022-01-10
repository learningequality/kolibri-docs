.. _rpi:


Raspberry Pi
------------

Kolibri is tested to work on Raspberry Pi Models **3, 3+, 4 and Zero W**.

Kolibri may also run on Raspberry Pi Model 2, but the platform has not been tested on that model, and it does not have on-board WiFi.


Disk image
==========

If you are starting a new Raspberry Pi installation and want to get set up as quickly as possible, you can download our custom OS image and flash it to your SD card. Once flashed, you can configure your Pi as usual.

Our image provides an out-of-the-box Kolibri experience pre-configurated with a WiFi hotspot and networking. No additional installation steps are needed once the SD card is inserted and the Pi is booted.

To use:

1. Download the `Raspberry Pi ZIP file <https://learningequality.org/download/>`_ for Kolibri **version** |version-b|, or have it copied to your local drive.
2. Use any of the methods explained in the `official Raspberry Pi user guide <https://www.raspberrypi.com/documentation/computers/getting-started.html>`_ to write the image to a SD card.
3. Insert the SD card in the Raspberry Pi.
4. Power on the Raspberry Pi and wait. The process takes less than 5 minutes in a model 4, but in other models can take longer. You may observe some ``Failure`` messages during this process, which is normal.

.. warning:: After installing the image, an ssh server is installed with the user ``pi`` and the password ``kolibrifly``. You should immediately change the password to ensure that your server is secure.

After following the above steps the Raspberry Pi will provide a WiFi network named under the ssid ``kolibri`` without any password. The Kolibri server will be accessible at the URL ``http://10.10.10.10``.

By default the server does not have Internet access. To import resources to Kolibri, either connect a USB drive with exported channels, or connect the Pi to an internet-connected router using the ethernet cable.


.. note:: The installed system contains a full RPi image, with all the software included in the ``Lite`` version from https://www.raspberrypi.org/software/operating-systems/#raspberry-pi-os-32-bit. After login use ``sudo raspi-config`` to customize the environment, including localization, timezone, etc. if desired.


.. note:: When an ethernet cable with Internet access is connected to the Raspberry, it will have internet connectivity but won't provide this connectivity to the devices that are connected to its ``kolibri`` ssid. These devices will only be able to use the browser with the Kolibri application at the URL ``http://10.10.10.10``.


Debian package
==============

If you already have a running Raspberry Pi set up or if you prefer to set up manually from an official Pi image, we recommend installing the :ref:`Kolibri Server Debian package <kolibri_server_package>`, which includes important optimizations such as static content caching and optimized CPU usage.

Manual configuration of networking and WiFi on the Pi are outside the scope of these instructions.
