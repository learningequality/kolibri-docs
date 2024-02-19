.. _manage_data_ref:

Data
####

You can download Kolibri *Detail* and *Summary* logs usage data and export in the CSV format from the |save| **Data** tab in your |facility| **Facility** dashboard.

.. note::
  If you have more than one facility on the device, you must first select a facility. Click on the name of the facility from the list to access its data.

  .. figure:: /img/select-facility.png
    :alt: After clicking the Facility option in the sidebar, select which one you want to work on.

    Select a facility to access its data.

Remember that to manage Kolibri data you must sign in as **admin** or **super admin**.

.. figure:: /img/export-usage-data.png
  :alt: Open Facility page, navigate to Data tab, and use the Download buttons to save the logs on your local drive.  

To download session or summary logs, follow these steps.

#. Click the :guilabel:`Generate log` button for the file you require.
#. Select the desired data range.
#. Wait for the logs to be ready and click the :guilabel:`DOWNLOAD` button.
#. Save the generated CSV file on your local drive.

.. tip::
  If the log generation is taking a long time, we recommend :ref:`using the command line interface <export_data_logs>`.

.. _csv_import:


Import and export users from a CSV file
***************************************

To import and export many users and classes at once you can use an externally generated CSV (comma separated values) file. 

  .. figure:: /img/csv-import-export.png
    :alt: 

    Import and export users with CSV.

.. warning:: Importing from CSV will make many changes to your users and classes, and these changes cannot be easily reverted. Read carefully the requirements below, and make sure to verify that the data in your CSV file is accurate and adheres to the format reference. 

For the import to be successful, you must have a CSV file with properly formatted data with some required values. We recommend the following procedure:

#. Click the :guilabel:`Generate user CSV file` link.
#. Wait for the file to be ready and click the :guilabel:`DOWNLOAD` button to save the CSV file which contains all users and classes you already have in the facility.
#. Open the CSV file with an external spreadsheet program and make the required changes.
#. Export the edited records as *a new CSV file* from the spreadsheet program.
#. Click the :guilabel:`IMPORT` button and select that CSV file exported from the spreadsheet  to import and update users and classes.

.. tip:: You can also use this :download:`CSV file template </data/users_example.csv>` to get familiar with the required format. 

.. _csv_format:



CSV file format reference
^^^^^^^^^^^^^^^^^^^^^^^^^

The first row must be a header row, and contain the columns:

* **Database ID** (``UUID``) - Optional

  An ID used by Kolibri to uniquely identify a user. Leave it blank to create a new user. 

* **Username** (``USERNAME``) - Required

	Maximum 125 characters. Can contain letters, numbers and underscores.

* **Password** (``PASSWORD``) - Required
  
  Maximum 125 characters. To leave unchanged, use an asterisk ``*``.

* **Full name** (``FULL_NAME``) - Required
  
  Maximum 125 characters.

* **User type** (``USER_TYPE``) - Required
  
  Use one of theses values:

  * ``ADMIN``
  * ``FACILITY_COACH``
  * ``CLASS_COACH``
  * ``LEARNER``

* **Identifier** (``IDENTIFIER``) - Optional
	
	Any identifying string, such as a student ID or email address. Maximum 64 characters.

* **Birth year** (``BIRTH_YEAR``) - Optional

	A four-digit year, greater than 1900

* **Gender** (``GENDER``) - Optional

  Use one of theses values:

  * ``MALE``
  * ``FEMALE``
  * ``NOT_SPECIFIED``

* **Learner enrollment** (``ENROLLED_IN``) - Optional
  
  List of classes to enroll the user in as a learner.

  * Any type of user can be enrolled as a learner in a class.
  * Write the class names separated by commas.
  * If the class name in the field does not match exactly with any of the existing classes in the facility, the command will create a new class with that name.

* **Coach assignment** (``ASSIGNED_TO``) - Optional
  
  List of classes to which the user will be assigned as a coach.

  * Do not use for learner users.
  * Write the class names separated by commas.
  * If the class name in the field does not match exactly with any of the existing classes in the facility, the command will create a new class with that name.

Import users
^^^^^^^^^^^^

Importing users from a CSV file will make the following changes to your facility:

* Create new user accounts (for any ``USERNAME`` in the CSV that does not exist in the facility).
* Update existing user accounts (when the username in the database and the CSV match exactly).
* Set which classes each learner is enrolled in.
* Set which classes each coach is assigned to.
* Create new classes (for any value of ``ENROLLED_IN`` or ``ASSIGNED_TO`` in the CSV that does not match exactly the existing class name in the facility).
* Delete any users and classes in the facility if not referenced in the CSV.

To import users from a CSV file, follow these steps.

#. Click the :guilabel:`IMPORT` button to open the **Import users** page.
#. Click the :guilabel:`Browse` button to select the CSV file with the new user and classes data.
   
	  .. figure:: /img/import-users-browse-csv.png
	    :alt:

	    Browse for the CSV file.

#. Click the :guilabel:`CONTINUE` button to see the summary of changes that will be made.

	  .. figure:: /img/csv-import-review-summary.png
	    :alt:

	    Review the changes in users and classes.

#. Click the :guilabel:`IMPORT` button to finish importing.
#. When you see the notification that the import was successful, click the :guilabel:`CLOSE` button.
#. Open the **Users** or **Classes** tab to verify the changes.

.. _csv_export:


Export users
^^^^^^^^^^^^

#. Click the :guilabel:`Generate user CSV file` link.
#. Wait for the file to be ready and click the :guilabel:`DOWNLOAD` button.
#. Save the generated CSV file on your local drive.

.. _sync_kdp:



Sync facility data
******************

You can use the :term:`facility sync <Sync>` feature for multiple purposes.

* If your implementation is in a completely offline setting, you can bring another device like a laptop, :ref:`import the facility <import_facility>` of the offline device on it, and periodically perform the sync for backup purposes or further learning progress monitoring that needs to be performed in a different location with online access. 

* If your Kolibri facility is part of a larger organization that tracks data on the **Kolibri Data Portal** (**KDP**), you may have received the project token to sync the facility data with the organization in the cloud. 

Follow these steps to register your facility on **KDP** and perform the sync.

.. figure:: /img/sync-facility-data.png
  :alt:  

#. Open the options menu and select **Register**.
#. Enter the **project token** and click the :guilabel:`CONTINUE` button.

   .. figure:: /img/register-facility.png
 	   :alt:  

3. Click the :guilabel:`SYNC` button to synchronize the data from your facility with the project on **Kolibri Data Portal**.

.. figure:: /img/syncing-facility-data.png
  :alt:  

Be sure to follow the guidance of your **Kolibri Data Portal** project administrator on the frequency of sync-ups that you need to perform.

Schedule sync
^^^^^^^^^^^^^

To set up a regular syncing schedule, follow these steps.

#. Open the options menu and select **Manage sync schedule**.
#. Choose to sync with **KDP** or another device in the local network.
#. Set the preferred frequency and time to perform the sync.
#. Click the :guilabel:`SAVE` button to confirm.

   .. figure:: /img/edit-device-sync-schedule.png
     :alt:

You can configure your device to sync regularly with more than one device. To add a scheduled sync with another device, click the :guilabel:`ADD DEVICE` button and repeat the above steps.

If you need to edit the frequency or the time of previously configured sync, click the :guilabel:`EDIT` button and adjust the values. 

