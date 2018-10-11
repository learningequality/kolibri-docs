Raspberry Pi
============

This is a draft that is not yet included in the TOC.

Prerequisites
-------------

* Raspberry Pi Model 3+
* Formatted MicroSD Card > 4GB (64 GB recommended or attached USB storage)
* Card reader for a laptop or computer to write to the MicroSD card
* Latest Raspbian Stretch OS .img file
  * `Raspbian Desktop <http://downloads.raspberrypi.org/raspbian/>`__
  * `Raspbian Lite <http://downloads.raspberrypi.org/raspbian_lite/>`__
* **Or** `Installation of Raspbian via NOOBS <https://www.raspberrypi.org/documentation/installation/noobs.md>`__
* Internet connectivity (for setting up the device)

Getting started guides
----------------------

https://projects.raspberrypi.org/en/projects/raspberry-pi-getting-started
https://www.raspberrypi.org/documentation/installation/installing-images/README.md

Setting up the SD card
----------------------

Updating the software
---------------------

After installation, it is recommended that you upgrade all the software on the device:
  
.. code-block:: bash

  sudo apt update
  sudo apt upgrade

Updating the firmware
---------------------

Run ``sudo rpi-update`` to update the firmware. This may not bring any necessary changes, but it's always recommended. You cannot replicate this by copying MicroSD cards, you would have to repeat this step for every Raspberry Pi device that you are installing.

General system configuration
----------------------------

Run ``sudo raspi-config`` for the general setup options such as keyboard layout, timezone etc.


Setting up a hotspot
--------------------

Setting up a "Captive portal"
-----------------------------

Attaching USB storage
---------------------

Many people have a 4 GB or 16 GB MicroSD card that came along with the Raspberry Pi. In order to have more content, such as the full Khan Academy, you may want to attach a USB storage media -- a flash device or a hard drive.

.. tip:: Moving content: If you have a USB source for additional storage, you can use the ``kolibri manage movedirectory`` command or create your own symbolic links to have the data folder located elsewhere.
  
    Using the built-in management command:

    .. code-block:: bash

        # Stop kolibri
        sudo systemctl kolibri stop
        # Move the data
        kolibri manage movedirectory /path/to/your/external_drive
        # Start kolibri
        sudo systemctl kolibri start
        
  
    **Or** using symbolic links, you need to start and stop Kolibri and to set the permissions correctly:

    .. code-block:: bash

        # Stop kolibri
        sudo systemctl kolibri stop
        # Move its data
        sudo mv /var/kolibri/.kolibri /your/external/media/kolibri_data
        # Ensure that the kolibri system service user owns the folder
        sudo chown -R `cat /etc/kolibri/username` /your/external/media/kolibri_data
        # Restore the original location with a symbolic link
        sudo ln -s /your/external/media/kolibri_data /var/kolibri/.kolibri
        # Start kolibri
        sudo systemctl kolibri start


Saving your image for replication
---------------------------------


