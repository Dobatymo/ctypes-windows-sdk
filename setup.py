from setuptools import setup

setup(
	name = 'python-windows-sdk',
	version = '0.14',
	description = 'Ctypes port of Windows SDK',
	packages = ["win32sdk"],
	python_requires = ">=2.7",
	use_2to3 = False,
)
