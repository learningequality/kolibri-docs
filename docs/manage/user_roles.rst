.. _user_roles:

Default User Roles
##################

Kolibri users by default can be divided in 3 different roles with respective access to features. 

+------------------------------------------------------------------------------------------------------+
| Default user roles                                                                                   |
+======================================================================================================+
| **Learners** can:                                                                                    |
|  * View content and have their progress tracked                                                      | 
+------------------------------------------------------------------------------------------------------+
| **Coaches** can:                                                                                     |
|  * View content and have their progress tracked                                                      |
|  * View *Coach* dashboard and track progress of other users and usage stats for individual exercises |
|  * Create/Edit/Delete *Groups* in *Classes* and add users to them                                    |
|  * Create/Edit/Delete *Quizzes* and assign them to users                                             |
|  * Create/Edit/Delete *Lessons* and assign them to users                                             |
|                                                                                                      |
|  *Facility coaches* have access to all classes, *class coaches* only to ones they are assigned to    |
+------------------------------------------------------------------------------------------------------+
| **Admins** can:                                                                                      |
|  * View content and have their progress tracked                                                      |
|  * View *Coach* dashboard and track progress of other users and usage stats for individual exercises |
|  * Create/Edit/Delete other **admins**, **coaches**, and **learners**                                |
|  * Create/Edit/Delete *Classes* and enroll users in them                                             |
|  * Create/Edit/Delete *Groups* in *Classes* and add users to them                                    |
|  * Create/Edit/Delete *Quizzes* and assign them to users                                             |
|  * Create/Edit/Delete *Lessons* and assign them to users                                             |
|  * View/Edit *Facility configuration* settings                                                       |
|  * Export *Detail* and *Summary* logs usage data                                                     |
+------------------------------------------------------------------------------------------------------+

Kolibri Super Admins
--------------------

Kolibri **super admin** users have all device permissions, and are able to :ref:`assign them to other users <permissions>`. Therefore **super admin** users can:

+------------------------------------------------------------------------------------------------------+
|  * View content and have their progress tracked                                                      |
|  * View *Coach* dashboard and track progress of other users and usage stats for individual exercises |
|  * Create/Edit/Delete other **admins**, **coaches**, and **learners**                                |
|  * Create/Edit/Delete *Classes* and enroll users in them                                             |
|  * Create/Edit/Delete *Groups* in *Classes* and add users to them                                    |
|  * Create/Edit/Delete *Quizzes* and assign them to users                                             |
|  * Create/Edit/Delete *Lessons* and assign them to users                                             |
|  * View/Edit *Facility configuration* settings                                                       |
|  * Export *Detail* and *Summary* logs usage data                                                     |
|  * Import/Export *Content* channels                                                                  |
|  * View/Edit *Permissions* of other users                                                            |
+------------------------------------------------------------------------------------------------------+

.. tip::
   If you are unable to retrieve the username and password for a super admin account in your facility, you can :ref:`create a new super admin account using the command line <create_superuser>`.

Assign Additional Permissions
-----------------------------

By default, only **super admin** users can view the **Device** dashboard, import/export **Content** channels in Kolibri, and modify **Permissions** for other users. However, depending on the needs of the institution, **super admin** users can also :ref:`grant these permissions <permissions>` to other users.