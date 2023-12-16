import git
from pathlib import Path

# Get the current working directory and Set.
repo = git.Repo(Path.cwd())

# Remote origin and set to main branch.
origin = repo.remote(name='origin')
existing_branch = repo.heads['main']
existing_branch.checkout()

# Check status
print(repo.git.status())

# Add files
repo.index.add('*')

# Input commit message.
repo.index.commit(
    input("Enter commit message: "),
)

# Push all the code.
origin.push()

print('\n Added, Commited & Pushed successfully \n')
