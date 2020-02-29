# CS 1XA3 Project01 - <nasirn4>
## Usage
Execute this script from project root with:
chmod +x CS1XA3/Project01/project_analyze.sh
./CS1XA3/Project01/project_analyze feature1 feature2 feature3
With arguments
        feature1: File Size List
        feature2: File Type Count
        feature3: FIXME log
	feature4: Switch to Executable
	feature5: Find Tag
	feature6: Checkout Latest Merge
	feature7: Custom Feature 1
	feature8: Custom Feature 2 

....
### Feature 01
*Description:* List all files in the repo and their sizes in integer format in descending order
using the flag -rn.
*Execution:* Run the script ./project_analyze.sh feature1 . .
*Reference:* some code was taken from [[https://stackoverflow.com/questions/18193392/how-to-sort-a-file-in-unix-both-alphabetically-and-numerically-on-different-fiel]]

### Feature 02
*Description:* Using the read command, the user is prompted for an extension such as txt, pdf, py.
In order to get rid of the absolute path, a variable parent_path was created that gets the
absolute path of the script and then uses that to get the parent directory by cd-ing into it.
*Execution:* Run the script ./project_analyze.sh . feature2 .
Make sure to just type in the extension without the '.' before it.
*Reference:* some code was taken from [[https://tecadmin.net/prompt-user-input-in-linux-shell-script/]]
				    [[https://stackoverflow.com/questions/24112727/relative-paths-based-on-file-location-instead-of-current-working-directory/24113238]]

### Feature 03
*Description:* Find every file in the repo that has the word #FIXME in the last line using find for
the file, tail -1 for the last line and grep for the word. It then puts list of the file names in
CS1XA3/Project01/fixme.log with each gile seperated by a newline. 
*Execution:* Run the script ./project_analyze.sh . . feature3
Then type in ls and you will find the file fixme.log. Type in less fixme.log and you will be able
to view the contents of this file.
*Reference:* some code was taken from [[https://unix.stackexchange.com/questions/107067/tail-multiple-files-and-output-as-additional-column-with-find-results]]
...

### Feature 04
*Description:* This feature finds all shell script files in the repo. The user is prompted to type in change or restore.
If the user selects change, for each shell script, the permissions for the file are changed so that
only the user who has write permissions has executable permissions. The log of the file and its' original permissions is stored in permissions.log which is created or overwrited if it does not exist.
If the user selects Restore, restores each file to its original permissions.
*Execution:* Run the script ./project_analyze.sh . . . feature4 . . . .
Then user is prompted to type in restore or change, all lower case.
*Reference:* some code was taken from [[https://stackoverflow.com/questions/2331936/bash-scripting-and-bc]]
                                      [[https://www.unix.com/unix-for-dummies-questions-and-answers/89791-cut-usage-bash.html]

### Feature 05
*Description:* This feature prompts the user to type in the name of a tag (a single word) and for each python file in the repo, finds all the lines that begin with a comment and include Tag and puts them$
This file CS1XA3/Project01/Tag.log is either created or overwrited if it already exists.
*Execution:* Run the script ./project_analyze.sh . . . . feature5 . . .
Then user is prompted to type in a tag. Then user must type in ls where they will find the tag.log file.
After, the user can type in less tag.log and view the contents of this file.
*Reference:* some code was taken from [[http://www.cs.columbia.edu/~tal/3261/fall07/handout/egrep_mini-tutorial.htm]]

### Feature 06
*Description:* This feature finds the most recent commit with the word merge in the commit message.
It then automatically checkouts that commit.
*Execution:* Run the script ./project_analyze.sh . . . . . feature6 . .
*Reference:* some code was taken from [[https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History]]

...

### Custom Feature 01
*Description:* This feature creates a file CS1XA3/Project01/sortedprocesses.log if it doesn't exist,
if it does exist overwrite it.
This file will contain a list of all the process identification numbers sorted in descending order.
*Execution:* Run the script ./project_analyze.sh . . . . . . feature7 .
Then type in ls and you will find the file sortedprocesses.log. Type in less sortedprocesses.log
and you will be able to view the contents of the file.
*Reference:* some code was taken from [[https://www.linuxquestions.org/questions/linux-newbie-8/sorting-ps-output-4175598163/]]

### Custom Feature 02
*Description:* This feature removes duplicate lines from all files.
It creates a file CS1XA3/Project01/removedlines.log where a list of all removed lines is stored.
*Execution:* Run the script ./project_analyze.sh . . . . . . . feature8
Then type in ls and you will find the file removedlines.log. Type in less removedlines.log and
you will be able to view the contents of this file.
*Reference:* some code was taken from [[https://stackoverflow.com/questions/10523415/execute-command-on-all-files-in-a-directory]]
                                      [[https://www.cyberciti.biz/faq/unix-linux-shell-removing-duplicate-lines/]]
