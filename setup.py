from setuptools import setup

setup(
	name = 'ctypes-windows-sdk',
	version = '0.14',
	description = 'Ctypes port of Windows SDK',
	packages = ["cwinsdk", "cwinsdk/km", "cwinsdk/km/crt", "cwinsdk/shared", "cwinsdk/um"],
	python_requires = ">=2.7",
	use_2to3 = False,
)
