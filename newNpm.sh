dir=$(pwd)
mkdir $1
cd $1
cp -a ${dir}/assets/newNpm/. ./
npm init -y
npm i --save-dev babel-preset-env babel-plugin-transform-object-rest-spread cross-env eslint eslint-config-google nodemon babel-eslint
git init
