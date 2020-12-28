.. _user_roles:

Default User Roles
##################

Kolibri users by default can be divided in 3 different roles with respective access to features. 

+--------------------------------------------------+
| **Learners** have access to:                     |
+==================================================+
|.. figure:: /img/navbar-learner.png               |
+--------------------------------------------------+
| **Learners can**                                 |
+--------------------------------------------------+
| * View resources and have their progress tracked |
+--------------------------------------------------+

+----------------------------------+-----------------------------------------------------------------------------------------------------+
| **Coaches** have access to:                                                                                                            |
+==================================+=====================================================================================================+
|.. figure:: /img/navbar-coach.png                                                                                                       |
+----------------------------------+-----------------------------------------------------------------------------------------------------+
| **Coaches can**                                                                                                                        |
+----------------------------------+-----------------------------------------------------------------------------------------------------+
| * View resources and have their progress tracked                                                                                       |
+----------------------------------+-----------------------------------------------------------------------------------------------------+
| Access *Reports*                 | * View *Coach* dashboard and track progress of other users and usage stats for individual exercises |
+----------------------------------+-----------------------------------------------------------------------------------------------------+
| Access *Plan*                    | * Create/Edit/Delete *Groups* in *Classes* and add users to them                                    |
|                                  | * Create/Edit/Delete *Quizzes* and assign them to users                                             |
|                                  | * Create/Edit/Delete *Lessons* and assign them to users                                             |
+----------------------------------+-----------------------------------------------------------------------------------------------------+
| Note: *Facility coaches* have access to all classes, *class coaches* only to ones they are assigned to                                 |
+----------------------------------+-----------------------------------------------------------------------------------------------------+

+----------------------------------+------------------------------------------------------------------+
| **Admins** have access to:                                                                          |
+==================================+==================================================================+
|.. figure:: /img/navbar-admin.png                                                                    |
+----------------------------------+------------------------------------------------------------------+
| **Admins can**                                                                                      |
+----------------------------------+------------------------------------------------------------------+
| * View resources and have their progress tracked                                                    |
| * View *Coach* dashboard and track progress of other users and usage stats for individual exercises |
+----------------------------------+------------------------------------------------------------------+
| Access *Classes*                 | * Create/Edit/Delete *Groups* in *Classes* and add users to them |
|                                  | * Create/Edit/Delete *Quizzes* and assign them to users          |
|                                  | * Create/Edit/Delete *Lessons* and assign them to users          |
+----------------------------------+------------------------------------------------------------------+
| Access *Users*                   | * Create/Edit/Delete *Classes* and enroll users in them          |
+----------------------------------+------------------------------------------------------------------+
| Access *Settings*                | * View/Edit *Facility configuration* settings                    |
+----------------------------------+------------------------------------------------------------------+
| Access *Data*                    | * Export *Detail* and *Summary* logs usage data                  |
+----------------------------------+------------------------------------------------------------------+

Kolibri Super Admins
--------------------

Kolibri **super admin** users have all device permissions, and are able to :ref:`assign them to other users <permissions>`. In addition to **admin** user access, **super admin** users can:

+-------------------------------------------+
|  * Import/Export *Content* channels       |
|  * View/Edit *Permissions* of other users |
+-------------------------------------------+

.. tip::
   If you are unable to retrieve the username and password for a super admin account in your facility, you can :ref:`create a new super admin account using the command line <create_superuser>`.

Assign Additional Permissions
-----------------------------

By default, only **super admin** users can view the |device| **Device** dashboard, import/export channels in Kolibri, and modify |permissions| **Permissions** for other users. However, depending on the needs of the institution, **super admin** users can also :ref:`grant these permissions <permissions>` to other users.
