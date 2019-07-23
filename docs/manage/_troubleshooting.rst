.. _troubleshooting:

Troubleshooting
~~~~~~~~~~~~~~~

.. _network:

Troubleshoot Network Issues
---------------------------

#. Can you access Kolibri when you type ``http://127.0.0.1:8080`` in the address bar of the browser?
#. Can you access anything from the :ref:`external IP <access_LAN>` of the device running Kolibri **FROM** the device itself? Read more information :ref:`about IP addresses <ips>`.
#. Can you ping the external IP address from another device on the network? For example, if Kolibri is on a device/computer with IP address ``192.168.0.104``, type this in the Terminal or Command prompt:

	.. code-block:: bash

	   ping 192.168.0.104

#. Kolibri may change address every time you reboot your network equipment. Read about :ref:`static IP addresses <ips_static>`


.. _firewalls:

Firewalls
*********

If you are having trouble connecting to Kolibri from other computers, your firewall might be blocking access.

Windows systems often come with firewalls bundled and enabled, and this may interfere with running Kolibri. That said, you probably want to keep your firewall enabled for security reasons, especially if the server is connected to the public internet.

You can try temporarily disable your firewall to see if it helps with connecting to Kolibri. If so, you'll want to turn the firewall back on and then create a exception rule for Kolibri to allow access.


Troubleshoot Database Issues
----------------------------

In case you receive the ``database disk image is malformed`` error in Terminal, try running these commands (note that **you must have the** ``sqlite3`` **command available on your system**).

.. code-block:: bash

	mkdir -p malformed
	cp -b db.sqlite3* malformed
	sqlite3 ~/.kolibri/db.sqlite3 .dump | sqlite3 fixed.db
	cp fixed.db ~/.kolibri/db.sqlite3
	rm -f db.sqlite3-wal db.sqlite3-shm


For further assistance, please report the issue on our `Community Forums <https://community.learningequality.org/>`_, stating the operating system and Kolibri version.


Videos are not playing
----------------------

Make sure to check the :ref:`system requirements <sys_reqs>` to see if you can support video playback. Please report any issues on our `Community Forums <https://community.learningequality.org/>`_, stating the operating system and browser you are using.


Antivirus
---------

Some overzealous antivirus programs on Windows platform may preventively impede Kolibri or some of its components (for example ``python.exe``) from running correctly. If that happens you need to add them to the antivirus exclusion list. Below steps refer to the program **Avast**, but should be similar in other antivirus applications.

1. Open **Avast**.
2. Click on **Protection** in the sidebar.
3. Click on **Virus Chest**.
4. Find the file `python.exe` in the list.
5. Right click on the file and select *Scan*.
6. If the scan is inconclusive the ``python.exe`` file is not infected with a virus.
7. Right click on the file and select *Restore and add to exclusions*.


Problems with import and export from USB drives
-----------------------------------------------

Kolibri needs read and write access to USB drives in order to import and export content. There are several possibilities why you may encounter issues during this procedure.

* **User account does not have access**:

  - you installed Kolibri in your own environment running as a non-desktop user (for instance UWSGI)
  - you have upgraded Kolibri on Debian from a version prior to v0.10. Follow these instructions to :ref:`change the ownership of Kolibri system service <changing-system-user>` from one user account to another
  - to grant access to USB drives to other accounts, refer to the documentation of your operating system

* **Write access denied**: Some USB drives will experience problems when they are unplugged from the computer in an "unclean" way. If you are denied access to write, look for options to "fix" or "repair" the file system.

* **Data failures**: Copying the data can take a long time. If you do not see the final success confirmation message after the copy apparently finishes, do not assume that the data has been imported or exported correctly. Restart the process instead, otherwise you risk inconsistent and malfunctioning content data.

* **Hardware life expectancy**: SD and flash storage drives can "expire". Reading and writing large quantities of content data, especially on older or models with smaller capacity, may produce data errors over time.


Locate Kolibri log files
------------------------

When you report a problem with Kolibri, we may ask you to send us Kolibri **log** files to help us find out why is it not working or crashing.

Open the ``.kolibri/`` folder inside the :ref:`Home <home>` folder of the Kolibri server and locate the ``logs/`` folder. You will be able to find these two files:

* ``kolibri.txt``
* ``debug.txt``

If the problem happened earlier than the dates in the above log, you can open the ``archive/`` folder inside ``logs/`` to find older log files:

* ``kolibri-YYYY-MM-DD.txt``

.. warning:: On Linux and MacOS systems you will need to activate the *Show Hidden Files* option in your file browser, in order to view the ``.kolibri`` folder.


.. _ips:

About IP addresses
------------------

* The ``127.0.0.1`` IP address, or ``localhost``, is a device's own IP address where it can access *itself*. You can use it in the browser on the device where Kolibri is running to make sure it is working correctly.
* Aside from its own `localhost <https://en.wikipedia.org/wiki/Localhost>`_ address, a device running Kolibri also has an external IP address like ``192.*.*.*`` or ``10.*.*.*``, under which other devices in the same local network can connect with. That is the IP address that you need to use in the :ref:`browsers on client devices <access_LAN>` (learner tablets or computers), to connect with Kolibri server.
* Kolibri by default runs on the port number ``8080``, but you can :ref:`change this setting <port>` to meet your particular needs.
* So when you type the full IP address like ``http://192.168.1.1:8080`` in the browser of a client device, you are telling it to: "Connect to IP address ``192.168.1.1`` on port ``8080`` with the HTTP protocol, and display its content".

.. _ips_static:

Static IP addresses
-------------------

In order for other clients on your network to find Kolibri on a consistent IP address, this address shouldn't change.

The default behavior of an operating system, no matter if it's Linux/Windows/Mac, will be to receive an IP address from a network authority, i.e. a *DHCP server*. DHCP is a service that's typically run on the local access point or router.

Therefore, you should be cautious that when such a router or access point restarts (for instance during a power cut), it may forget the IP address assigned to your Kolibri device, and thus the IP changes.

To fix this, you have two general options:

#. Find out how to log in and configure your access point or router, such that it assigns the same IP address consistently to your Kolibri device.

   .. tip:: Any network interface, both a WIFI and a cabled ethernet, has a *MAC* address that's consistent. You can use this *MAC* address by configuring your router or access point to assign the same IP address every time.

#. Configure your Kolibri device to use a static IP address: Instead of asking a DHCP server for an IP address, your device can choose one itself.

   .. warning:: If you choose an IP address that's already in use on the network, you can have an IP conflict on your network where traffic doesn't get routed correctly. You need to choose an IP address on the same *subnet* as your automatically assigned DHCP address, but also an address that won't be used by the DHCP server, i.e. outside of the *DHCP range*. For instance, a DHCP server could hand out IP address from `192.168.1.10` to 192.168.1.255` and the router would be located on `192.168.1.1`. Thus, `192.168.1.2` would be free to assign.


Still not working?
------------------

Read about :ref:`getting support from online community <support>`.
