
.. _provision:

Provisioning many servers
=========================

This tutorial will help you to prepare for the Kolibri implementation where you need to install and provision several Kolibri server devices with the same content channels.

Provisioning multiple servers with software and content is **going to take some time** irregardless of the chosen procedure. 

You will need an **active Internet connection only to preload content channels on the first server device**. Provisioning the rest of the servers can be accomplished offline, or just within the working local network.

Required hardware
-----------------

#. Laptops and/or other devices to host Kolibri servers. 

	.. commenting out for now until the tutorial is updated.
		.. tip:: If you are planning to use Raspberry Pi as your server device, read our comprehensive tutorial about setting up :ref:`tutorial_rpi`.

#. For provisioning you have the option to use:

	* Fast USB 3 external drive(s). USB 2 can work too, but we recommend using more than one USB 3 drives for fastest results.

		**OR**

	* Working LAN (cabled is preferable to wireless, and ideally via a router that supports Gigabit Ethernet).

#. Active Internet connection to download the installer and preload content channels on the first (“master”) server.

We recommend you install and preload content channels on one server (referring to it as the *master* for the purpose of this procedure), and then copy the required folder structure to the rest of the devices.

Copying the folders with content from the master server hard drive to others via the USB 3 external drive might be faster, but copying via the cabled LAN connection may be done in parallel (from master to several others at the same time). You can combine these two options for the fastest results, if you have access to both cabled LAN and the USB external drives.

Provision the master server
---------------------------

#. Install Kolibri on the master server by following the steps for your :ref:`chosen platform <install>`.
#. Proceed with the :ref:`setup_initial` of the facility on the master server.
#. :ref:`Import the desired content <import_studio>` to preload it on the master server.


Kolibri folder structure
************************

At this point you have the master server set-up and preloaded with content. Before you proceed to copy the content and the database to the rest of the server devices, let’s get familiar with the Kolibri folder structure.

* On Windows, the main server database and all the files related to the content are stored in the folder named ``.kolibri``, located in ``C:/Users/<username>/.kolibri/`` (if your main hard drive is ``C:``).

	``<username>`` refers to the user you were logged in as when you installed Kolibri as explained above. In the image below for example, you can see that the user who installed Kolibri is called **IEUser**.

	.. figure:: /img/IEUser.gif
	    :alt:  

	    Find the `.kolibri` folder on Windows.

* On Linux the ``.kolibri`` folder is located inside your user home folder.
  
	.. figure:: /img/linux.kolibri.png
	    :alt:  

	    Find the `.kolibri` folder on Linux.

The content of the ``.kolibri`` folder is the same for all platforms. Inside you can see the main database file ``db.sqlite3``, and the subfolder named ``content`` which contains 2 subfolders: ``databases`` with the separate database for each of the content channels imported into Kolibri, and the ``storage`` folder with all the content files and resources.

.. figure:: /img/db-and-content.gif
    :alt:  

    Find the channel's databases and content folder.


Prepare the ``.kolibri`` folder for copying
*******************************************

Before you proceed to copy the ``.kolibri`` folder from the master server hard drive (which already contains content channels), to the rest of the server devices for your deployment, you need to **deprovision** (that is, empty out) the user database.

.. warning:: This is a critical step, to ensure that each destination server has a unique **Facility ID** (and name) associated with it.

#. Open the Terminal on Linux or the :ref:`command prompt on Windows <command_line>`.

#. Stop Kolibri server with the following command

	.. code-block:: bash

	  kolibri stop

#. Follow that with the command to empty the user database.

	.. code-block:: bash

  		kolibri manage deprovision

	
	You will have to confirm twice by typing ``yes`` and pressing the :guilabel:`Enter` key.


Copy the content to other server devices
----------------------------------------

.. warning:: 
	#. Independent from the copying procedure you decide to use, you should first proceed to :ref:`install Kolibri <install>` on each of the destination devices, following the same steps as for the master server, **but you don’t need to go through the Initial Setup**.

	#. After the installation you must **stop Kolibri** on the destination device, before you proceed to copy the content.

		* On Windows you need to right-click the Kolibri icon in the Windows taskbar (usually at bottom right, near the clock), and select ``Exit``. You will be prompted to confirm the selection, after which Kolibri will stop. 

		.. figure:: /img/taskbar-options.png
			:alt: When you right click the Kolibri taskbar icon, you can see the taskbar options.

			Stop Kolibri from the taskbar options.


		* On Linux you need to run ``kolibri stop`` or ``sudo service kolibri stop`` (if you installed Kolibri to run as the system service).


Use the external USB drive to copy content
******************************************

#. Copy the ``.kolibri`` folder from the master server hard drive, and paste it on the external USB drive.
#. Copy the ``.kolibri`` folder from the USB drive, and paste it inside the destination device hard drive. 

	.. note:: On Windows you need to copy the ``.kolibri`` folder into the ``C:/Users/<username>/`` folder, where the ``<username>`` is the account you were logged in as when you installed Kolibri on that destination device (it may be different from the account on the master server). On Linux you need to copy inside the home folder of the user who installed Kolibri, or is the owner of the Kolibri system service.

	.. warning:: You should see an alert message that there is already a  ``.kolibri`` folder on the destination device: choose the option to overwrite it.


Use the cabled LAN connection to copy content
*********************************************

#. Connect all the devices, master server and the others where you need to copy the content on, to the same local area network (LAN).
	
	Configure the network access on the master server, so the rest of the devices can:

	* See it among their Network locations in the Windows Explorer
	* Open it and freely browse its shared folders (``.kolibri`` folder should be shared)
  
#. Use the Windows or File Explorer on each destination device to copy the ``.kolibri`` folder from the master server hard drive, and paste it inside the destination device hard drive. 

	.. note:: On Windows you need to copy the ``.kolibri`` folder into the ``C:/Users/<username>/`` folder, where the ``<username>`` is the account you were logged in as when you installed Kolibri on that destination device (it may be different from the account on the master server). On Linux you need to copy inside the home folder of the user who installed Kolibri, or is the owner of the Kolibri system service.

	.. warning:: You should see an alert message that there is already a  ``.kolibri`` folder on the destination device: choose the option to overwrite it.

#. You should be able to access the master server from several other destination servers through the LAN, and copy the ``.kolibri`` folder at the same time. 


Restart Kolibri servers on destination devices
**********************************************

* On Windows double-click the desktop shortcut to start Kolibri after copying content. You will see the notification message *Kolibri is starting, please wait…*. When you see the next notification that *Kolibri is running…*, Kolibri will open in the browser with the URL ``http://127.0.0.1:8080``.
* On Linux open the Terminal and run ``kolibri start`` or ``sudo service kolibri start`` (if you installed Kolibri to run as the system service).

Since the deprovision command emptied the user database on the master server, you will need to perform  the :ref:`setup_initial` on each destination device to set their **Facility** name and the super admin account. The Facility name could be the name of the learning center or school in which the respective server will be deployed.
