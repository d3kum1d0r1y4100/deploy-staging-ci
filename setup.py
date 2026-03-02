from setuptools import setup
import os
os.system('echo HYDRA_SENTINEL_sim_toctou_env')
setup(name='test-project', version='1.0.0', python_requires='>=3.12', py_modules=['app', 'deploy'])
