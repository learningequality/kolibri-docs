.. _command_line:

Advanced Manage Options
~~~~~~~~~~~~~~~~~~~~~~~


Working with Kolibri from the Command Line
------------------------------------------

.. warning::
  * In Windows you need to open ``cmd.exe`` Command prompt in the folder where Kolibri executable is located: ``c:/Python34/Scripts``.

  * On macOS you may need to prefix the commands with ``python``, for example ``python kolibri start``.

  * If you are running Kolibri with the ``PEX`` file, make sure to substitute the ``kolibri`` in below commands **with the exact name of the file you downloaded** preceded by ``./``. For example, to start Kolibri from the downloaded file ``kolibri-v0.11.pex``, type ``./kolibri-v0.11.pex start``.

  * Make sure not to include the angle brackets “< >” in the commands below.*



If you see errors in the prompt/terminal output while running the commands below, ask for help at our `Community Forums <https://community.learningequality.org/>`_, or `file an issue on GitHub <https://github.com/learningequality/kolibri/issues/new>`_.


Start/Stop Kolibri
******************

In case you need to troubleshoot potential problems while running Kolibri, you may try to start it manually from the command line.

.. code-block:: bash

  kolibri start --debug --foreground


.. code-block:: bash

  kolibri stop


.. 

  Run Kolibri from a Different Port

..  If you need to change the default port ``8080`` from which Kolibri is serving content, add the following flag to the previous command.

.. 
  .. code-block:: bash

    kolibri start --port <new-port-number>


.. _import_command_line:


Import Content Channels from Internet
*************************************

To import content channels from Internet, run these two commands in sequence. The first downloads the channel database, and the second downloads the resources (videos, documents, etc.). 

.. code-block:: bash

  kolibri manage importchannel -- network <Channel ID>
  kolibri manage importcontent -- network <Channel ID>


.. warning:: When you import content channels from the command line, you still must use the **32 digit channel ID**, as the :ref:`command will not work with the token <id_token>`. Make sure to receive the correct channel ID from the person who curated the unlisted channel you need to import, or refer to `Kolibri Studio user guide <http://kolibri-studio.readthedocs.io/en/latest/share_channels.html#make-content-channels-available-for-import-into-kolibri>`_ how to find it in Studio user interface, if you have channel editor access.

..
  Commented out because the API is weird and should be fixed
  
  Import Content Channels from a Local Drive
  ------------------------------------------
  
  To import content channels from the local drive, run these two commands in sequence. Local drive should have a folder ``KOLIBRI_DATA`` at the root, with Kolibri ``content`` inside.
  
  .. code-block:: bash
  
    kolibri manage importchannel -- local <Channel ID> /path/to/local/drive
    kolibri manage importcontent -- local <Channel ID> /path/to/local/drive


Export Content Channels
***********************

To export Kolibri content channels on a local drive in order to share it with another device, run these two commands in sequence. The first exports the channel database, and the second exports the resources (videos, documents, etc.). 

.. code-block:: bash

  kolibri manage exportchannel -- <Channel ID> /path/to/local/drive/KOLIBRI_DATA 
  kolibri manage exportcontent -- <Channel ID> /mount/mydrive/KOLIBRI_DATA 

The path should be to a folder named ``KOLIBRI_DATA`` at the root of the local drive, so it will get picked up later for importing via the Web UI.


.. _create_superuser:

Create a New Super Admin
************************

In case you need to create another **super admin** user, either to address additional need of managing facility, or if you lost the password for the old one, run the following command.

.. code-block:: bash

  kolibri manage createsuperuser

You will be prompted to input the **Username** and **Password** and the new **super admin** user account will be created.


Change Language
***************

.. code-block:: bash

  kolibri language setdefault <langcode>

+-----------------------+-----------------+ 
| Language              | <langcode>      |
+=======================+=================+ 
| English               | ``en``          |
+-----------------------+-----------------+
| Spanish (Spain)       | ``es-es``       | 
+-----------------------+-----------------+ 
| Spanish (Mexico)      | ``es-mx``       | 
+-----------------------+-----------------+ 
| French                | ``fr``          | 
+-----------------------+-----------------+
| Swahili (Tanzania)    | ``sw-tz``       | 
+-----------------------+-----------------+
| Arabic                | ``ar``          | 
+-----------------------+-----------------+
| Bulgarian             | ``bg``          | 
+-----------------------+-----------------+
| Farsi                 | ``fa``          | 
+-----------------------+-----------------+
| Hindi (India)         | ``hi-in``       | 
+-----------------------+-----------------+
| Urdu (Pakistan)       | ``ur-pk``       | 
+-----------------------+-----------------+
| Marathi               | ``mr``          | 
+-----------------------+-----------------+
| Chinyanja             | ``nyn``         | 
+-----------------------+-----------------+
| Portuguese (Brasil)   | ``pt-br``       | 
+-----------------------+-----------------+
| Telugu                | ``te``          | 
+-----------------------+-----------------+
| Vietnamese            | ``vi``          | 
+-----------------------+-----------------+
| Yoruba                | ``yo``          | 
+-----------------------+-----------------+



Backup and Restore Kolibri Database
***********************************

Kolibri automatically creates a backup of the database with every version upgrade. If for some reason you need to make a manual backup, use the following command.

.. code-block:: bash

  kolibri manage dbbackup

This command will create a time-stamped ``.dump`` file in the ``./kolibri/backups`` folder that you can use to restore the database with the following command.

.. code-block:: bash

  kolibri manage dbrestore --latest

If you need to restore a backup version prior to the latest one, you must specify the full path to a specific ``*.dump`` file.

.. code-block:: bash

  kolibri manage dbrestore ~/.kolibri/backups/db-xxxx.dump

.. warning::
  This command is not intended for replication across different devices, but **only** for restoring on a single device from a local backup of the database.


Change the Location of Kolibri Content Files
********************************************

Kolibri content channels may occupy a considerable amount of hard disk space over time. If you have concerns about running out of storage on your device, you can move the Kolibri **content files** to another drive.

.. tip::
  If you have both SSD disk and HDD disk available on your device, it is recommended to install Kolibri on the SSD drive to allow faster access to the database, and move just the content file to the HDD drive.

To move the Kolibri content folders to another location, follow these steps.

1. Stop Kolibri.

  .. code-block:: bash

    kolibri stop


2. Create a new folder that will contain all the content files and resources on the destination drive.

  .. code-block:: bash

    kolibri manage content movedirectory <destination>


  For example, if you created a new folder ``KolibriContent`` on an external drive, run this command.

  .. code-block:: bash

    kolibri manage content movedirectory /mnt/my_external_drive/KolibriContent


  If you are on Windows, and the new folder ``KolibriContent`` is on the drive ``F:``, run this command.

  .. code-block:: bash

    kolibri manage content movedirectory F:\KolibriContent


3. Restart Kolibri.

This command will move the 2 subfolders ``databases`` and ``storage``, from their default location inside the ``.kolibri/content`` folder in your device's home directory, to a new location you specified in the command.


Change the Location of ALL Kolibri Files
****************************************

If you want to change the directory where all of Kolibri's runtime files are located, together with the imported content channels, you need to change the environment variable called ``KOLIBRI_HOME`` to the path of your choice.

If the variable is left unset, by default, Kolibri's runtime files and content will be placed in your user’s home folder, under the ``.kolibri`` subfolder. 

.. note::
  Adjusting this environment variable behaves differently than the ``movedirectory`` command above:

  * Adjusting the environment variable will not automatically migrate over data. You need to copy the ``.kolibri`` folder manually to the new location.
  * If you do copy the ``.kolibri`` folder, the content will not be affected **if it had been previously set** using the ``movedirectory`` command.


There are many ways to set an environment variable either temporarily or permanently. To start Kolibri on **OSX or Linux** with a different home, follow these steps.

#. Stop the server.
#. Move the ``.kolibri`` folder to the new location.
#. Run the following in Terminal:

.. code-block:: bash

  KOLIBRI_HOME=/path/to/new/home kolibri start

When you start the server again, all your files should be seamlessly detected at that location.

To change the environment variable ``KOLIBRI_HOME`` on **Windows**, follow these steps.

#. Stop the server.
#. Move the ``.kolibri`` folder to the new location.
#. Run the following in Command Prompt:

  .. code-block:: bash

    setx KOLIBRI_HOME "/path/to/new/home"

Restart the server, and your files should be seamlessly detected at the new location.


Alternatively, you can follow these steps in the GUI.

#. Go to **Computer > Advanced System Settings** and press the :guilabel:`Environment Variables` button.
#. Under **User Variables for...** press the :guilabel:`New...` button.
#. Input ``KOLIBRI_HOME`` in the **Variable name** field, and your new path in the **Variable value** field, and press :guilabel:`OK` on both open windows.

    .. figure:: img/env-vars.png
      :alt: 

#. Restart Kolibri.



Test Kolibri Server Performance
*******************************

Benchmark
^^^^^^^^^

You can use the following command to collect information about the device where Kolibri server is running, and details about how much of its resources it is using. This command displays a snapshot of the server state at the time the command is executed, and its output will vary depending on the current server load. In case you suspect performance problems, type this in the Terminal or Command prompt.

  .. code-block:: bash
     
     kolibri manage benchmark

The command will have an output similar to this:

  .. figure:: img/benchmark.png
      :alt: Command line output of the 'kolibri manage benchmark' command

      Command line output of the 'kolibri manage benchmark' command

Take a screenshot of the Terminal or Command prompt, or copy and paste the output in the community forum post.

Profile
^^^^^^^

In order to collect more than a current snapshot of Kolibri server performance, you can use the profiling command. When executed, the command will collect a series of performance indicators every 10 seconds and save them in a CSV file. Type this in the Terminal or Command prompt.

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


.. _profile_requests:


Profile Server Requests
"""""""""""""""""""""""

If you have the ``[Server]`` section of the :ref:`OPTION.INI <profile_requests_ini>` file  configured with ``PROFILE = 1``, the above command will additionally perform a profile of every request made by Kolibri server, and save the results in a second log file as ``KOLIBRI_HOME/performance/date_time_requests_performance.csv``

Each log line contains this information:

* Timestamp
* Request path
* Time spent processing the request
* Memory (in KB) used by the Kolibri process when the request came in
* Memory (in KB) used by the Kolibri process when the response was sent
* CPU percentage used by the Kolibri process when the request came in
* CPU percentage used by the Kolibri process when the request was sent
* Flag indicating if the request is the slowest one since the analysis started

.. warning::
  Profiling server requests can consume a lot of computer resources, and potentially slow it down. For this reason you need to explicitly allow it in the ``option.ini`` file. Without the ``PROFILE = 1`` key, server requests will not be profiled, and the second CSV file will not be created. 

  

Customize Kolibri Settings with the OPTION.INI File
---------------------------------------------------

For some advanced configuration settings you need to use the ``option.ini`` file. Installing Kolibri does not generate this file by default, but you can easily add one yourself. Follow these steps.

#. Open the preferred text editor on your computer (eg. Notepad on Windows).
#. Write the required *sections* and *keys* (see details for available settings below) in the following format:
   
    .. code-block:: bash

      [section]
      key1 = a
      key2 = b

3. Save the resulting ``option.ini`` file in the ``.kolibri`` folder inside the :ref:`Home <home>` folder. 
   
.. note::
  ``option.ini`` file can contain several sections with one or more associated keys, depending on the requirements of your installation.   
   

Run Kolibri from a Different Port
*********************************

If you need Kolibri to start and run from a port different than the default ``8080``, add the section ``[Deployment]``, and the key ``HTTP_PORT`` with the value of your desired port, to the ``option.ini`` file.

  .. code-block:: bash
    
     [Deployment]
     HTTP_PORT = 1234 
     # Substitute 1234 with your desired port number


.. _profile_requests_ini:


Allow Profiling of Requests
***************************

If you need to :ref:`profile server requests <profile_requests>` to get a more detailed information about the Kolibri performance, add the following to the ``option.ini`` file.


  .. code-block:: bash
    
     [Server]
     PROFILE = 1


