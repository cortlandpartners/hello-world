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

1. Install Git in your local development environment (laptop/desktop)

1. Create Repository in GitHub. Either under your organizations or your personal account. Click on the "New" button
![alt text](images/NewRepository.JPG "New Repo")

1. Add a descriptive `lowercase-with-hyphens` name, do not initialize a README this time and click on Create.

1. **Scenario 1** - Repository already exists in GitHub and you have code already in your local

    - **Terminal** -  Replace <<repository-url>> with your GitHub repo URL. i.e. https://github.com/cortlandpartners/hello-world
    
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
    # add your all your new and modified (".") changes to the staging area
    $git add .
    # push local changes to the remote specified branch
    $git push origin develop
    ```
 1. **Scenario 2** - Repository already exists and your local environment is empty (Recommended)
    (Via HTTPS)
    ```bash
    $cd <<project-parent-folder>>
    $git clone https://github.com/cortlandpartners/<<repository-name>>.git

    ```
    

    

