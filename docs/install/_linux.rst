.. _lin:

Debian/Ubuntu
=============

Compatibility
-------------

Debian 8 (Jessie), Debian 9 (Stretch), Ubuntu 16.04+ and up - anything that's *not* end-of-life. Ubuntu-based distributions count a number of flavors, for instance Xubuntu and Mint.

.. _ppa:

Install from PPA repository
---------------------------

**In Ubuntu-based distributions**, use the following commands in `Terminal <https://help.ubuntu.com/community/UsingTheTerminal>`_ to add the PPA and install Kolibri:

.. code-block:: bash

    sudo apt-get install software-properties-common dirmngr
    sudo add-apt-repository ppa:learningequality/kolibri
    sudo apt-get update
    sudo apt-get install kolibri

**In Debian-based distributions** you need to use these commands to point to our Launchpad PPA:

.. code-block:: bash

    sudo apt-get install dirmngr
    sudo su -c 'echo "deb http://ppa.launchpad.net/learningequality/kolibri/ubuntu cosmic main" > /etc/apt/sources.list.d/learningequality-ubuntu-kolibri-cosmic.list'
    sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys DC5BAA93F9E4AE4F0411F97C74F88ADB3194DD81
    sudo apt-get update
    sudo apt-get install kolibri

Uninstall
*********
From the command line: ``sudo apt-get remove kolibri``.

Upgrade
*******

When you use the PPA installation method, upgrades to newer versions will be automatic, provided there is internet access available.

kolibri-server (pre-release)
****************************

We are finalizing the release of an optimized version of Kolibri for Linux systems called **kolibri-server**. This version is recommended for:

* Clear server-client setup for implementations with many client devices
* When the server device has more than one CPU core

**kolibri-server** has some specific features like **static content cache** and **optimized usage of the CPU processing power** in multi core devices. Typical use case would be a *Raspberry Pi 3+* device with 4 CPU cores, which will perform much better and faster with **kolibri-server** compared to base Kolibri.

To install **kolibri-server** follow these steps.

#. Run these commands in the Terminal:

	.. code-block:: bash

                sudo apt-get install software-properties-common dirmngr
		sudo add-apt-repository ppa:learningequality/kolibri-proposed
		sudo apt-get update
		sudo apt-get install kolibri-server

   During the installation you will be offered the option to choose the port (8000, 80 or leave the default 8080).

#. Restart the system.

.. warning:: * Be advised that this procedure also switches the setup to use the latest built Kolibri pre-release.
	* Keep in mind that the **kolibri-server** system performance will depend not only on server device features, but on local WiFi access point characteristics.

.. _lin_deb:

Install from a .deb file
------------------------

The advantages of downloading a ``.deb`` file is the portability: you can copy the file from device to device and install Kolibri without internet access.

#. Download the latest `.deb installer <https://learningequality.org/download/>`_ for Kolibri **version 0.12**, or have it copied to your local drive.
#. Run this command from the location where you downloaded the ``DEB`` file:

   .. code-block:: bash

       sudo dpkg -i kolibri-installer-filename.deb

#. Wait for the installation to finish and run this command to start Kolibri:

   .. code-block:: bash

       kolibri start

   .. note:: If you choose to install Kolibri as a system service, you will not need to start it manually.

#. When the command finishes, open the default browser at http://127.0.0.1:8080 and proceed with the :ref:`setup_initial` of your facility. 


Uninstall
*********

* Open **Software** on Ubuntu and locate the Kolibri. Press **Remove**.
* Or from the command line: ``sudo apt-get remove kolibri``.


Upgrade
*******

When you use the PPA installation method, upgrades to newer versions will be automatic, provided there is internet access available.

To upgrade Kolibri on a Debian device without internet access, bring the updated ``.deb`` file and follow the same steps as in :ref:`lin_deb`.


.. _changing-system-user:

Changing the owner of Kolibri system service
--------------------------------------------

The *system service* is the script that runs Kolibri in the background when your system boots on Debian-based distributions.

You may need to change the system service to run with the permissions of a different user account. Prior to v0.10, ``kolibri`` user account was the owner of the system service, while from v0.10 and later, desktop user's account is preferred, in order for Kolibri to access the local USB storage.

To change the system service owner, you need to change the configuration of the system service: move the ``.kolibri`` data folder (containing channels, databases etc.), and assign owner permissions to the new user. Follow these steps.

.. code-block:: bash

	# Stop Kolibri
	sudo systemctl stop kolibri
	# Move data to your desktop user:
	sudo mv /var/kolibri/.kolibri /home/$USER/.kolibri
	# Change ownership
	sudo chown -R $USER /home/$USER/.kolibri
	# Change the username configuration
	sudo sh -c 'sudo echo -n $USER > /etc/kolibri/username'
	# Start Kolibri again
	sudo systemctl start kolibri

.. note:: Replace the ``$USER`` in commands above with the name of the user you wish to be the new Kolibri system service owner.


Raspberry Pi
------------

To install Kolibri on RPi refer to our :ref:`Raspberry Pi Tutorial for Kolibri <tutorial_rpi>`.

.. warning:: Kolibri is intended for **Raspberry Pi Model 3** and upwards.
