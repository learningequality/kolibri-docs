.. _facilities:

Facilities
##########

You can import, sync and remove the facilities on your Kolibri device from the **Facilities** tab in your **Device** dashboard ( icon). 

.. TO-DO (icon)

.. note::
  To manage facilities on the device you must have the **super admin** permissions.


.. figure:: ../img/facilities.png
	:alt: Open the Device page and navigate to Facilities tab.

	Manage the facilities on the device.

Import a Facility on Device
***************************

If you are part of a wider learning environment, where your device is used to store the data from other facilities that are offline, you must import those facilities first. Once you have imported the facility on your device, you can periodically connect to their local network and sync the learner progress data.

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

				Add the network address of the device manually.

#. **Select facility**. If there several facilities on the source device, select the one you want to import. 

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

	   Facility is imported on your device.

#. When the import process is completed click the *Back to facilities* link and you will see the new facility on the list.

  	.. figure:: /img/new-imported-facility.png
	   :alt: 

	   List of the facilities on your device.

.. _sync_facility:



Sync Facility
*************

You can use the syncing feature for a variety of needs in both offline and online settings. To sync the classes, groups, learner progress and all the facility data with the device from where you imported it, follow these steps.

#. Click the :guilabel:`SYNC` button for the desired facility.
#. Any device that has Kolibri running in the local network should appear in the **Select network address** window. Select the network address of the device you want to sync with. 
#. Syncing process will start immediately and you will see the task progress bar in the **Facilities** page. When the import process is completed you can open the task manager and review the size of the sent and received data.

Sync with Kolibri Data Portal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If your Kolibri facility is part of a larger organization that tracks data on the **Kolibri Data Portal**, you can register and sync from **Facilities** page, same as from **Facility > Data** page.

#. Click the :guilabel:`OPTIONS` button and select the **Register** option, to :ref:`register your facility with the Kolibri Data Portal <sync_kdp>` (you must provide the project token). 
#. Click the :guilabel:`SYNC ALL` button to sync all registered facilities to the Kolibri Data Portal.
  

Remove Facility
***************

To remove a facility from the device, follow these steps.

#. Click the :guilabel:`OPTIONS` button on the right edge of the desired facility.
#. Select the **Remove** option.
#. Click the :guilabel:`REMOVE` button in the confirmation window to proceed, or :guilabel:`CANCEL` to exit.
   
  	.. figure:: /img/remove-facility.png
	   :alt: 

.. warning:: When you remove a facility you will loose all its data. However, if you previously synced it to another device or the Kolibri Data Portal, you should be able to load it again.