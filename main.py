
#!/usr/bin/env python

import os
import time

# Pull "dev"
os.system('git pull origin dev')

# Build
#os.system('make build')

# Test
if os.system('python3 test/NombresRomainsTest.py') == 0:
    # Rebase + Fast Forward the commit tested on "main"
    os.system('git rebase --onto origin/master origin/dev')
else:
    timestamp = time.strftime('%Y%m%d_%H_%M')
    # Move the commit to the failures branch
    os.system('git branch failures/{}'.format(timestamp))
    os.system('git reset --hard HEAD~1')
    os.system('git checkout failures/{}'.format(timestamp))
    os.system('git add .')
    os.system('git commit -m "Test failure {}"'.format(timestamp))