
.. _manage_quizzes:

Quizzes
#######

You can view, create and delete quizzes, assign them to learners, as well as access the progress reports on resources included in each quiz, in the **Quizzes** tab of your |coach| **Coach** dashboard. The default view displays the list of all quizzes in the selected class, their size, average score, groups they are assigned to, and their status and progress indicators.

.. figure:: /img/quizzes-home.png
  :alt: 

.. note::
  To manage |quiz| **Quizzes** in Kolibri classes and groups you must sign in as **coach**, **admin** or **super admin**.

Manage quizzes
--------------

Create new quiz
"""""""""""""""

To create a new |quiz| quiz, click the :guilabel:`NEW QUIZ` button and select **Create new quiz**.

#. Fill in the field for the quiz title in the *Create new quiz* |nbrs| page.
#. Select the *Report visibility* to learners: either after each learner submit their quiz, or after the coach ends the quiz.
#. Select the learners and groups to whom you wish to assign the quiz under the *Recipients* heading.
#. Quiz can have one or more sections. 
    * You can choose between **Randomized** and **Fixed** section order (default).
    * Click the :guilabel:`+ ADD SECTION` button to add more sections to the quiz. |br|
#. Click the :guilabel:`+ ADD QUESTIONS` button to select and add questions from exercise resources in the library.
#. Adjust the number of questions you want the quiz to contain. You can use the arrow field value modifiers with the mouse, or :guilabel:`-` and :guilabel:`+` buttons if you are using the keyboard.

   * The default value is 10, and it is not recommended that you add more than 25 questions to a section.
   * When you proceed, Kolibri will automatically add the chosen number of questions from the exercise resources you select in the next step.
   * Activate the **Choose questions manually** if you prefer to select the individual questions manually (instead of letting Kolibri add random questions from the selected exercise resources).

#. Click the :guilabel:`CONTINUE` button.
#. Select a channel from the library, navigate through the topic tree and activate checkboxes of the exercises you want Kolibri to add questions from, to include in the quiz. 

   * At the bottom of the page you can see the link **(number) resources selected** that allows you to review and change the selected resources. 

#. Use the **Search** feature to look for topics and exercises about a specific subject. 

   * Write the search term in the field, press the :guilabel:`ENTER` key or click the |search| (search) button to display the results.

   * You can filter the search results by *category* of resource, include only those from a specific *language* or *level*.

#. When you are done, click the :guilabel:`+ ADD (number) QUESTIONS` to return to the main view of the quiz.
#. There are several features to help you work with questions:

   * Click on the question title to expand and review the full content of the question, and click the title again to collapse it back.
   * Use the |collapseAll| (collapse all) and |expandAll| (expand all) buttons to open and close the full content of all questions in the section.
   * Select and auto-replace |autoReplace| or manually replace |refresh| questions from the same resources you selected in the steps above.
   * Select and remove |trash| questions from the section.
   * Reorder the questions in the section by using the |dragHorizontal| (drag) button with the mouse (drag and drop), or with |chevronUp| (up) and |chevronDown| (down) buttons if you navigate by keyboard.

#. Use the :guilabel:`OPTIONS` button to access the |edit| **Edit section**, |delete| **Delete section**, and |plus| **Add more questions** features.

#. Click :guilabel:`SAVE` button to save the current state and continue adding or reordering questions, or the :guilabel:`SAVE & CLOSE` button, to finish editing the quiz (you will see a confirmation notification at the bottom). 

Start and end quiz
""""""""""""""""""

Newly created quizzes are by default *not started*, meaning that learners will not see them in the **Learn > Classes** view. 

* Click the :guilabel:`START QUIZ` button to enable learners to see the quiz and start answering the questions. Button will change the label to indicate that the quiz is now opened for learners, and can be *ended*.

* Click the :guilabel:`END QUIZ` button once the designated time had passed, and you want to stop learners from interacting with it.
  
  .. .. figure:: /img/start-end-quiz.png
    :alt: 


.. warning:: You can edit all the quiz features, including adding and changing questions, **until you start the quiz**. Once the quiz is **started** you will be able to edit the title, visibility of the report, recipients and the order of sections, **but you will not be able to add or change the questions**.


Change quiz recipients
""""""""""""""""""""""

Newly created quizzes are by default visible to entire class. To change quiz *Recipients*, that is select groups or individual learners instead of the whole class, follow these steps.

#. Click to open a quiz from the list in the **Quizzes** tab.
#. Click the |optionsHorizontal| (options) button and select **Edit details** option.
#. Select the learners and groups to whom you wish to assign the quiz under the *Recipients* heading.
#. Click :guilabel:`SAVE` button to save the current state and continue editing, or the :guilabel:`SAVE & CLOSE` button, to finish editing the quiz (you will see a confirmation notification at the bottom). 

.. .. figure:: /img/exam-visibility.png
    :alt: 

Copy quiz
"""""""""

To copy a quiz to a different group or another class, follow these steps.

#. Click to open a quiz from the list in the **Quizzes** tab.
#. Click the |optionsHorizontal| (options) button and select **Copy quiz** option.
#. Select the class to which you wish to copy the quiz to and click :guilabel:`CONTINUE`.
#. Select the entire class, groups or inidividual learners to whom you wish to assign the quiz under the *Assign quiz to* heading.
#. Click :guilabel:`COPY` to confirm, or :guilabel:`CANCEL` to exit without change.

If the quiz is copied to another group in the same class, it will appear in the **Quizzes** tab as the *Copy of...*. Follow the steps in the next section to rename it.

Rename quiz
"""""""""""

To rename quiz, follow these steps.

#. Click to open a quiz from the list in the **Quizzes** tab.
#. Click the |optionsHorizontal| (options) button and select **Edit details** option.
#. Change the quiz title and/or the description.
#. Click :guilabel:`SAVE` button to save the current state and continue editing, or the :guilabel:`SAVE & CLOSE` button, to finish editing the quiz (you will see a confirmation notification at the bottom). 

Delete quiz
"""""""""""

To delete quiz, follow these steps.

#. Click to open a quiz from the list in the **Quizzes** tab.
#. Click the |optionsHorizontal| (options) button and select **Delete** option.
#. Click :guilabel:`DELETE` in the confirmation window to proceed, or :guilabel:`CANCEL` to exit without deleting the quiz.

.. warning::
  All data from the quiz you are deleting will be lost.


View learner progress in quizzes
--------------------------------

In the main view of the **Quizzes** tab you can view the summary of the progress for all quizzes created in the class. 

* **Average score** in the first column is calculated only from quizzes that were completed.
* **Progress** column presents the summary of learners that |inProgress| *started* and |mastered| *completed* each quiz.
* The **Status** column indicates whether the quiz is *opened* for learners (whether they can still answer the questions), or whether the quiz has *ended*. It also indicates whether the quiz is still visible to learners in the **Learn > Classes** view.

.. .. figure:: /img/quizzes.*
  :alt: 

.. TO-DO (image)

#. Click on the quiz title to review progress in detail.
#. In the **Learners** sub-tab, you can see the list of learners, with columns for the *progress* and obtained *score*.
#. Open the **Difficult questions** sub-tab to view the list of questions learners gave incorrect answers to, and gain insight of how many |helpNeeded| *need help* with the concept.
#. Click a *difficult question* in the list to review each of the incorrect answers and attempts.
   
#. When you click a name of a single learner, you can see the full report for each answer. This can help you understand which questions learners had difficulties answering correctly, and how many attempts they used.
  
   * |correct| green check mark icon indicates the **correct** answer
   * |incorrectReport| red X mark icon indicates the **incorrect** answer
   * |delete| gray X mark icon indicates an **unanswered** question

     .. figure:: /img/exam-report-detail.png
       :alt: 

Print and export coach reports
""""""""""""""""""""""""""""""

Whenever you see the |print| (print) and |download| (download) buttons, you will be able to print the report on paper, save in a PDF format, or export as a CSV file, for further analysis or to share with others. Follow these steps.

#. Click the |print| (print) button for the report you want to print or save as PDF file on your local drive. You will either have to select your paper printer device, or the *Save as PDF* option in the print dialog.
    
#. Click the |download| (download) button for the report you want to export as CSV file on your local drive. 
