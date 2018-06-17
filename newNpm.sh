dir=$(pwd)
mkdir $1
cd $1
cp -a ${dir}/assets/newNpm/. ./
npm init -y
npm i --save-dev eslint eslint-config-google nodemon babel-eslint
git init