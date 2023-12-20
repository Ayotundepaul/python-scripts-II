#!/bin/bash

# Specify the number of commits you want to create
NUM_COMMITS=10

# Loop to create commits
for (( i=1; i<=NUM_COMMITS; i++ ))
do
    # Append current date and time to a file
    echo "Commit number $i on $(date)" >> commit_log.txt

    # Add the file to the staging area
    git add commit_log.txt

    # Commit the change
    git commit -m "Automatic commit number $i"

    # (Optional) Sleep for a second to ensure a different timestamp for each commit
    sleep 1
done

# Push commits to the remote repository
# Uncomment the line below to enable pushing
# git push origin main
