.. _command_line:

Working with Kolibri from the Command Line
##########################################

* In Windows you need to open the command prompt, for example by using the :guilabel:`WIN` + :guilabel:`R` shortcut, and then typing ``cmd``.

      .. figure:: /img/cmd.exe.png
        :alt: 

* On macOS open Spotlight and type ``Terminal``. You may also need to prefix the commands with ``python -m``, for example ``python -m kolibri start``.

* If you are running Kolibri with the ``.pex`` file, make sure to substitute the ``kolibri`` in below commands **with the exact name of the file you downloaded** preceded by ``./``. For example, to start Kolibri from the downloaded file ``kolibri-v0.13.pex``, type ``./kolibri-v0.13.pex start``.

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

  kolibri manage importchannel network <Channel ID>
  kolibri manage importcontent network <Channel ID>


For example (``Channel ID`` without angle brackets ``<...>``): 

.. code-block:: bash

  kolibri manage importchannel network a9b25ac9814742c883ce1b0579448337
  kolibri manage importcontent network a9b25ac9814742c883ce1b0579448337

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

  kolibri manage exportchannel <Channel ID> /path/to/local/drive/KOLIBRI_DATA 
  kolibri manage exportcontent <Channel ID> /path/to/local/drive/KOLIBRI_DATA 

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

The full name for the new super admin user will be the same as the chosen ``username``, and can be edited in the **Facility > Users** page, or the user profile.


Import Users from a CSV File
****************************

.. note:: 
  This is currently an experimental feature, so please forward to the development team any details about the issues you may encounter while using it.

  Command works on Kolibri version 0.9 and above.

CSV File Structure
""""""""""""""""""

To import users into Kolibri with this command, you will need to provide the user data in a CSV (comma separated values) file format. You can export a CSV file from a tabular data in any spreadsheet program (Excel, Google Sheets, LibreOffice Calc, etc.).

  .. figure:: /img/csv.png
      :alt: User data in a spreadsheet table

      User data in a spreadsheet table.

* Header row is optional, but if you do not include it, Kolibri will assume that you are providing the data in the following order:

    ``<full_name>,<username>,<password>,<facility>,<class>``

* If you do include a header row, you can provide less data, or put them a different order:

    ``<full_name>,<username>,<password>``

    ``<username>,<full_name>``

* Only the ``username`` is required.

* When you do not provide passwords for the imported users, Kolibri will set the default password ``kolibri`` for those usernames.

* If you do not provide full names for the imported users, Kolibri will set them to be the same as the values for ``username``, and you can edit them in the **Facility > Users** page.

* The facility can be either the facility name or the facility ID. If you do not provide the facility, Kolibri will import users in the default facility on the device. You can also specify the facility by adding the ``--facility`` argument in the command line (see below).


.. code-block:: bash

  kolibri manage importusers your-csv-file.csv

  kolibri manage importusers your-csv-file.csv --facility <your-facility>


Export Users to a CSV File
**************************

To export users from Kolibri in a CSV file, run the below command. It does not export demographic data by default, but has an optional ``-d/--demographic-data`` flag to include them in the exported CSV file. 

.. code-block:: bash

  kolibri manage exportusers your-csv-file.csv

  kolibri manage exportusers your-csv-file.csv --demographic-data


.. figure:: /img/exportusers.png
  :alt: CSV file with the user data.

  CSV file with the exported users including the demographic data.


Change User's Password
**********************

Run the following command to change the password for a user. 

.. code-block:: bash

  kolibri manage changepassword <username>

You will be prompted twice to input the new password for the user.


Delete Users Permanently
************************

If you need to permanently delete a Kolibri user and all the data associated with their account, for example to ensure privacy rights according to GDPR, use the following command.

.. code-block:: bash

  kolibri manage deleteuser <username>


.. warning:: This will permanently erase all the user data.


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

    .. figure:: /img/env-vars.png
      :alt: 

#. Restart Kolibri.
