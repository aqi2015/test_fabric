# coding:utf8

from fabric.api import (
	run, env, roles, hosts, cd,
	local, put
)


env.roledefs = {
	'test': [
		'127.0.0.1',
		'127.0.0.1',
	],
}



@roles('test')
def host_type():
	run('uname -s')


def remote_run(command):
	run(command)


def ls_tmp():
	run('cd /root')
	run('pwd')
	run('ls')

	with cd('/tmp'):
		run('pwd')
		run('ls')
		
