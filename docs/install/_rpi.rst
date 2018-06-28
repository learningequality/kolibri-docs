.. _rpi:

Raspbian
========

Compatibility
-------------

Kolibri currently doesn't work out of the box for Raspbian Jessie. We are refining our distribution to work out of the box, but you can follow the below steps in order to install it (tested on Kolibri v0.9).

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

        sudo systemctl kolibri stop  # Stop kolibri
        sudo mv /var/kolibri/.kolibri /your/external/media/kolibri_data  # Move its data
        sudo chown -R kolibri /your/external/media/kolibri_data  # Ensure that the kolibri user owns the folder
        sudo ln -s /your/external/media/kolibri_data /var/kolibri/.kolibri  # Restore the original location with a symbolic link
        sudo systemctl kolibri start  # Start kolibri

  * Loading channels can take a **long time** on a Raspberry Pi. When generating channel contens for Khan Academy, the step indicated as "Generating channel listing. This could take a few minutes…" could mean ~30 minutes. The device's computation power is the bottleneck. You might get logged out while waiting, but this is harmless and the process will continue. Sit tight!


Uninstall
---------

From the command line: ``sudo apt-get remove kolibri``.


Upgrade
-------

When you use the PPA installation method, upgrades to newer versions will be automatic, provided there is internet access available.
