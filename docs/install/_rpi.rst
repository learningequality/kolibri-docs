.. _rpi:

Raspberry Pi
============

There are several varieties of operating systems for Raspberry Pi. This guide is intended for and tested on `Raspbian <https://http://raspbian.org//>`__, the most popular choice of OS, based on Debian. To obtain and install Raspbian, refer to the official documentation.

Kolibri is intended for **Raspberry Pi Model 3** and upwards.

.. tip:: Read our :ref:`Raspberry Pi Tutorial for Kolibri <tutorial_rpi>`.

.. warning:: These steps require an internet connection during the installation. After completing the installation, it's possible :ref:`to replicate an image <rpi_replication>` for offline installation.


Install
-------

#. We need to upgrade the ``python3-cffi`` library, which is outdated on Raspbian. Upgrade it like this:

   .. code-block:: bash

      sudo apt install libffi-dev python3-pip python3-pkg-resources dirmngr
      sudo pip3 install pip setuptools --upgrade
      sudo pip3 install cffi --upgrade

#. Add our Ubuntu PPA with these special instructions:

   .. code-block:: bash

      sudo su -c 'echo "deb http://ppa.launchpad.net/learningequality/kolibri/ubuntu xenial main" > /etc/apt/sources.list.d/learningequality-ubuntu-kolibri-xenial.list'
      sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys DC5BAA93F9E4AE4F0411F97C74F88ADB3194DD81
      sudo apt update
      sudo apt install kolibri

   When asked questions during the installation, it is recommended that you use the default ``pi`` user for running Kolibri because it will have access to USB devices.

#. When the command finishes, open the default browser at http://127.0.0.1:8080 and proceed with the :ref:`setup_initial` of your facility. 


.. note:: The following issues are quite common on a Raspberry Pi:

  * **System time** isn't set properly or resets during power-off. This causes errors while downloading software. For instance, SSL certificates for online sources will fail to validate. Ensure that you have the right timezone in ``/etc/timezone`` and that the clock is set properly by running ``sudo ntpd -gq``.

  * **Storage space** is often scarce. If you have a USB source for additional storage, you can use the ``kolibri manage movedirectory`` command or create your own symbolic links to have the data folder located elsewhere.
  
    Using the built-in management command:

    .. code-block:: bash

        # Stop kolibri
        sudo systemctl kolibri stop
        # Move the data
        kolibri manage movedirectory /path/to/your/external_drive
        # Start kolibri
        sudo systemctl kolibri start

  * **I/O operations are slow**: This means that a typical bottleneck on a Raspberry Pi is file transfer to/from MicroSD card or USB attached storage. Once Kolibri is up and running, this will not be a bottleneck, but while copying initial contents of several gigabytes, you will experience this. Both the SD card reader and the USB ports will limit you at 50-80MB/sec. From our experience, it doesn't matter much whether you are using the main SD card reader for storage or some media connected to your USB, as in principle they both reach about the same maximum speeds. However, you may find significant differences in the speeds of individual SD Cards.

    When replicating installations, you can save time if you connect the SD card of USB storage to another device with faster transfer speeds. Replication will be described in future guides.


Uninstall
---------

From the command line: ``sudo apt-get remove kolibri``.


Upgrade
-------

When you use the PPA installation method, upgrades to newer versions will be automatic, provided there is internet access available.
