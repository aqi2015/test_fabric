# coding:utf8

from fabric.api import (
	run, env, roles, hosts, cd,
	local, put
)


env.roledefs = {
	'test': [
		'root@127.0.0.1',
		'root@127.0.0.1',
	],
}



def host_type():
	run('uname -s')


@roles('test')
def remote_run():
	run('pip list | grep ipython || pip install ipython')


def ls_tmp():
	run('cd /root')
	run('pwd')
	run('ls')

	with cd('/tmp'):
		run('pwd')
		run('ls')
		
