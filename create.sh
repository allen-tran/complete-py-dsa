#!/bin/sh
cd leetcode/
read -p "Enter folder name: " foldername
mkdir "$foldername"
cd "$foldername"
read -p "Enter file name: " filename
cd ../../
cp example_readme.md ./leetcode/${foldername}
cp example_leetcode.py ./leetcode/${foldername}
cd ./leetcode/${foldername}
mv example_readme.md README.md
mv example_leetcode.py ${filename}.py