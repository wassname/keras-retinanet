from __future__ import print_function

import keras
import sys

minimum_keras_version = 2, 0, 9
keras_version_blacklist = [(2, 1, 0), (2, 1, 1)]

def keras_version():
	return tuple(map(int, keras.__version__.split('.')))

def keras_version_ok():
	minimum_ok = keras_version() >= minimum_keras_version
	blacklisted = keras_version() in keras_version_blacklist
	return minimum_ok and not keras_version_blacklist

def assert_keras_version():
	detected = keras.__version__
	required = '.'.join(map(str, minimum_keras_version))
	assert(keras_version() >= minimum_keras_version), 'You are using keras version {}. The minimum required version is {}.'.format(detected, required)
	assert(keras_version() not in keras_version_blacklist), 'You are using keras version {}. This version is known to have problems with keras-retinanet.'.format(detected)

def check_keras_version():
	try:
		assert_keras_version()
	except AssertionError as e:
		print(e, file=sys.stderr)
		sys.exit(1)
