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

**Repository** - organizes a single project, they can contain folders and files, images, videos, spreadsheets and data sets

**Branching** - is the way to work on different versions of a repository at one time


### Step-by-step guide

1. Sign up for an account in GitHub or receive an organization invitation

1. [Download](https://git-scm.com/downloads) and install Git in your local development environment (laptop/desktop)

1. Create Repository in GitHub. Either under your organizations or your personal account. Click on the "New" button
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
 1. So far we have used the big git commands, don't forget to also use `git help`. It is seriously very helpful if you're starting out.
  
    

    

