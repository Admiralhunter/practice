from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install
import subprocess

class LicenseCheckCommand(develop):
    description = 'Check licenses of installed packages'
    user_options = install.user_options + []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # Run licensecheck
        subprocess.check_call(['licensecheck', '-r'])

setup(
    # Other setup options...
    install_requires=[
        # Other dependencies...
        'licensecheck'
    ],
    cmdclass={
        'licensecheck': LicenseCheckCommand,
    }
)