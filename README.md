# Mach-Eight-Sample-Project
This repository is created to upload the proyect for Mach Eight.

The purpose of the project is to create an application that takes a single integer input and with the data from the website above (https://mach-eight.uc.r.appspot.com), print a list of all pairs of players whose height in inches adds up to the integer input by the user.

To run the application use python with the libraries jason and requests installed, if you do not have this libraries use pip to install them. Also, you can use Spyder to run and edit the python file.

When the application start the user has to enter an integer or a error will be display on the terminal, if there is no matches for the input number a message of "No matches found" will appear. Finally, to shut down the application the user has to write "exit".

#How the solution works
The solution works with a hash table or dictionary called in python. With this dictionary the data check is only iterate one time reducing considerly time of operation.
The keys of the dictionary are the heights of the players and the values are the players names, with that structure configuration you can look for all the players with a specific height.
