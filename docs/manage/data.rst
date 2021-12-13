.. _manage_data_ref:

Data
####

You can download Kolibri *Detail* and *Summary* logs usage data and export in the CSV format from the |data| **Data** tab in your |facility| **Facility** dashboard.

	.. figure:: /img/export-usage-data.png
	  :alt: Open Facility page, navigate to Data tab, and use the Download buttons to save the logs on your local drive. 

.. note::
  If you have more than one facility on the device, you must first select a facility. Click on the name of the facility from the list to access its data.

  .. figure:: /img/select-facility.png
    :alt: After clicking the Facility option in the sidebar, select which one you want to work on.

    Select a facility to access its data.

  Remember that to manage Kolibri data you must sign in as **admin** or **super admin**.

To download session or summary logs, follow these steps.

#. Click the *Generate log file* link for the file you require.
#. Click the :guilabel:`DOWNLOAD` button.
#. Save the generated CSV file on your local drive.
#. To download again after more interactions click the *Generate a new log file* link.

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

#. Use the **Export** :ref:`feature first and save the CSV file <csv_export>` which contains all users and classes you already have in the facility.
#. Open the CSV file with an external spreadsheet program and make changes.
#. Export *a new CSV file* from the spreadsheet program.
#. Use that CSV file to **Import** or update users and classes.

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
  
  List of classes to enroll the user in as a learner:

  * Any type of user can be enrolled as a learner in a class.
  * Write the class names separated by commas.
  * If the class name in the field does not match exactly with any of the existing classes in the facility, the command will create a new class with that name.

* **Coach assignment** (``ASSIGNED_TO``) - Optional
  
  List of classes to which the user will be assigned as a coach:

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
#. Click the :guilabel:`BROWSE` button to select the CSV file with the new user and classes data.
   
	  .. figure:: /img/import-users-browse-csv.png
	    :alt:

	    Browse for the CSV file.

#. Click the :guilabel:`CONTINUE` button to see the summary of changes that will be made.

	  .. figure:: /img/csv-import-review-summary.png
	    :alt:

	    Review the changes in users and classes.

#. Click the :guilabel:`IMPORT` button finish importing.
#. When you see the notification that the import was successful, click the :guilabel:`CLOSE` button.
#. Open the **Users** or **Classes** tab to verify the changes.

.. _csv_export:


Export users
^^^^^^^^^^^^

#. Click the :guilabel:`EXPORT` button and wait for the CSV file to generate.
#. Save the generated CSV file on your local drive.

.. _sync_kdp:



Sync facility data
******************

If your Kolibri facility is part of a larger organization that tracks data on the **Kolibri Data Portal**, you may have received the project token to sync the facility data with the organization in the cloud. Follow these steps to register your facility and sync.

.. figure:: /img/sync-facility-data.png
  :alt:  

#. Click the :guilabel:`REGISTER` button.
#. Enter the **project token** and click the :guilabel:`CONTINUE` button.

.. figure:: /img/register-facility.png
 	:alt:  

3. Click the :guilabel:`SYNC` button to synchronize the data from your facility with the project on **Kolibri Data Portal**.

.. figure:: /img/syncing-facility-data.png
  :alt:  


Be sure to follow the guidance of your **Kolibri Data Portal** project administrator on the frequency of sync-ups that you need to perform.
