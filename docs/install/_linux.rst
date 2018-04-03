.. _lin:

Debian/Ubuntu Linux
===================


Install from PPA repository
---------------------------

Use the following commands in Terminal to add the PPA and install Kolibri:

.. code-block:: bash

    sudo add-apt-repository ppa:learningequality/kolibri
    sudo apt-get update
    sudo apt-get install kolibri


.. _lin_deb:

Install from a .deb file
------------------------

The advantages of downloading a ``.deb`` file concern portability: If you need to install Kolibri on devices without internet access, you can copy the file from device to device.

#. Download the latest Kolibri `DEB installer <https://learningequality.org/r/kolibri-deb-latest>`_, or have it copied to your local drive.
#. Run this command from the location where you downloaded the ``DEB`` file:

   .. code-block:: bash

       sudo dpkg -i kolibri-installer-filename.deb

#. Wait for the installation to finish and run this command to start Kolibri:

   .. code-block:: bash

       kolibri start
	
#. When command finishes, open the default browser at http://127.0.0.1:8080 and proceed with the :ref:`setup_initial` of your facility. 


Uninstall
---------

* Open **Software** on Ubuntu and locate the Kolibri. Press **Remove**.
* Or from command line: ``sudo apt-get remove kolibri``.

Upgrade
-------

Upgrades are automatic when you use the PPA installation method. 
To upgrade Kolibri with a ``.deb``, follow the same steps in :ref:`lin_deb`.
