.. _manage_content_ref:

Manage Content
~~~~~~~~~~~~~~

.. note::
  To manage Kolibri content channels you must have the appropriate permissions.

Kolibri **Content Channel** is a collection of educational resources (video, audio, document files or interactive apps) prepared and organized by the content curator for their use in Kolibri. You can import and export content channels in Kolibri from the **Channels** tab of the **Device** dashboard (|channels| icon).

  .. figure:: img/manage-content.png
    :alt: manage content page with list of available channels

    Kolibri content channels in the Device > Channels tab.


.. _id_token:

Each Kolibri content channel has its own **token/ID** in `Kolibri Studio <https://studio.learningequality.org/accounts/login/>`_. You can freely view and browse content to import from the **public** channels in Kolibri, but in order to import content from **private or unlisted** channels, you will need the **channel token or ID from the content curator who assembled it**.

.. note:: The term **Channel ID** was valid for Kolibri versions up to 0.6, while from the Kolibri version 0.7 onward, we started using exclusively the term **token** to uniquely designate each channel.

.. warning:: When you :ref:`use the Terminal or command prompt <import_command_line>` to import content channels in Kolibri from the command line, you still must use the **32 digit channel ID**, as the command will not work with the token. Make sure to receive the correct channel ID from the person who curated the channel you need to import, or refer to `Kolibri Studio user guide <http://kolibri-studio.readthedocs.io/en/latest/share_channels.html#make-content-channels-available-for-import-into-kolibri>`_ how to find it in Studio user interface, if you have channel editor access.



Import Content into Kolibri
---------------------------

.. warning:: **Important**: You **cannot** import your own files (videos, documents, etc.) as learning resources directly into Kolibri from your computer. Kolibri can **only** import content from:

  * already curated **content channels** on `Kolibri Studio <https://studio.learningequality.org/accounts/login/>`_, if the computer running Kolibri is connected to internet

  OR 

  * an external storage drive (USB or hard drive) where content channels have been previously exported to from another Kolibri installation, if the computer running Kolibri is not connected to internet

  **To import your own files for use in Kolibri**, you need to register at `Kolibri Studio <https://studio.learningequality.org/accounts/login/>`_ site (it's free), and build your own content channel that you can subsequently import into Kolibri. Read more about how to do this in our Kolibri `Studio user guide <http://kolibri-studio.readthedocs.io/en/latest/index.html>`_.


.. warning::
  Kolibri database and content may become temporarily unavailable while importing or updating large content channels. Therefore, as a precaution, we recommend you:

  * avoid other interactions with Kolibri (view learner pages or manage users, for example) while content import is in progress
  * perform these maintenance operations outside the periods when system is being used by learners


To import content into Kolibri, follow these steps.

#. Click **Import** button in the **Content** page.
#. Choose the source option: **Kolibri Studio** or **Attached drive or memory card**.

  .. figure:: img/import-choose-source.png
    :alt: select source for importing content

    Select a source to import Kolibri content channels.


Import Content from Kolibri Studio
**********************************

If the computer where Kolibri is running has an Internet connection with the sufficient bandwidth, follow these steps to import content channels.

.. _central_server:

#. Choose option *Kolibri Studio*, click **Continue** and you will be able to see all the available **public** content channels.

  .. figure:: img/kolibri-central-server.png
    :alt: Select which public channel on Kolibri Studio you want to import content from.

    Select which public channel on Kolibri Studio you want to import content from.

    
  Channels from which you have already imported some or all content onto your device will have the |on-device| icon. 


2. Click **Select** button for the desired channel, and wait for Kolibri to load the channel information and the topic tree.

   .. warning:: This could take some time for big channels. Please be patient, as Kolibri needs to retrieve a lot of information to display.


#. In the **Select content from...** page you will see all the details for the selected channel: description, version, total size and number of learning resources, with the information weather you have some of the resources from that channel already imported on the local device.

  	.. image:: img/select-content.png
	  :alt: Select topics and resources to import from channel.

#. Under **Choose content to import** click the topics links to browse through the channel contents. Use the *Select all* checkbox to import the content channel in full, or select only certain topics or resources. As you keep selecting, you will see the total number and size on disk under *Content selected:*, and the remaining space on your device.

#. Click **Import** button once you finish selecting all the desired content.

#. Wait for the content to be downloaded and click **Close** for the new channel to appear under the **Channel** heading.

	.. image:: img/import-CC.png
	  :alt: wait for import channel to finish

#. If you need to import content from a **private/unlisted** channel, click on **Try adding the token** link above the channel list.  
#. Enter the **channel token/ID** received from the channel curator on Kolibri Studio.

	.. image:: img/enter-token.png
	  :alt: enter content token to import from unlisted channel

#. Click **Confirm** to unlock channel, or **Cancel** to exit.
#. Proceed to select and import channel topics and resources as for the public channels.

   Unlisted or private channels in the list are indicated with the |unlisted-channel| icon.
#. To add more learning resources from a channel that you previously imported content from, click **Options**, select **Import more**, and repeat the selection procedure from step 3. 


.. _local_network:

Import Content from a Local Network or Internet
***********************************************

You can also import content from a different device running Kolibri in your same local network, or even from a Kolibri server hosted outside your LAN, provided you know its exact IP address. This feature is useful for when you have:

* a larger country- or region level Kolibri content server outside your LAN, but with resources specific to your implementation requirements
* various instances of Kolibri servers in your local network, in order to support a high number of client (learner) devices 
  
Follow these steps to import content channels.

#. Choose option *Local network or internet*, and click **Continue**.
#. Click *New address* link to add a new network address.
#. Input the full network address, and assign a name for this network. Don't forget to add the correct port if different from the default one ``8080``. You can use either the IP address or the domain name.
  
    .. image:: img/new-network-address.png
      :alt: add new address for the local network import

#. Click **Add** to save this address to your device settings. If you later decide to delete it, use the link *Forget*.
#. Click **Continue** and follow the same steps for selecting topics and resources as for the :ref:`import from Kolibri Studio <central_server>`.

.. warning:: This feature is introduced in Kolibri version 0.11, and all the server devices to be used for this type of content import **must have the Kolibri version 0.11 or later** running.

.. _local_drive:

Import Content from a Local Drive
*********************************

If the computer where Kolibri server is running does not have access to Internet or has insufficient bandwidth, you have the option to receive content channels stored on an external drive (USB stick or hard disk). Follow these steps to import content channels.

#. Connect the external USB drive to your computer.
#. Choose option for *Attached drive or memory card*, and click **Continue**.
#. Kolibri will automatically detect and display the drive(s) with available Kolibri content files.
#. Select the drive where the desired channel is stored, and click **Continue**.
#. Click **Select** button for the desired channel, and follow the same steps for selecting topics and resources as for the :ref:`import from Kolibri Studio <central_server>`.

  .. image:: img/import-local-drive2.png
    :alt: import channel from detected local drive


.. tip:: **Workaround for import from external drive on older devices.**

	If Kolibri is installed on an older or a low-resource device, you can try the following procedure for importing content channels for faster results.

	#. Stop Kolibri.
	#. Browse the local drive with the file explorer of your operating system.
	#. Copy the ``content`` folder located inside the ``KOLIBRI_DATA`` folder on the local drive.
	#. Paste the copied ``content`` folder inside the ``.kolibri`` folder on your hard disk. The location of the ``.kolibri`` folder will depend on your operating system (see the table below).
	#. Confirm the merge of the two folders.
	#. Restart Kolibri, and the new channels should now be available.


.. _home:

     +---------------------------+-----------------------------------------+
     | **Operating system**      | **Location**                            |
     +===========================+=========================================+
     | Windows                   | ``C:/Users/<your_username>/.kolibri/``  |
     +---------------------------+-----------------------------------------+
     | OSX                       | ``HD/Users/<your_username>/.kolibri/``  |
     +---------------------------+-----------------------------------------+
     | Linux                     | ``/home/<your_username>/.kolibri/``     |
     +---------------------------+-----------------------------------------+

     On Linux and OSX you will need to enable the **Show hidden folders** option in order to view the ``.kolibri`` folder.


Export from Kolibri to Local Drive
----------------------------------

If you want to make available the content you have imported on your Kolibri device, to another computer where Kolibri is installed, follow these steps to export your content channels.

.. note::
  You must have an external drive (SD card, USB stick or hard disk) attached to your device.

#. Click **Export** button in **Content** page.
#. Select the local drive (export destination) where you wish to export **Kolibri** content, and click **Continue**.
#. In the *Export to <name-of-your-drive>* page you will be able to see all the available content channels on your device.

  	.. image:: img/export-to.png
	  :alt: Select from which channel you want to export to local drive.

#. Click **Select** button for the desired channel, and wait for Kolibri to display the channel information and the topic tree.
#. In the **Select content from...** page you will see all the details of the selected channel: description, version, total size and number of learning resources.
#. Under **Choose content to export** you can browse the channel topics and individual resources. Use the *Select all* checkbox to import the content channel in full, or select only certain topics or resources. As you keep selecting, you will see the total number and size on disk under *Resources selected:*, and the remaining space on the destination drive.
#. Click **Export** button once you finish selecting all the desired content.
#. Wait for Kolibri to export the selected content and click **Close**.
#. Once the export is finished, safely disconnect the drive according to the recommended procedure for your operating system, and proceed to import channels on other devices.

.. note:: This procedure makes a copy of the ``content`` folder located inside the ``.kolibri`` folder on your hard disk, and places it in the ``KOLIBRI_DATA`` folder on the selected local drive. This structure is recognized by the **Import from local drive** command.

	.. image:: img/kolibri-data-osx.png
	  :alt: structure of the local drive folders with exported content channels

Delete Channel
--------------

To delete a content channel from your device, follow these steps.

#. Click **Options** for the channel you want to delete.
#. Select **Delete** option.
#. Click **Delete** to proceed, or **Cancel** to exit without deleting the channel.

  .. image:: img/delete-channel.png
    :alt: delete content channel from your device



Peer-to-Peer Content Synchronization
------------------------------------

``Stay tuned!``


.. Not yet. Peer to peer sync is a priority for Kolibri in the near future, but is not available yet.
