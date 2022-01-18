import os
from distutils.command.install import install

import pip
from setuptools import setup


class CustomInstall(install):
    """Custom handler for the 'install' command."""

    def run(self):
        # uninstall lingua_franca
        # the whole purpose of this package is to replace it
        pip.main(["uninstall", "lingua_franca", "-y"])
        super().run()


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


def required(requirements_file):
    """ Read requirements file and remove comments and empty lines. """
    with open(os.path.join(os.path.dirname(__file__), requirements_file),
              'r') as f:
        requirements = f.read().splitlines()
        return [pkg for pkg in requirements
                if pkg.strip() and not pkg.startswith("#")]


extra_files = package_files('lingua_franca')

with open("readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ovos-lingua-franca',
    version='0.4.3a1',
    packages=['lingua_franca', 'lingua_franca.lang'],
    cmdclass={'install': CustomInstall},
    url='https://github.com/OpenVoiceOS/lingua_plus',
    license='Apache2.0',
    package_data={'': extra_files},
    include_package_data=True,
    install_requires=required('requirements.txt'),
    author='Mycroft AI / OVOS',
    author_email='jarbasai@mailfence.com',
    description='OpenVoiceOS\'s multilingual text parsing and formatting library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
