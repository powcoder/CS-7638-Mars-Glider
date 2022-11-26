https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
Grid Search Script for Parameter Tuning   - Josh O'Rourke.

Hello Everyone,

I've been working on this project for several days and many hours at this point. One thing that I've found extremely helpful as I experiment with the PF algorithm is a script that allows me to test many different values for sigma, noise, etc. . Another student asked about it on Slack, so I thought I'd share in case someone else finds it useful. 

 

The script works by using subprocess.Popen to run testing_suite_full.py in parallel with different environment variables. Inside of marsglider.py, I use `os.environ` to get the environment values specific to each process, like this:

 

import os
SIGMA = float(os.environ['SIGMA'])
NOISE = float(os.environ['NOISE'])  
FUZZ = float(os.environ['FUZZ'])   

 

The output looks like this (The values for SUCCEEDED are the results for Part A and Part B):

SIGMA 8.0 NOISE 7.0 FUZZ 0.75 SUCCEEDED ['9', '6']
SIGMA 8.0 NOISE 8.0 FUZZ 0.25 SUCCEEDED ['8', '5']
SIGMA 8.0 NOISE 8.0 FUZZ 0.33 SUCCEEDED ['9', '4']
SIGMA 8.0 NOISE 8.0 FUZZ 0.5 SUCCEEDED ['8', '6']

 

And finally, here is the script:  <gridsearch.py>
Hopefully, someone else finds this as helpful as I have. Good luck!

NOTE: May have issues with windows:

Q: Has anyone had success with this script on Windows? I'm running Win10, and the script is throwing:

WindowsError: [Error -2146893795] Provider DLL failed to initialize correctly

The traceback specifically seems to relate to the random.py default library, but I don't have much of an inclination on why this might be the case. Any ideas, or similar issues others are running into?

A: It's related to the environment setup. In windows you need to copy the environment first it seems.
I got it running by following this: https://stackoverflow.com/questions/21791005/windows-error-provider-dll-failed-to-initialize-correctly-on-import-of-cgi-mo

BUT it didn't really work very reliably once it did get running, so im now setting up a Ubuntu VM.

