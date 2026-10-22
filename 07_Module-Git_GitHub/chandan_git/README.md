# Git TUTORIAL REAME

This is a tutorial for git.

![images](https://miro.medium.com/1*mtsk3fQ_BRemFidhkel3dA.png)


# GIT and GitHub UseFull Command:-
=============================================GIT & GITHUB===========================================
• Git & GitHub Command:-
1. Repository & Setup Shortcuts:-
	i. Git init                               --     initialize new repository
	ii. Git clone <url>                       --     clone a repository
	iii. Git status                           --     Check status of files
	iv. Git config --global user.name "Name"  --     Set global user name
	v. Git config --global user.email "email" --     Set global email
	
2. Basic workFlow Shortcuts:-
	i. Git add .                              --     Add all changes
	ii. Git add <file>                        --     Add specific file
	iii. Git commit -m "Message"              --     commit chnages
	iv. Git commit -am "Message"              --     Add and commit (Tracked files)
	v. Git push                               --     Push changes to remote
	vi. Git pull                              --     Pull latest changes
			      
3. Branching Shortcuts:-
	i. Git branch                             --     List all Branches
	ii. Git branch <name>                     --     create a new branch
	iii. Git checkout <name>                  --     Switch to a branch
	iv. Git checkout -b <name>                --     Create and switch to new branch
	v. Git merge <branch>                     --     merge a branch
	vi. Git branch -d <name>                  --     delete a branch
			     
4. Undo & restore Shortcuts:-
	i. Git restore <file>                     --     Discard changes in a file
	ii. Git restore .                         --     Discard all changes
	iii. Git reset <file>                     --     Unstage a file
	iv. Git reset --hard                      --     Reset everything(***Be careful***)
	v. Git revert <commit>                    --     Undo a commit(safe)
	vi. Git clean -fd                         --     Remove untracked files & Folders
		
5. Stash Shortcuts:-
	i. Git stash                              --     Stash current changes (if u delete any file and you want back 
	                                                                        then use this command to get back)
	ii. Git stash list                        --     view stashes
	iii. Git stash apply                      --     Apply latest stash
	iv. Git stash pop                         --     Apply and remove latest stash
	v. Git stash drop                         --     Delete a stash
			       
6. Remote Repository Shortcuts(GITHUB):-
	i. Git remote -v                          --     View remote URLs
	ii. Git remote add origin <URL>           --     Add remote repository
	iii. Git push -u origin <branch>          --     Push and set upstream
	iv. Git fetch                             --     Fetch latest changes
	v. Git pull origin <branch>               --     Pull from the specific branch
	vi. Git push origin --delete <branch>     --     Delete remote branch
			         
7. Useful shortcuts:-
	i. Git log --online                       --     View commit history (short)
	ii. Git log --graph                       --     view commit history (graph)
	iii. Git diff                             --     show changes
	iv. Git show <commit>                     --     show commit details
	v. Git blame <file>                       --     see who changes a line
	vi. Git bisect                            --     Find the commit that introduced a bug
