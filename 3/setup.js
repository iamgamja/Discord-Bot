const {execSync} = require('child_process');

execSync('python -m ensurepip --default-pip');
execSync('pip install -r requriements.txt');
