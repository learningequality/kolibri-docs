.. _lin:

Debian/Ubuntu
=============

Compatibility
-------------

Debian/Ubuntu 14.04, 16.04 and up - anything that's *not* end-of-life

.. _ppa:

Install from PPA repository
---------------------------

Use the following commands in `Terminal <https://help.ubuntu.com/community/UsingTheTerminal>`_ to add the PPA and install Kolibri:

.. code-block:: bash

    sudo apt-get install software-properties-common python-software-properties
    sudo add-apt-repository ppa:learningequality/kolibri
    sudo apt-get update
    sudo apt-get install kolibri


.. _lin_deb:

Install from a .deb file
------------------------

The advantages of downloading a ``.deb`` file is the portability: you can copy the file from device to device and install Kolibri without internet access.

#. Download the latest Kolibri `.deb installer <https://learningequality.org/r/kolibri-deb-latest>`_, or have it copied to your local drive.
#. Run this command from the location where you downloaded the ``DEB`` file:

   .. code-block:: bash

       sudo dpkg -i kolibri-installer-filename.deb

#. Wait for the installation to finish and run this command to start Kolibri:

   .. code-block:: bash

       kolibri start

   .. note:: If you choose to install Kolibri as a system service, you will not need to start it manually.

#. When the command finishes, open the default browser at http://127.0.0.1:8080 and proceed with the :ref:`setup_initial` of your facility. 


Uninstall
---------

* Open **Software** on Ubuntu and locate the Kolibri. Press **Remove**.
* Or from the command line: ``sudo apt-get remove kolibri``.


Upgrade
-------

When you use the PPA installation method, upgrades to newer versions will be automatic, provided there is internet access available.

To upgrade Kolibri on a Debian device without internet access, bring the updated ``.deb`` file and follow the same steps as in :ref:`lin_deb`.


.. _changing-system-user:

Changing the owner of Kolibri system service
--------------------------------------------

If you installed Kolibri from the ``DEB`` file **prior to v0.10**, the new account named ``kolibri`` was created as the default user account (*owner*) of the system service. This configuration worked well in most cases, but it did not allow Kolibri the access to the local USB drives. From Kolibri v0.10 on, we have changed the system service configuration to select the default desktop user's account as the service owner.

When you upgrade Kolibri **to v0.10 and later** using the ``DEB`` file, you will need to change the user account who owns the system service, move the data (user and content databases) and assign the owner permissions to your desktop user. To change the owner, follow these steps. 

.. code-block:: bash

	# Stop kolibri
	sudo service kolibri stop
	# Move data to your desktop user:
	sudo mv /var/kolibri/.kolibri /home/$USER/.kolibri
	# Change ownership
	sudo chown -R $USER /home/$USER/.kolibri
	# Change the username configuration
	sudo echo -n $USER > /etc/kolibri/username
	# Start kolibri again
	sudo service kolibri start

.. note:: Replace the ``$USER`` in commands above with the name of the user you wish to be the new Kolibri system service owner.