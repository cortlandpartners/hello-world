# Getting started with Git and GitHub

### What is Git?
   - Version Control System for tracking changes in source code files
   - Time Machine
   - Distributed version control (Developers in different networks)
   
### What is GitHub?
   - Social code-hosting platform for version control and collaboration , you can even host websites for free
   
In other words, Git is the control system and GitHub is a hosting service for Git with enhanced features

### Concepts of Git

- Keeps track of code history
- Takes "snapshots" of your files
- We decide when to take a snapshot by making a "commit"
- We can always go back in time and see a snapshot of our code
- We can put our code in a staging area
- Use our terminal or Git Bash's terminal

Git is a stream of snapshots (commits)

### GitHub Essentials - Repositories and Branches

**Repository** 
- A repository is like a folder for your project. Your project's repository contains all of your project's files and stores each file's revision history. You can also discuss and manage your project's work within the repository.
- A repository organizes a single project. It can contain folders and files, images, videos, spreadsheets and data sets.

**Branching** 
-  Use a branch to isolate development work without affecting other branches in the repository. Each repository has one default branch, and can have multiple other branches. You can merge a branch into another branch using a pull request.
-  Branching  is the way to work on different versions of a repository at one time.


___Think of a Repository as a place where all the code for an application is held. Developers on a team would use different branches to work on features, make enhancements, or fix bugs.___

### GitHub Essentials - Git Commands and Flags

**Commands to mention**
- `git init`
- `git clone`
- `git status`
- `git add`
- `git commit -m ''`
- `git push`

**Flags**
- Such as `-m`
-  Think of flags as arguments or parameters passed to the command. A flag    usually triggers a variation of the command executed. Flags are usually    seen as a hyphen followed by a letter `-h` or two hyphens followed by a    word `--help`
   One of the most important command and flag to know is `git help` and the `--help`/`-h` flag.

### GitHub Essentials - Repositories and Users

- Repositories can be public or private.
   - If the repository is public, it can be seen by anyone. It can be cloned/downloaded, people are allowed to fork your repository, create pull requests, create issues, etc.
   - If a repository is private, only collaborators of that repository are allowed to see it
	- Repositories can be owned by a user or an organization.
		- You can tell who it is owned by because of the naming convention: `user_or_organization/name_of_repository`
    		- `cortlandpartners/hello-world`
		- If the repository is owned by an organization, it can be owned by multiple users.
      - Users can also be collaborators as well as owners. 


### GitHub Interaction - Desktop Vs Terminal Vs Website
- There are multiple ways a user could interact with git and github. These include the follow:
  - Terminal: command prompt, powershell, bash, etc
  - Web: Using Github.com
  - Desktop: Install the desktop application
Using the terminal seems to be the most popular among developers. It also helps to memorize the process.

### Step-by-step guide

1. Sign up for an account in GitHub or receive an organization invitation

2. [Download](https://git-scm.com/downloads) and install Git in your local development environment (laptop/desktop)

3. Create Repository in GitHub. Either under your organizations or your personal account. Click on the "New" button
![alt text](images/NewRepository.JPG "New Repo")

1. Add a descriptive `lowercase-with-hyphens` name, do not initialize a README this time and click on Create.

1. It is recommended to introduce our user and e-mail to every repository
    ```bash
    $git config --global user.name "<your_user_name_here>"
    $git config --global user.email "<your@email.com>"
    ```
1. Getting started (Clone or fetch)
    1. **Initialize and fetch** - Repository already exists in GitHub and you have code already in your local. 
    
        Note: Replace <<repository-url>> with your GitHub repo URL. i.e. https://github.com/cortlandpartners/hello-world
      
        ```bash
        $cd <<project-folder>>
        # creates the "develop" branch
        $git checkout -b develop
        # initializes .git repo in our local environment
        $git init
        # creates a remote called "origin" linked to "GitHub repo's URL"
        $git remote add origin <<repository-url>>
        # downloads commits, files and refs from remote repository into our local
        $git fetch origin
        # check the status of my local working tree repo
        $git status
        # add your all your new and modified (".") changes to the staging area
        $git add .
        # push local changes to the remote specified branch
        $git push origin develop
        ```
        
     1. **Clone repository** - Repository already exists and your local environment is empty (Via HTTPS)
        ```bash
        $cd <<project-parent-folder>>
        $git clone https://github.com/cortlandpartners/<<repository-name>>.git
        ```
 1. So far we have used the most common git commands, don't forget to also use `git help`. It is seriously very helpful if you're starting out.
 
 1. Now, it is important to understand the following components:
    - Working directory (files) - write changes in our computer's files and represents a particular commit (snapshot)
    - index (staging area) - getting prepared to be packaged into a commit object
    - head (last commit) - point to your last commit on a branch in your Git repo
  
    

    

