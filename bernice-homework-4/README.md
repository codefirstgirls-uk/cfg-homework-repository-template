## TASK 1 (GIT and GitHub)

### Question 1

#### GIT WORKFLOW FUNDAMENTALS

**1. Working Directory**

A Git repository tracks and saves the history of all changes made to the files in a Git project. 
It saves this data in a directory called . git , also known as the repository folder. 

**2. Staging Area**

Staging area is files that are going to be a part of the next commit, which lets git know what 
changes in the file are going to occur for the next commit.

**3. Local Repo(head)**

When working with Git, only one branch can be checked out at a time - and this is what's called the "HEAD" branch. 
Often, this is also referred to as the "active" or "current" branch. Git makes note of this current branch in a file 
located inside the Git repository, in .git/HEAD. 

**4. Remote repo(master)**

It's a default branch of Git. After cloning a project from a remote server, the resulting local repository contains 
only a single local branch. This branch is called a "master" branch. It means that "master" is a repository's "default"
branch.


#### WORKING DIRECTORY STATES:

**1. Staged**

A staging step in git allows you to continue making changes to the working directory, and when you decide you want to
interact with version control, it allows you to record changes in small commits.

**2. Modified**


As you edit files, Git sees them as modified, because you've changed them since your last commit. As you work, you 
selectively stage these modified files and then commit all those staged changes, and the cycle repeats.

**3. Committed**

A file in the committed state means that the changes made to it are safely stored in a snapshot in the Git directory.
A file is committed using git commit command.This command creates a new snapshot in the Git directory and shows us 
some stats for the change made.

#### GIT COMMANDS:

**1. Git add**

The git add command adds a change in the working directory to the staging area. It tells Git that you want to 
include updates to a particular file in the next commit.

**2. Git Commit**

The git commit command captures a snapshot of the project's currently staged changes. Committed snapshots can be
thought of as “safe” versions of a project—Git will never change them unless you explicitly ask it to.

**3. Git push**


The git push command is used to upload local repository content to a remote repository. Pushing is how you transfer
commits from your local repository to a remote repo. 

**4. Git fetch**

Git fetch will fetch all the changes in the remote repository (GitHub) and move the origin/master pointer to HEAD.
Meanwhile, your local branch master will keep pointing to where it has.

**5. Git merge**


Git merge is a command that allows you to merge branches from Git. 

**6. Git pull**

The git pull command is used to fetch and download content from a remote repository and immediately update the local repository to match that content. 