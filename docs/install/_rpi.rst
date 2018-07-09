.. _rpi:

Raspbian
========

Compatibility
-------------

Kolibri works well on Debian-based distributions for `Raspberry Pi <https://www.raspberrypi.org/>`_, such as Raspbian, and has been tested on RPi 3 models.

Install
-------

1. Running ``add-apt-repository`` as shown in the PPA instructions does not work. Instead, run::

      sudo su -c 'echo "deb http://ppa.launchpad.net/learningequality/kolibri/ubuntu xenial main" > /etc/apt/sources.list.d/learningequality-ubuntu-kolibri-xenial.list'
      sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys DC5BAA93F9E4AE4F0411F97C74F88ADB3194DD81
      sudo apt update
      sudo apt install kolibri

2. Kolibri does not start after installation. This is because ``python3-cffi`` is outdated on Raspbian. Upgrade it like this::

      sudo apt install libffi-dev
      sudo pip3 install pip --upgrade
      sudo pip3 install cffi --upgrade
      sudo systemctl start kolibri

3. When the command finishes, open the default browser at http://127.0.0.1:8080 and proceed with the :ref:`setup_initial` of your facility. 


.. note:: The following issues are quite common on a Raspberry Pi:

  * The time isn't set properly and you will have errors downloading software. For instance, SSL certificates for online sources will fail to validate. Ensure that you have the right timezone in ``/etc/timezone`` and that the clock is set properly by running ``sudo ntpd -gq``.

  * You run out of storage space. If you have a USB source for additional storage, do something like this::

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

  * Loading channels can take a **long time** on a Raspberry Pi. When generating channel contents for Khan Academy, the step indicated as "Generating channel listing. This could take a few minutes…" could mean ~30 minutes. The device's computation power is the bottleneck. You might get logged out while waiting, but this is harmless and the process will continue. Sit tight!


Uninstall
---------

From the command line: ``sudo apt-get remove kolibri``.


Upgrade
-------

When you use the PPA installation method, upgrades to newer versions will be automatic, provided there is internet access available.
