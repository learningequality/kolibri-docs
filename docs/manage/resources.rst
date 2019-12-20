.. _manage_resources_ref:

Channels and Resources
######################

.. note::
  To manage Kolibri channels and resources you must have the appropriate permissions.

Kolibri **Channel** is a collection of educational resources (video, audio, document files or interactive apps) prepared and organized by the resources curator for their use in Kolibri. You can import and export channels in Kolibri from the **Channels** tab of the **Device** dashboard (|channels| icon).

  .. figure:: /img/manage-resources.png
    :alt: Open the Device page and Channels tab to see the list of available channels on your device

    Kolibri resources channels in the Device > Channels tab.


.. _id_token:

Each Kolibri channel has its own **token** in `Kolibri Studio <https://studio.learningequality.org/accounts/login/>`__. You can freely view and browse resources to import from the **public** channels in Kolibri, but in order to :ref:`import resources from private or unlisted channels <import_with_token>`, you will need the **channel token from the resources curator who assembled it**.

.. note:: The term **Channel ID** was valid for Kolibri versions up to 0.6, while from the Kolibri version 0.7 onward, we started using exclusively the term **token** to uniquely designate each channel.

.. warning:: When you :ref:`use the Terminal or command prompt <import_command_line>` to import channels in Kolibri from the command line, you still must use the **32 digit channel ID**, as the command will not work with the token. Make sure to receive the correct channel ID from the person who curated the channel you need to import, or refer to `Kolibri Studio user guide <https://kolibri-studio.readthedocs.io/en/latest/share_channels.html>`__ how to find it in Studio user interface, if you have channel editor access.



Import Channels and Resources into Kolibri
------------------------------------------

.. warning:: **Important**: You **cannot** import your own files (videos, documents, etc.) as learning resources directly into Kolibri from your computer. Kolibri can **only** import resources from:

  * already curated **channels** on `Kolibri Studio <https://studio.learningequality.org/accounts/login/>`__, if the computer running Kolibri is connected to internet

  OR 

  * an external storage drive (USB or hard drive) where channels have been previously exported to from another Kolibri installation, if the computer running Kolibri is not connected to internet

  **To import your own files for use in Kolibri**, you need to register at `Kolibri Studio <https://studio.learningequality.org/accounts/login/>`__ site (it's free), and build your own channel that you can subsequently import into Kolibri. Read more about how to do this in our `Kolibri Studio user guide <https://kolibri-studio.readthedocs.io/en/latest/index.html>`__.


.. warning
  Kolibri database and resources may become temporarily unavailable while importing or updating large resources channels. Therefore, as a precaution, we recommend you:

  * avoid other interactions with Kolibri (view learner pages or manage users, for example) while resources import is in progress
  * perform these maintenance operations outside the periods when system is being used by learners


To import resources into Kolibri, follow these steps.

#. Click :guilabel:`IMPORT` in the **Channels** tab on the **Device** page.
#. Choose the source option: **Kolibri Studio**, **Local network or internet**, or **Attached drive or memory card**.

  .. figure:: /img/import-choose-source.png
    :alt: Use the radio buttons to select source for importing resources

    Select a source to import Kolibri channels.


.. _import_studio:


Import from Kolibri Studio
**************************

If the computer where Kolibri is running has an Internet connection with the sufficient bandwidth, follow these steps to import resources channels.


#. Choose option *Kolibri Studio*, click :guilabel:`CONTINUE` and you will be able to see all the available **public** resources channels.

    .. figure:: /img/kolibri-studio.png
      :alt: Available channels on Kolibri Studio page where you can select which public channel you want to import resources from.

      Select which public channel on Kolibri Studio you want to import resources from.

    
    Channels from which you have already imported some or all resources onto your device will have the |on-device| icon. 


2. Click :guilabel:`SELECT RESOURCES` for the desired channel, and wait for Kolibri to load the channel information and the topic tree.

   .. warning:: This could take some time for big channels. Please be patient, as Kolibri needs to retrieve a lot of information to display.


#. In the following page you will see all the details for the selected channel: description, version, total size and number of learning resources, with the information weather you have some of the resources from that channel already imported on the local device.

    .. figure:: /img/select-content.png
	    :alt: 

#. Click the topics links to browse through the channel resources. Use the *Select all* checkbox to import all the resources in the channel, or select only certain topics or resources. As you keep selecting, you will see the total number and size of *resources selected* at the bottom of the page.

#. Click the :guilabel:`IMPORT` button once you finish selecting all the desired resources.

#. You will see the import progress in the **Task manager** page. Once the import concludes, the newly imported channel and resources display on the **Channels** page.

    .. figure:: /img/import-CC.png
  	  :alt: resources import progress bar will display the percentage of the download


Import Entire Channels
""""""""""""""""""""""

To import entire channels instead of a selected resources, follow these steps.

#. Click the **Select entire channels instead** link above the list of public channels in Kolibri.
#. Use the checkboxes to select the channels you want to import in full. As you keep selecting, you will see the total number and size of *channels selected* at the bottom of the page.
#. Click the :guilabel:`IMPORT` button once you finish selecting all the desired channels.

.. warning:: You can also use the *Select all on page* option, but beware that it will require several hundreds of gigabytes on your hard drive, and likely prolonged import times.

.. _import_with_token:

Import with Token
"""""""""""""""""

#. If you need to import resources from a **private/unlisted** channel, click on **Import with token** button above the channel list.  
#. Enter the **channel token** received from the channel curator on Kolibri Studio.

    .. figure:: /img/enter-token.png
  	  :alt: Use the text input field to enter channel token in order to import from an unlisted channel

#. Click :guilabel:`CONTINUE` to unlock the channel, or :guilabel:`CANCEL` to exit.
#. Proceed to select and import channel topics and resources as for the public channels.

    Unlisted or private channels in the list are indicated with the |unlisted-channel| icon.

Import More Resources
"""""""""""""""""""""

To add more learning resources from a channel that you previously imported resources from, follow these steps.

#. Click the :guilabel:`MANAGE` button for the desired channel.
#. Click :guilabel:`IMPORT MORE`.
#. Repeat the selection procedure from above. 


.. _local_network:

Import from a Local Network or Internet
***************************************

You can also import resources from a different device running Kolibri in your same local network, or even from a Kolibri server hosted outside your LAN, provided you know its exact IP address. This feature is useful for when you have:

* a larger country- or region-level Kolibri server outside your LAN, but with resources specific to your implementation requirements
* various instances of Kolibri servers in your local network, in order to support a high number of client (learner) devices 
  
.. note:: Kolibri will try to automatically detect other instances (*peers*) running in the same LAN, and you will see a spinning loader while it is searching. When the detection is successful, you will be able to select these Kolibri instances and import resources from them.

    .. figure:: /img/peer.png
      :alt: 


Follow these steps to import from a local network.

#. Choose option *Local network or internet*, and click :guilabel:`CONTINUE`.
#. Click *Add new address* link to add a new network address.
#. Input the full network address, and assign a name for this network. Don't forget to add the correct port if different from the default one ``8080``. You can use either the IP address or the domain name.
  
  .. figure:: /img/new-network-address.png
    :alt: Use the text input fields to add the new address and the name for the local network import


#. Click :guilabel:`ADD` to save this address to your device settings. If you later decide to delete it, use the link *Forget*.
#. Click :guilabel:`CONTINUE` and follow the same steps for selecting topics and resources as for the :ref:`import from Kolibri Studio <import_studio>`.

.. warning:: 
  
  * Beware that active firewalls on your devices could cause:

    - inability to be discovered by peers
    - inability to discover other peers
    - ability to be discovered, but not be available for import


  * This feature was introduced in Kolibri version 0.11, and all the server devices to be used for this type of resources import **must have the Kolibri version 0.11 or later** running.

.. _local_drive:


Import from a Local Drive
*************************

If the computer where Kolibri server is running does not have access to Internet or has insufficient bandwidth, you have the option to receive resources channels stored on an external drive (USB stick or hard disk). Follow these steps to import resources channels.

#. Connect the external USB drive to your computer.
#. Choose option for *Attached drive or memory card*, and click :guilabel:`CONTINUE`.
#. Kolibri will automatically detect and display the drive(s) with available Kolibri resources files.
#. Select the drive where the desired channel is stored, and click :guilabel:`CONTINUE`.
#. Click :guilabel:`SELECT` for the desired channel, and follow the same steps for selecting topics and resources as for the :ref:`import from Kolibri Studio <import_studio>`.

  .. figure:: /img/import-local-drive2.png
    :alt: Importing resources from a local drive presents the same interface options as importing from Kolibri Studio.

.. TO-DO (image)


Update Channels
---------------

Public channels on Kolibri Studio are periodically updated from their original sources. Private and unlisted channels that you have on your local Kolibri device may also have changed since you first imported them. You can update your local channels from Kolibri Studio from online sources, from another updated device in your local network or from an external drive where the latest version of the channels has been :ref:`previously exported <export>`.

.. warning:: It is recommended to schedule and perform channel updates only during periods of low activity on the server. Updating resources while server is receiving requests by client devices may cause errors or performance issues.

To update a channel to its latest version and import new resources into Kolibri, follow these steps.

#. Click the :guilabel:`MANAGE` button for the channel you want to update.
#. When a new channel version is available, you will see the notification. Click the :guilabel:`VIEW CHANGES` button.
   
    .. figure:: /img/view-changes.png
      :alt: 

#. On the following page you can see the summary of the changes: how many resources will be added, deleted or updated if you decide to proceed. 

    .. figure:: /img/update-channel.png
      :alt: 

      Notification for the new version of the resources channel.

    .. warning:: Use caution when updating channels that have been used to make **currently-active** :ref:`lessons <manage_lessons>` and :ref:`quizzes <manage_quizzes>`. The structure and location of some resources inside the channel may have changed in the updated version, which can cause lessons and quizzes to not load correctly. 

4. Click the :guilabel:`UPDATE CHANNEL` button.
5. You will see the update progress in the **Task manager** page. Once the update concludes, the newly imported and updated resources will be available to use in Kolibri.


.. warning:: 
  All import tasks can be cancelled before they are labeled as *Completed* in the **Task manager** page. However, beware that resources from canceled imports might not be fully available. If you plan to use the resources in lessons or quizzes, please check the state of their channel before you do, and use the :guilabel:`IMPORT MORE` button if necessary.


Edit Channel Order 
------------------

To change the order in which channels are presented to learners on the **Learn > Channels** page, follow these steps.


#. Click the :guilabel:`OPTIONS` button and select the **Edit channel order** option.
#. In the *Edit channel order* page you can either:

    * Grab the |drag| button to reorder channels with the mouse (drag and drop).
    * Use the |arrow-up| and |arrow-down| buttons to reorder by keyboard navigation.  

  You will see a confirmation notification at the bottom every time you change the order of the channels.

3. Close the *Edit channel order* to return to **Device > Channels**, and review their order on the **Learn > Channels** page.



.. _export:

Export from Kolibri to Local Drive
----------------------------------

If you have imported resources on one Kolibri device, and want to make it available on another computer where Kolibri is installed, you can export it either in full, or make a selection of the resources to be exported

.. note::
  You must have an external drive (SD card, USB stick or hard disk) attached to your device.


Export Complete Channels
************************

To export one or more full channels with all of its resources on a local drive, follow these steps.


#. Click the :guilabel:`OPTIONS` button and select the **Export channels** option.
#. Use the checkboxes to select single channels you want to export, or the *Select all on page* to export all of them in bulk. As you keep selecting, you will see the total number and size of *channels selected* at the bottom of the page.
#. Click the :guilabel:`EXPORT` button once you finish selecting, or :guilabel:`CANCEL` to exit.
#. Select the local drive (destination for the export) where you wish to export Kolibri resources, and click :guilabel:`CONTINUE`.
#. You will see the export progress in the **Task manager** page. Once the export is finished, safely disconnect the drive according to the recommended procedure for your operating system, and proceed to import channels on other devices.
   
.. warning::
  Beware that exporting complete channels might require a lot of available space on your local drive.
   

Export Selected Resources from a Channel
****************************************

To export only a selection of channel resources on a local drive, follow these steps.

#. Click the :guilabel:`MANAGE` button for the channel from which you want to export resources, and wait for Kolibri to display the channel information and the topic tree.
#. Follow the same steps for selecting topics and resources in the topic tree as for the import procedure. As you keep selecting, you will see the total number and size of *resources selected* at the bottom of the page.
#. Click the :guilabel:`EXPORT` button once you finish selecting, or :guilabel:`CANCEL` to exit.
#. Select the local drive (destination for the export) where you wish to export Kolibri resources, and click :guilabel:`CONTINUE`.
#. You will see the export progress in the **Task manager** page. Once the export is finished, safely disconnect the drive according to the recommended procedure for your operating system, and proceed to import channels on other devices.

.. note:: The above procedures copy the channel databases and resources from the ``content`` folder located inside the ``.kolibri`` folder on your device's hard disk, and place them in the ``KOLIBRI_DATA`` folder on the selected local drive. This structure is recognized by the **Import from local drive** command.

        .. figure:: /img/kolibri-data-osx.png
          :alt: structure of the local drive folders with exported resources channels


Delete Channels
---------------

Delete Complete Channels
************************

To delete one or more full channels with all of its resources from your device, follow these steps.


#. Click the :guilabel:`OPTIONS` button and select the **Delete channels** option.
#. Use the checkboxes to select single channels you want to delete, or the *Select all on page* to delete all of them in bulk. As you keep selecting, you will see the total number and size of *channels selected* at the bottom of the page.
#. Click the :guilabel:`DELETE` button once you finish selecting, or :guilabel:`CANCEL` to exit without deleting the channel.

#. If you are certain you want to proceed, click the :guilabel:`DELETE` button again in the **Delete channel** confirmation window.
#. You will see the delete progress in the **Task manager** page. Once the delete task is completed, the channel(s) will not be listed in the **Channels** tab on the **Device** page.


Delete Selected Resources from a Channel
****************************************

To delete only a selection of channel resources from your device, follow these steps.

#. Click the :guilabel:`MANAGE` button for the channel from which you want to delete resources, and wait for Kolibri to display the channel information and the topic tree.
#. Follow the same steps for selecting topics and resources in the topic tree as for the import procedure. As you keep selecting, you will see the total number and size of *resources selected* at the bottom of the page.
#. Click the :guilabel:`DELTE` button once you finish selecting, or :guilabel:`CANCEL` to exit without deleting the channel.

#. If you are certain you want to proceed, click the :guilabel:`DELETE` button again in the **Delete channel** confirmation window.
#. You will see the delete progress in the **Task manager** page. Once the delete task is completed, the selected resources will not be present in the topic tree of the channel.
