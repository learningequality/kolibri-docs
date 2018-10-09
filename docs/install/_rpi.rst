.. _rpi:

Raspberry Pi
============

There are several varieties of operating systems for Raspberry Pi. This guide is intended for and tested on `Raspian <https://www.raspberrypi.org/>`__, the most popular choice of OS, based on Debian. To obtain and install Raspbian, refer to the official documentation.

Kolibri is intended for **Raspberry Pi Model 3** and upwards.

.. note:: The standard Raspbian choice has a graphical desktop. But you can also install **Raspbian Lite** that uses less resources but only has a command line interface. This documentation works seemlessly on both, but you might find that some packages are already installed in the desktop version of Raspbian.


Install
-------

#. We need to upgrade the ``python3-cffi`` library, which is outdated on Raspbian. Upgrade it like this::

      sudo apt install libffi-dev
      sudo pip3 install pip --upgrade
      sudo pip3 install cffi --upgrade
      sudo systemctl start kolibri

  .. warning:: If you are installing Kolibri on the older **Raspbian Jessie** which is from before August 2017, you need to complete a few extra steps:
  
     ::
    
        sudo apt install python3-pip python3-pkg-resources
        sudo pip3 install setuptools --upgrade

#. Add our Ubuntu PPA with these special instructions::

      sudo apt install dirmngr
      sudo su -c 'echo "deb http://ppa.launchpad.net/learningequality/kolibri/ubuntu xenial main" > /etc/apt/sources.list.d/learningequality-ubuntu-kolibri-xenial.list'
      sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys DC5BAA93F9E4AE4F0411F97C74F88ADB3194DD81
      sudo apt update
      sudo apt install kolibri

#. When the command finishes, open the default browser at http://127.0.0.1:8080 and proceed with the :ref:`setup_initial` of your facility. 


.. note:: The following issues are quite common on a Raspberry Pi:

  * **System time** isn't set properly or resets during power-off. This causes errors while downloading software. For instance, SSL certificates for online sources will fail to validate. Ensure that you have the right timezone in ``/etc/timezone`` and that the clock is set properly by running ``sudo ntpd -gq``.

  * **Storage space** is often a scarcety. If you have a USB source for additional storage, you can use a ``kolibri`` management command or create your own symbolic links to have the data folder located elsewhere.
  
    Using the built-in management command::
      
        # Stop kolibri
        sudo systemctl kolibri stop
        # Move the data
        kolibri manage movedirectory /path/to/your/external_drive
        # Start kolibri
        sudo systemctl kolibri start
        
  
    Using symbolic links, you need to start and stop Kolibri and to set the permissions correctly::

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

  * **I/O operations are slow**, this means that a typical bottleneck on a Raspberry Pi is file transfer. Once Kolibri is up and running, this will not be a bottleneck, but while copying initial contents of several gigabytes, you will experience this. Both the SD card reader and the USB ports will limit you at 50-80MB/sec. From our experience, it doesn't matter much whether you are using the main SD card reader for storage or some media connected to your USB. But you might save time if you can connect the SD card of USB storage to another device with faster transfer speeds, especially if you are replicating from other installations.


Uninstall
---------

From the command line: ``sudo apt-get remove kolibri``.


Upgrade
-------

When you use the PPA installation method, upgrades to newer versions will be automatic, provided there is internet access available.
