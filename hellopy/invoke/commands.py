
import os
import re
from invoke import Collection, call, task, Context

@task
def run_jserv(c):
    cd = '../../../semantic-jserv/jserv-album/bin'
    if os.name == 'nt':
        cd = re.sub('/', '\\\\', cd)
    ret = c.run(f'cd {cd} && java -jar bin/jserv-album-0.7.1.jar')
    print(ret.ok)


if __name__ == '__main__':
    # Create a collection of tasks
    ns = Collection()
    ns.add_task(run_jserv)
    ctx = Context()

    # Call a task programmatically
    ns["run_jserv"](ctx)
