.. _rpi:


Raspberry Pi
------------

Kolibri is tested to work on Raspberry Pi Models **3, 3+, 4 and Zero W**.

Kolibri may also run on Raspberry Pi Model 2, but the above tutorial was not fully intended for that model, since it does not have on-board WiFi.


Quick start
===========

If you are starting from a brand new Raspberry Pi and want to get set up as quickly as possible, you can download our custom OS image and flash it to your SD card. Once flashed, you can configure your Pi as usual.

If you already have a Pi running and don't want to erase it, or if you would like to learn more about how to set up the system from scratch, see our :ref:`Raspberry Pi Tutorial for Kolibri <rpi_manual>`. 

.. warning:: After installing the image, a ssh server is installed with the user ``pi`` and the password ``kolibrifly``. You should immediately change the password to ensure that your server is secure.


1. Download the `Raspberry Pi ZIP file <https://learningequality.org/download/>`_ for Kolibri **version 0.13**, or have it copied to your local drive.
2. Use any of the methods explained in the `official Raspberry Pi user guide <https://www.raspberrypi.org/documentation/installation/installing-images/README.md>`_ to write the image to a SD card.
3. Insert the SD card in the Raspberry Pi.
4. Power on the Raspberry Pi and wait. The process takes less than 5 minutes in a model 4, but in other models can take longer. You may observe some ``Failure`` messages during this process, which is normal.


After following the above steps the Raspberry Pi will provide a WiFi network named under the ssid ``kolibri`` without any password. The Kolibri server will be accessible at the URL ``http://10.10.10.10``.

By default the server does not have Internet access. To add content to Kolibri, either connect a USB drive with content, or connect the Pi to an internet-connected router using the ethernet cable.


.. note:: The installed system contains a full Raspbian image, with all the software included in the ``lite`` version from https://www.raspberrypi.org/downloads/raspbian/. After login use ``sudo raspi-config`` to customize the environment, including localization, timezone, etc. if desired.


.. note:: When an ethernet cable with Internet access is connected to the Raspberry, it will have internet connectivity but won't provide this connectivity to the devices that are connected to its ``kolibri`` ssid. These devices will only be able to use the browser with the kolibri application at the ``http://10.10.10.10`` url.


Manual setup
============

It is not necessary to use the custom OS image. If you already have a running Raspberry Pi set up and want to install Kolibri, or if you prefer to set up manually from an official Pi image, please refer to our :ref:`Raspberry Pi Tutorial for Kolibri <rpi_manual>`. 
