.. _manage_advanced:

Advanced Management
~~~~~~~~~~~~~~~~~~~

.. _command_line:

Working with Kolibri from the Command Line
------------------------------------------

* In Windows you need to open the command prompt, for example by using the :guilabel:`WIN` + :guilabel:`R` shortcut, and then typing ``cmd``.

      .. figure:: img/cmd.exe.png
        :alt: 

* On macOS open Spotlight and type ``Terminal``. You may also need to prefix the commands with ``python -m``, for example ``python -m kolibri start``.

* If you are running Kolibri with the ``.pex`` file, make sure to substitute the ``kolibri`` in below commands **with the exact name of the file you downloaded** preceded by ``./``. For example, to start Kolibri from the downloaded file ``kolibri-v0.12.pex``, type ``./kolibri-v0.12.pex start``.

.. warning:: In the commands below, angle brackets and the text between them ``<...>`` are used to denote placeholders for you to modify. Make sure to replace them with your own information.


If you see errors in the prompt/terminal output while running the commands below, ask for help at our `Community Forums <https://community.learningequality.org/>`_, or `file an issue on GitHub <https://github.com/learningequality/kolibri/issues/new>`_.


Start/Stop Kolibri
******************

In case you need to troubleshoot potential problems while running Kolibri, you may try to start it manually from the command line.

.. code-block:: bash

  kolibri start --debug --foreground


.. code-block:: bash

  kolibri stop


.. _import_command_line:


Import Content Channels from Internet
*************************************

To import content channels from Internet, run these two commands in sequence. The first downloads the channel database, and the second downloads the resources (videos, documents, etc.). 

.. code-block:: bash

  kolibri manage importchannel -- network <Channel ID>
  kolibri manage importcontent -- network <Channel ID>


For example (``Channel ID`` without angle brackets ``<...>``): 

.. code-block:: bash

  kolibri manage importchannel -- network a9b25ac9814742c883ce1b0579448337
  kolibri manage importcontent -- network a9b25ac9814742c883ce1b0579448337

.. warning:: When you import content channels from the command line, you still must use the **32 digit channel ID**, as the :ref:`command will not work with the token <id_token>`. Make sure to receive the correct channel ID from the person who curated the unlisted channel you need to import, or refer to `Kolibri Studio user guide <https://kolibri-studio.readthedocs.io/en/latest/share_channels.html#make-content-channels-available-for-import-into-kolibri>`_ how to find it in Studio user interface, if you have channel editor access.

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
  kolibri manage exportcontent -- <Channel ID> /path/to/local/drive/KOLIBRI_DATA 

The path should be to a folder named ``KOLIBRI_DATA`` at the root of the local drive, so it will get picked up later for importing via the Web UI.

.. _reorder_channels:

Reorder Content Channels
************************

You can set the specific order for content channels in the **Learn** page according to your preferences. Follow these steps.

* To view the current ordered list of channels, run the command: 
   
  .. code-block:: bash

    kolibri manage listchannels


  The output will be something like:

  .. code-block:: bash

    Pos       ID                                      Name
    ---       --                                      ----
    1         95a52b386f2c485cb97dd60901674a98        CK-12 Testing
    2         a9b25ac9814742c883ce1b0579448337        TESSA - Teacher Resources


* To set a position for a channel, run the command: 
   
  .. code-block:: bash

    kolibri manage setchannelposition <Channel ID> <Pos>


  Example with the above channels:

  .. code-block:: bash

    kolibri manage setchannelposition a9b25ac9814742c883ce1b0579 1

    Pos       ID                                      Name
    ---       --                                      ----
    1         a9b25ac9814742c883ce1b0579448337        TESSA - Teacher Resources
    2         95a52b386f2c485cb97dd60901674a98        CK-12 Testing


.. _create_superuser:

Create a New Super Admin
************************

In case you need to create another **super admin** user, either to address additional need of managing facility, or if you lost the password for the old one, run the following command.

.. code-block:: bash

  kolibri manage createsuperuser

You will be prompted to input the **Username** and **Password** and the new **super admin** user account will be created.


Import Users from a CSV File
****************************

.. note:: 
  This is currently an experimental feature, so please forward to the development team any details about the issues you may encounter while using it.

  Command works on Kolibri version 0.9 and above.

CSV File Structure
""""""""""""""""""

To import users into Kolibri with this command, you will need to provide the user data in a CSV (comma separated values) file format. You can export a CSV file from a tabular data in any spreadsheet program (Excel, Google Sheets, LibreOffice Calc, etc.).

  .. figure:: img/csv.png
      :alt: User data in a spreadsheet table

      User data in a spreadsheet table.

* Header row is optional, but if you do not include it, Kolibri will assume that you are providing the data in the following order:

    ``<full_name>,<username>,<password>,<facility>,<class>``

* If you do include a header row, you can provide less data, or put them a different order:

    ``<full_name>,<username>,<password>``

    ``<username>,<full_name>``

* Only the ``username`` is required.

* When you do not provide passwords for the imported users, Kolibri will set the default password ``kolibri`` for those usernames.

* The facility can be either the facility name or the facility ID. If you do not provide the facility, Kolibri will import users in the default facility on the device. You can also specify the facility by adding the ``--facility`` argument in the command line (see below).


.. code-block:: bash

  kolibri manage importusers your-csv-file.csv

  kolibri manage importusers your-csv-file.csv --facility <your-facility>


Change User's Password
**********************

Run the following command to change the password for a user. 

.. code-block:: bash

  kolibri manage changepassword <username>

You will be prompted twice to input the new password for the user.


Delete Users Permanantly
************************

If you need to permanently delete a Kolibri user and all the data associated with their account, for example to ensure privacy rights according to GDPR, use the following command.

.. code-block:: bash

  kolibri manage deleteuser <username>


.. warning:: This will permanently erase all the user data.


Change Language
***************

.. code-block:: bash

  kolibri language setdefault <langcode>

+--------------------------+-----------------+ 
| Language                 | <langcode>      |
+==========================+=================+ 
| English                  | ``en``          |
+--------------------------+-----------------+
| Spanish (Spain)          | ``es-es``       | 
+--------------------------+-----------------+ 
| Spanish (Latin America)  | ``es-419``      | 
+--------------------------+-----------------+ 
| French                   | ``fr``          | 
+--------------------------+-----------------+
| Swahili (Tanzania)       | ``sw-tz``       | 
+--------------------------+-----------------+
| Arabic                   | ``ar``          | 
+--------------------------+-----------------+
| Bulgarian                | ``bg``          | 
+--------------------------+-----------------+
| Farsi                    | ``fa``          | 
+--------------------------+-----------------+
| Hindi (India)            | ``hi-in``       | 
+--------------------------+-----------------+
| Urdu (Pakistan)          | ``ur-pk``       | 
+--------------------------+-----------------+
| Marathi                  | ``mr``          | 
+--------------------------+-----------------+
| Chinyanja                | ``nyn``         | 
+--------------------------+-----------------+
| Portuguese (Brasil)      | ``pt-br``       | 
+--------------------------+-----------------+
| Telugu                   | ``te``          | 
+--------------------------+-----------------+
| Vietnamese               | ``vi``          | 
+--------------------------+-----------------+
| Yoruba                   | ``yo``          | 
+--------------------------+-----------------+
| Fulfulde Mbororoore      | ``ff-cm``       | 
+--------------------------+-----------------+
| Bengali                  | ``bn-bd``       | 
+--------------------------+-----------------+
| Gujarati                 | ``gu-in``       | 
+--------------------------+-----------------+
| Burmese                  | ``my``          | 
+--------------------------+-----------------+



Backup and Restore Kolibri Database
***********************************

Kolibri automatically creates a backup of the database with every version upgrade. If for some reason you need to make a manual backup, use the following command.

.. code-block:: bash

  kolibri manage dbbackup

This command will create a time-stamped ``.dump`` file in the ``./kolibri/backups`` folder that you can use to restore the database with the following command.

.. code-block:: bash

  kolibri manage dbrestore --latest

To restore the DB from a specific ``.dump`` file, use the flag ``--select`` to see all that available sorted by date, and select the one you need.

.. code-block:: bash

  kolibri manage dbrestore --select

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



Customize Kolibri Settings with the OPTIONS.INI File
----------------------------------------------------

For certain configuration settings you need to use the ``options.ini`` file. Installing Kolibri does not generate this file by default, but you can easily add one yourself. Follow these steps.

#. Open the preferred text editor on your computer (eg. Notepad on Windows).
#. Write the required *sections* and *keys* (see details for available settings below) in the following format:
   
    .. code-block:: ini

      [section]
      key1 = a
      key2 = b

3. Save the resulting ``options.ini`` file in the ``.kolibri`` folder inside the :ref:`Home <home>` folder. 
   
.. note::
  ``options.ini`` file can contain several sections with one or more associated keys, depending on the requirements of your installation.   
   
.. _port:


Run Kolibri from a Different Port
*********************************

If you need Kolibri to start and run from a port different than the default ``8080``, add the section ``[Deployment]``, and the key ``HTTP_PORT`` with the value of your desired port, to the ``options.ini`` file.

  .. code-block:: ini
    
     [Deployment]
     HTTP_PORT = 1234 
     # Substitute 1234 with your desired port number


.. _profile_requests_ini:


Allow Profiling of Requests
***************************

If you need to :ref:`profile server requests <profile_requests>` to get a more detailed information about the Kolibri performance, add the following to the ``options.ini`` file.


  .. code-block:: ini
    
     [Server]
     PROFILE = 1




Test Kolibri Server Performance
-------------------------------

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

In order to collect more than a current snapshot of Kolibri server performance, you can use the profiling command. When executed, the command will collect a series of performance indicators every 10 seconds and save them in a CSV file. Type this in the Terminal or Command prompt.

  .. code-block:: bash
     
     kolibri manage profile

.. tip:: Command collects and saves the information 60 times by default. If you want to change this value, add the ``--num-samples`` flag with the desired number at the end.

  .. code-block:: bash
     
     kolibri manage profile --num-samples=100


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

If you have the ``[Server]`` section of the :ref:`OPTIONS.INI <profile_requests_ini>` file  configured with ``PROFILE = 1``, the above command will additionally perform a profiling of every request made by Kolibri server, and save the results in a second log file as ``KOLIBRI_HOME/performance/date_time_requests_performance.csv``

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
  Profiling server requests can consume a lot of computer resources, and potentially slow it down. For this reason you need to explicitly allow it in the ``options.ini`` file. Without the ``PROFILE = 1`` key, command will not profile server requests (but just the current server state), and it will not create the second CSV file. 
