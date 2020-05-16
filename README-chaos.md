This is a readme file, so you probably want to know how my code works. Once again, feel free to leave a comment or an issue.
Also, I want project ideas to do, so feel free to leave those too.
You sould take a look at my code. First, after importing the librarys, it defines a function called main. You can do without main, but it makes the code neater and more readable.
If you don't know what a function is, It is a block of code that sits there doing nothing until called. You'll notice the last line. 
That is the function call. If you didn't include it, the code won't raise an error, but it won't do anything. You probably want to go to 
https://www.w3schools.com/python/python_functions.asp to learn more from pros 
Next, it starts a while loop to keep on sking for a seed until you enter '0000'(the break seed.change it to whatever you like)
The first thing in the while loop is a blank list. I'll explain it later.
Then, it asks for a seed, and converts the answer to an integer. 
After that, there's a if statement to end the program if you enter 0000 as a seed.
Then it sets the seed for the random number generator as the input. 
Finally! We're getting somewhere good!
On line 11, it starts a for loop to run 100 times.
Each time it runs, it generates a new random number. Remember that blank list? Because after it generates the random number, it appends the random number to that list.
Then, it's a simple matter to plot the appended list with matplotlib.pyplot.
Thank you for reading this and for staring me.
