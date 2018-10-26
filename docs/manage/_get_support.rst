.. _support:

Troubleshooting
~~~~~~~~~~~~~~~

.. _network:

Troubleshoot Network Issues
---------------------------

#. Can you access Kolibri when you type ``http://127.0.0.1:8080`` in the address bar of the browser?
#. Can you access anything from the :ref:`external IP <access_LAN>` of the device running Kolibri **FROM** the device itself?
#. Can you ping the external IP address from another device on the network? For example, if Kolibri is on a device/computer with IP address ``192.168.0.104``, type this in the Terminal or Command prompt:

	.. code-block:: bash
	   
	   ping 192.168.0.104

	.. _ips:

	.. note:: **About IP addresses**

		* ``0.0.0.0`` = A special IP address on the **server** (your device running Kolibri and "serving" its content to others in the local network), which actually means "all available IP addresses". It's a kind of alias. But accessing ``0.0.0.0`` from another computer doesn't make sense and doesn't work. By default, Kolibri will serve on ``0.0.0.0``, which essentially means all IP addresses that are available on the device will render Kolibri accessible.
		* ``127.0.0.1`` = A device's local IP address, meaning "myself". Some people joke and say "There's no place like 127.0.0.1", meaning "there's no place like home" :) This can be used on the serving device itself to test that Kolibri is running, in case you need a failsafe way of checking that Kolibri is in fact running and responsive.
		* ``192.x.y.z`` = Addresses starting with ``192`` are local network IP addresses. The same thing can be said about ``10.x.y.z``. The address that you wanna use to enter on the clients/tablets in order to contact the server will in most cases start with ``192`` or ``10``.
		* Port number: Kolibri runs on port ``8080``. When you access something on an IP address, you need a port. Ports can be open or closed on the server, but they can also be regulated by firewall rules on the way. ``http://`` <- this is the protocol that the browser reads out from the "URL", which is just some text that describes Kolibri.
		* ``http://192.168.1.1:8080`` means: "Connect to IP address ``192.168.1.1`` on port ``8080`` with the HTTP protocol". The browser will the continue to try to reach this address, but may fail for instance if Kolibri isn't running, or if a step along the way blocks access.					


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

    sqlite3 ~/.kolibri/db.sqlite3 .dump | sqlite3 fixed.db 
    cp fixed.db ~/.kolibri/db.sqlite3

For further assistance, please report the issue on our `Community Forums <https://community.learningequality.org/>`_, stating the operating system and Kolibri version.


Videos are not playing
----------------------

Make sure to check the :ref:`system requirements <sys_reqs>` to see if you can support video playback. Please report any issues on our `Community Forums <https://community.learningequality.org/>`_, stating the operating system and browser you are using.


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

Open the ``.kolibri`` folder inside the :ref:`Home <home>` folder of the device where Kolibri is running and locate these two files:

* ``kolibri.log``
* ``debug.log``

.. warning:: On Linux and MacOS systems you will need to activate the *Show Hidden Files* option in your file browser, in order to view the ``.kolibri`` folder.


Kolibri server performance
--------------------------

Benchmark
*********

You can use the following command to collect information about the device where Kolibri server is running, and details about how much of its resources it is using. This command displays a snapshot of the server state at the time the command is executed, and its output will vary depending on the current server load. In case you suspect performance problems, type this in the Terminal or Command prompt.

	.. code-block:: bash
	   
	   kolibri manage benchmark

The command will have an output similar to this:

	.. figure:: img/benchmark.png
  	  :alt: Command line output of the 'kolibri manage benchmark' command

  	  Command line output of the 'kolibri manage benchmark' command

Take a screenshot of the Terminal or Command prompt, or copy and paste the output in the community forum post.

Profile
*******

In order to collect more than a current snapshot of Kolibri server performance, you can use the profiling command. When executed, the command will collect a series of performance indicators every 60 seconds and save them in a CSV file. Type this in the Terminal or Command prompt.

	.. code-block:: bash
	   
	   kolibri manage profile

.. tip:: Command collects and saves the information 60 times by default. If you want to change this value, add the ``--num_samples`` flag with the desired number at the end.

	.. code-block:: bash
	   
	   kolibri manage profile --num_samples=100


Each log line contains this information:

* Date and time of each command execution
* Number of Kolibri active sessions (including guest sessions)
* Number of Kolibri logged users
* Number of Kolibri user interactions during the last minute
* Total percentage of CPU use
* Total memory use
* Total available memory
* Number of processes executed in the server
* Percentage of CPU used by Kolibri
* Percentage of memory used by Kolibri

To help us troubleshoot potential problems on your Kolibri server, locate and send us the ``KOLIBRI_HOME/performance/date_time_performance.csv`` file.

