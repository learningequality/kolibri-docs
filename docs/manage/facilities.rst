.. _facilities:

Facilities
##########

You can import, sync and remove the facilities on your Kolibri device from the |facility| **Facilities** tab in your |device| **Device** dashboard. 

.. note::
  To manage facilities on a given device, you must have the **super admin** permissions.


.. figure:: ../img/facilities.png
	:alt: Open the Device page and navigate to Facilities tab.

	Manage facilities on a device.

.. _import_facility:


Import facility
***************

If you are part of a wider learning environment (for example when several learning facilities like schools or community centers are managed by one central organization), and your device is used to store the data from other facilities that are offline, you must first import those facilities. Once you have imported the facility on your device, you can periodically connect to their local network and sync the learner progress data.

To import a facility on your device, follow these steps.

#. Click the :guilabel:`Import facility` button. 

#. Any device that has Kolibri running in the local network should appear in the **Select network address** window.

	Select the device and click the :guilabel:`Continue` button.

  	.. figure:: /img/import-facility-select-device.png
	   :alt: 

	   Select the network address of the device from which you want to import a facility.

		.. note:: If you do not see the address of the device listed, but you know the IP address, you can add it manually. Click the *Add new address* link, and fill in the required information.

			.. figure:: /img/import-facility-add-device.png
				:alt: Add the network address of the device manually.

				Manually add the network address of the device.

#. **Select facility**. If there are several facilities on the source device, select the one you want to import. 

  	.. figure:: /img/select-facility-to-import.png
	   :alt: 

	   Select the facility you want to import.

#. **Enter admin credentials**. The credentials (username and password) you provide in this step must be either those for the **facility admin** of the facility you are importing, or for the **super admin** of the device you are importing from.

  	.. figure:: /img/import-facility-admin-creds.png
	   :alt: 

	   Enter admin credentials.

#. Wait for the importing facility task to complete. It may take some time, so please be patient. 
   
  	.. figure:: /img/import-facility-task.png
	   :alt: 

	   Facility is successfully imported on your device.

#. When the import process is completed click the *Back to facilities* link and you will see the new facility on the list.

  	.. figure:: /img/new-imported-facility.png
	   :alt: 

	   List of the facilities on your device.

.. _sync_facility:



Sync facility
*************

You can use the **Sync facility** feature for a variety of needs in both offline and online settings. 

..  raw:: html

	 <iframe width="670" height="380" src="https://www.youtube-nocookie.com/embed/AT7uO9vRGoo?rel=0&modestbranding=1&cc_load_policy=1&iv_load_policy=3" title="YouTube video player" frameborder="0" allow="accelerometer; gyroscope" allowfullscreen></iframe><br /><br />

Captions for the video are available in English, French, Swahili, Arabic, Hindi, Marathi and Brazilian Portuguese.


.. warning:: It is very important to remember that **syncing does not import channels and resources**. 

	When syncing facility data between devices in a local network, **you must make sure that the same channels and resources are present on all the devices**. If they do not have the same learning resources, coaches and learners will not be able to interact with lessons and quizzes correctly.


.. note:: **Examples of data syncing scenarios**:

	#.	**Roving admin scenario**

		* Kolibri is installed on the central server for the Kolibri implementation. 
		* Kolibri is installed on all learner devices along with the facility and resources from the school server, which are then distributed amongst learners for at home use.
		* The admin travels periodically to the communities along with the school server. Learner data syncs automatically from their devices when it comes into the network range of the school server. Simultaneously, the learner also receives any new assignments from the school server onto their device.


	#.	**Admin at Kolibri hub**

		* Kolibri is installed on a central server for the Kolibri implementation.
		* Kolibri is installed on all learner devices along with the facility and resources from the school server, which are then distributed amongst learners for at home use.
		* Learners periodically visit the Kolibri hub where the devices automatically start syncing when it comes into the network range of the school server


		Syncing will be automated as long as the devices and the server are using the same Kolibri facility and both are actively connected to the same network.

		Read our `Implementation Guide for Learner Data Syncing in Kolibri v0.15 <http://le.fyi/015-data-syncing-guide>`__ for more details to consider around the facility syncing strategies.

To sync  classes, groups, learner progress, and all  facility data with a device from which you previously imported it from, follow these steps.

#. Click the :guilabel:`SYNC` button for the desired facility.
#. Any device that has Kolibri running in the local network should appear in the **Select network address** window. Select the network address of the device you want to sync with. 
#. Syncing process will start immediately and you will see the task progress bar in the **Facilities** page. When the sync process is completed you can open the task manager and review the size of the sent and received data.
   
.. warning:: **Firewals** may impede your ability to see other devices in your local network, or add them as source. If you are unable to see other devices, make sure to:

	* disable the firewalls on all the devices that you need to sync
	* restart Kolibri for broadcast to take effect		


Sync with Kolibri Data Portal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If your Kolibri facility is part of a larger organization that tracks data on the **Kolibri Data Portal**, you can register and sync from **Facilities** page, same as from **Facility > Data** page.

#. Click the :guilabel:`OPTIONS` button and select the **Register** option, to :ref:`register your facility with the Kolibri Data Portal <sync_kdp>` (you must provide the project token). 
#. Click the :guilabel:`SYNC ALL` button to sync all registered facilities to the Kolibri Data Portal.

.. warning:: **Kolibri Data Portal** (KDP) is a new feature that is not yet broadly released. We are currently providing access to KDP to organizations on a contractual basis, and ultimately planning to offer this as a paid service by Learning Equality. 
  

Remove facility
***************

To remove a facility from the device, follow these steps.

#. Click the :guilabel:`OPTIONS` button on the right edge of the desired facility.
#. Select the **Remove** option.
#. Click the :guilabel:`REMOVE` button in the confirmation window to proceed, or :guilabel:`CANCEL` to exit.
   
  	.. figure:: /img/remove-facility.png
	   :alt: 

.. warning:: When you remove a facility you will loose all its data. However,  if you have previously synced it to another device or to the Kolibri Data Portal, you should be able to recover the removed facility data.
