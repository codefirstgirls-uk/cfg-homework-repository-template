## GIT WORKFLOW FUNDAMENTALS
* **Working Directory** - same as your folder with your work, where you can see all of the changes (history) of files. 
* **Staging Area** - is the place where you have files that are not yet committed, but are ready to be committed. It is the area between directory and repository. 
* **Local Repo (head)** - Your local repository latest committed state (latest commit).
* **Remote repo (master)** - Repository that is hosted on the remote machine and contains latest pushed commits to the master branch. Remote repositories can be accessed by others. 

## WORKING DIRECTORY STATES 
* **Staged** -state where all changes are made and file is ready to be committed to the local database.
* **Modified** - if we change anything in the file, then the state committed changes to modified, because file has changed since we last commited it in the local database.
* **Committed** - it means that your file is saved in the local database.

## GIT COMMANDS
* **Git add** - command that moves file changes from working directory to staging. 
* **Git commit** - saves staged changes to the local repository. 
* **Git push** - command pushes all committed changes from local repository to remote repository.
* **Git fetch** - command takes all of the content from the remote repository and downloads them into your local repository. Changes are not applied to files.
* **Git merge** -command lets you take multiple branches and put them together, mostly used for the main branch. 
* **Git pull** - command takes content  from remote repository to local repository and applies to changes to files. 

