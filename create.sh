#!/bin/sh
cd leetcode/
read -p "Enter folder name: " foldername
mkdir "$foldername"
cd "$foldername"
read -p "Enter file name: " filename
touch "${filename}.py"
touch "${filename}_test.py"
cd ../../
cp example_readme.md ./leetcode/${foldername}
cp example_test.py ./leetcode/${foldername}
cd ./leetcode/${foldername}
mv example_readme.md README.md
mv example_test.py "${filename}_test.py"