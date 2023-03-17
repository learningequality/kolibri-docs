.. _coach:

Coach your learners in Kolibri
##############################
 
You can track progress of the **Learners**, create and assign **Lessons** and **Quizzes** to classes or learner groups from the |coach| **Coach** dashboard. The default view presents the list of |classes| **Classes** with their assigned coaches, and the number of learners enrolled in each class.

Click on a class to access the progress-tracking features and create lessons, quizzes and groups.

	.. figure:: /img/coach-home.png
	  :alt: Open the Coach page to view the list of classes

	  Choose one of the classes from this view to access the Kolibri coach features.

.. note:: Kolibri progress tracking features are available by default in the *classroom model*, when learner devices are in the same local network as those used by coaches. However, in case of the at-home usage on personal devices, it is necessary to :ref:`sync facility data between devices <sync_facility>` for coaches to be able to track learner interactions with resources that happen while they are outside of the local network.


..  raw:: html

    <iframe width="670" height="380" src="https://www.youtube-nocookie.com/embed/xERcrV2UgzA?rel=0&modestbranding=1&cc_load_policy=1&iv_load_policy=3" frameborder="0" allow="accelerometer; gyroscope" allowfullscreen></iframe><br /><br />

Captions for the video are available in English, French, Swahili, Arabic, Hindi, Marathi and Brazilian Portuguese.


.. _track_progress:


Class home
~~~~~~~~~~

On the |dashboard| **Class Home** tab you can see the overview of the class activity and track progress of the learners on lessons and quizzes assigned to them.

	.. figure:: /img/class-home.png
	  :alt: Open the Coach page to view the list of classes

	  Class Home presents an overview of learner progress and activity.


Quizzes
-------

You can review the progress of learners on the assigned quizzes in the |quiz| **Quizzes** block.

* Progress bar will indicate how many learners have |inProgress| started and |mastered| completed the quiz.
* You can click on the progress bar to open the complete quiz data in the |reports| **Reports** tab.
* Click :guilabel:`VIEW ALL` to access the full list of notifications about quizzes (only the 3 most recent are displayed in the block).

.. note::
  **Quizzes** were known as **Exams** in Kolibri versions prior to 0.12.


Lessons
-------

You can review the progress of learners on the assigned lessons in the |lesson| **Lessons** block.

* Progress bar will indicate how many learners have |inProgress| started and |mastered| completed the lesson, and if they |helpNeeded| need help with some of the resources in it.
* You can click on the progress bar to open the complete lesson data in the |reports| **Reports** tab.
* Click :guilabel:`VIEW ALL` to access the full list of notification about lessons (only the 3 most recent are displayed in the block).


Class activity
--------------

As learners interact with lessons and quizzes, you can track their progress in the **Class activity** block. 

* When learners start or complete lessons, you will see one notification displaying the title of the lesson they |inProgress| started or |mastered| completed, and another displaying the title of the specific resource in the lesson they interacted with. In case of quizzes, you will see only the quiz title notification.
* When multiple learners are working on the same lesson or quiz, you will see a notification like *Learner1 and 3 other have started...*
* When learners input multiple incorrect answers to a question in a lesson, the notification in the **Class activity** block will display that one or more learners |helpNeeded| need help with a specific resource.
* You can click each notification link to review the complete resource data in the |reports| **Reports** tab.
* Click :guilabel:`VIEW ALL` to access the full list of activity notifications (only the 5 most recent are displayed in the block).
* Click the *View learners* link under the class name to review which learner devices are connected to the central Kolibri server, and when did they last synced the progress activity.
  
  .. figure:: /img/sync-learners.png
  	:alt: 


.. tip:: Click the *Information about sync statuses* link for more details.
	
	  .. figure:: /img/sync-statuses.png
  		:alt: 


.. _reports:


Reports
~~~~~~~

The |reports| **Reports** tab allows you to gain insight into detailed real-time progress of the learners for single resources in lessons and quizzes assigned to them.

Kolibri presents actionable reports for each lesson and quiz the class learners have been assigned, together with the possibility to observe the progress by groups and individual learners.

.. toctree::
  :maxdepth: 1

  reports_lessons
  reports_quizzes
  reports_groups
  reports_learners


.. figure:: /img/class-reports.*
  :alt: Open the Reports tab to track detailed learner progress

.. TO-DO (image)

Print and export coach reports
------------------------------

On any coach report where you see the |print| (print) and |download| (download) buttons, you will be able to print on paper, save in a PDF format, or export as a CSV file, for further analysis or to share with others. Follow these steps.

#. Click the |print| (print) button for the report you want to print or save as PDF file on your local drive.
   You will either have to select your paper printer device, or the *Save as PDF* option in the print dialog.
    
#. Click the |download| (download) button for the report you want to export as CSV file on your local drive. 



Plan
~~~~

Use the options in the |edit| **Plan** tab to create and manage the lessons, quizzes, and groups for the selected class.

.. toctree::
  :maxdepth: 1

  lessons
  quizzes
  groups

.. _coach_resource:


Coach support resources
~~~~~~~~~~~~~~~~~~~~~~~

`Kolibri Studio <https://studio.learningequality.org/>`_ supports the option to set visibility for any resource added to channels as a |coachContent| **Coach resource**. These materials can be lesson plans, professional development readings, training materials, etc. only viewable by coaches and not learners. When content curators set the visibility this way, the resource will not be visible by learners while browsing Kolibri |channel| **Channels**, but only to admins, facility coaches, or other users assigned to coach classes. 

However, coach can decide to include any of these resources in :ref:`lessons <manage_lessons>` or :ref:`quizzes <manage_quizzes>`, in which case they will be visible to learners in the context of that lesson or a quiz.

	.. figure:: /img/coach-resource-studio.png
	  :alt: In Kolibri Studio content curators can set the visibility for a single resource, or for the entire topic.

	  Setting the visibility of resources in Kolibri Studio.

Coach resources and channels that contain them are marked with the |coachContent| (coach resource) icon in Kolibri.

	.. figure:: /img/coach-resource.png
	  :alt: Indicators of the number of available coach support resources for all the channels are visible on the Kolibri Learn page, inside each channel card.

	  Channel with 4 support resources for coaches in Kolibri.

..  raw:: html

    <iframe width="670" height="380" src="https://www.youtube-nocookie.com/embed/jXoMLViGI3I?rel=0&modestbranding=1&cc_load_policy=1&iv_load_policy=3" frameborder="0" allow="accelerometer; gyroscope" allowfullscreen></iframe><br /><br />

Captions for the video are available in English, French, Swahili, Arabic, Hindi, Marathi and Brazilian Portuguese.
