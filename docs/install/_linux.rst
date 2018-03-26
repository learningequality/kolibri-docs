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

The advantage of having a ``.deb`` file is about portability. If you need to
install Kolibri on devices without internet access, you can copy the file from
device to device.

#. Go to `learningequality.org/download <https://learningequality.org/download/>`__ and download the latest version (or have it copied to your local drive).
#. Download the Kolibri installer  (``DEB`` file).
#. Run the command:

   .. code-block:: bash

       sudo dpkg -i kolibri-installer-filename.deb

#. Wait for the installation to finish and run this command to start Kolibri:

   .. code-block:: bash

       kolibri start
	
#. When command finishes, open the default browser at http://127.0.0.1:8080 and proceed with the :ref:`setup_initial` of your facility. 


Uninstall
---------

* Open **Software** on Ubuntu and locate the Kolibri. Press **Remove**.

OR

* Use ``sudo apt-get remove <name of package>``. You need to know the exact name of the package you installed, most probably ``kolibri``.

Upgrade
-------

Upgrades are automatic when you use the PPA installation method. 
To upgrade Kolibri with a ``.deb``, follow the same steps in :ref:`lin_deb`.
