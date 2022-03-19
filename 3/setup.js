const {execSync} = require('child_process');

execSync('py -m ensurepip --default-pip');
execSync('pip install -r requriements.txt');
