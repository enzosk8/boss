from fabric.api import run, hide, local


def fetch(prune=True):
    ''' The git fetch command. '''
    run('git fetch' + (' --prune' if prune else ''))


def checkout(branch, force=False):
    ''' The git checkout command. '''
    force_flag = '-f ' if force else ''
    run('git checkout {0}{1}'.format(force_flag, branch))


def pull(branch):
    ''' The git pull command. '''
    run('git pull origin %s' % branch)
    # TODO: Custom origin


def sync(branch):
    ''' Sync the current HEAD with the remote(origin)'s branch '''
    run('git reset --hard origin/%s' % branch)
    # TODO: Custom origin


def last_commit(remote=True, short=False):
    '''
    Get the last commit of the git repository.

    Note: This assumes the current working directory (on remote or local host)
    to be a git repository. So, make sure current directory is set before using this.
    '''

    cmd = 'git rev-parse{}HEAD'.format(' --short ' if short else ' ')

    with hide('everything'):
        result = run(cmd) if remote else local(cmd, capture=True)

        return result.strip()


def current_branch(remote=True):
    '''
    Get the current branch of the git repository.

    Note: This assumes the current working directory (on remote or local host)
    to be a git repository. So, make sure current directory is set before using this.
    '''

    cmd = 'git rev-parse --abbrev-ref HEAD'

    with hide('everything'):
        result = run(cmd) if remote else local(cmd, capture=True)

        return result.strip()


def show_last_commit():
    ''' Display the last commit. '''
    run('git log -1')
