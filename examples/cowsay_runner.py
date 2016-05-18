import sys
import os
from datetime import datetime
sys.path.insert(0, os.path.abspath('..'))
from multisarge import run_process, ProcessTask

# Matrix of parameters to feed into the `cowsay_cmd` function.
# The tuples here must all match the parameter signature of the `cowsay_cmd` function
PARAM_MATRIX = [
    ('moo', ''),
    ('moo', 'bunny'),
    ('moo', 'kitty'),
    ('moo', 'dragon'),
    ('moo', 'dragon-and-cow'),
    ('moo', 'cheese'),
]

# A timestamp to place on the whole run so later runs will not overwrite previous ones. This is recommended.
TIMESTAMP = datetime.now().strftime('%y-%m-%d_%H-%M-%S')


# This function will construct the command to feed to Sarge and provide Multisarge metadata about the process
# This probably needs to be defined top-level for the Pool of processes to be able to access it.
def cowsay_cmd(message, cowfile) -> ProcessTask:
    if not cowfile:
        cowfile='default'
    cmd = str.format('cowsay -f {file} {msg}', file=cowfile, msg=message)
    return ProcessTask(name=cowfile + '-saymoo',
                       command=cmd,
                       log_dir='cowsayrun_'+str(TIMESTAMP))


if __name__ == '__main__':
    run_process(
        # These are the required
        command_gen=cowsay_cmd,
        param_matrix=PARAM_MATRIX,
        # If true, will sleep to simulate long process times
        debug=False,
        # number of workers that the task pool will use
        num_processes=4,
    )
