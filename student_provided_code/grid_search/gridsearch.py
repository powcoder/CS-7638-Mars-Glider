https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder

# gridsearch.py

import os
import sys
import re
import subprocess
from queue import Queue


MAX_PROCESSES = 4

sigmas = [1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]
noises = [1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]
fuzzes = [.25, .33, .5, .66, .75]

queue = Queue(maxsize=MAX_PROCESSES)

def enqueue(sigma, noise, fuzz):
    env = {'SIGMA': str(sigma), 
           'NOISE': str(noise), 
           'FUZZ': str(fuzz),
           'OBJC_DISABLE_INITIALIZE_FORK_SAFETY': 'Yes' } # for macos

    #sys.executable should be the python3 executable that you are using to run
    #this script.
    p = subprocess.Popen([sys.executable, 'testing_suite_full.py'],
                         stdout=subprocess.PIPE,
                         env=env)

    queue.put((p, env))


def dequeue():
    p, env = queue.get()
    p.wait()

    result = p.stdout.read()
    matches = re.findall(r'Successes: (\d+)', result)

    print('SIGMA', env['SIGMA'], \
          'NOISE', env['NOISE'], \
          'FUZZ', env['FUZZ'], \
          'SUCCEEDED', matches)


if __name__ == "__main__":
    for sigma in sigmas:
        for noise in noises:
            for fuzz in fuzzes:
                if queue.full():
                    dequeue()
                enqueue(sigma, noise, fuzz)

    while not queue.empty():
        dequeue()
