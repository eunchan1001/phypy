#!/bin/bash

git add .
git commit -m 'update'
git push

rm -rf dist build mphyspy.egg-info
python setup.py bdist_wheel
python -m twine upload dist/*