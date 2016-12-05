# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> >What do the following commands do:  
ls : lists files,directories in the current directory  
ls -a: list with hidden files/directories: 
ls -l:  '-l' tells the command to use a long list format. It gives back several columns wich correspond to:
Permissions
Number of hardlinks
File owner
File group
File size
Modification time
Filename 
ls -lh: List Files with Human Readable Format 
ls -lah: Returns more comprehensive information about your files and directories compared just to ‘plain’ command ls  
ls -t:  Sorts files/directories list by time/date.
ls -Glp: Displays long format listing (excluding the owner name) and directories are shown with /

---

###Q2.  List Files in Unix   

> > ls -option filename

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls -a; ls -1; ld -R; ls -d; ls -F

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs is a command on Unix and most Unix-like operating systems used to build and execute command lines from standard input. Commands such as grep and awk can accept the standard input as a parameter, or argument by using a pipe. However, others such as cp and echo disregard the standard input stream and rely solely on the arguments found after the command. Additionally, under the Linux kernel before version 2.6.23, and under many other Unix-like systems, arbitrarily long lists of parameters cannot be passed to a command,[1] so xargs breaks the list of arguments into sublists small enough to be acceptable.

 

