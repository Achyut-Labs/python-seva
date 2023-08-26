# HOW DOES GITHUB WORK:
-
→

**SCM**- SOURCE CODE MANAGEMENT
→ Github is known as a ***SCM*** Tool

→ We have a ***Server*** and a ***Local***

Our server is Github.com

# SERVER: 
SERVER: GITHUB.COM


 Under github we have:  
        GITHUB
          ↆ
          PROJECT 
            ↆ
             BRANCHES

# Local
 Our branch is known as Local

Under Local we have:
        DEVELOPMENT
          ↆ
          STAGING/RELEASE
            ↆ
             MASTER → Your Branch! AKA Local


# Mirroring:
Whatever you have in the server you have in the local. Every time you pull and push your code, you update it into the server. That means that everytime your code is updated, whatever is in your local, will also be in the server. This is known as "mirroring"

# Cloning
We can also clone our local branch.
When you clone a repository, you copy the repository from GitHub.com to your local machine. Cloning a repository pulls down a full copy of all the repository data that GitHub.com has at that point in time, including all versions of every file and folder for the project.

# To Properly be up to date we must:
→Make sure you have commited everything from your branch
→ go into the main branch
→gitpull main
→Switch branches.
→in aira's branch → git merge main
→ Git Pull
→ Git Push

# So Then What are Conflicts? And Why do We Have Them?
Often, merge conflicts happen when people make different changes to the same line of the same file, or when one person edits a file and another person deletes the same file. You must resolve all merge conflicts before you can merge a pull request on GitHub.\

# Stashing Changes
To apply your changes to your repository, you must save the files and then commit the changes to a branch. If you have saved changes that you are not ready to commit yet, you can stash the changes for later. When you stash changes, the changes are temporarily removed from the files and you can choose to restore or discard the changes later. You can only stash one set of changes at a time with GitHub Desktop. If you use GitHub Desktop to stash changes, all unsaved changes will be stashed. After you stash changes on a branch, you can safely change branches or make other changes to your current branch.

If you use GitHub Desktop to switch branches while you have saved, but not committed, changes, GitHub Desktop will prompt you to stash the changes or bring them to the other branch. 
