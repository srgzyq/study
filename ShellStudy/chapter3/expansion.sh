#!/bin/bash

email="@gmail.com"

echo "brace expansion"
echo sp{el,il,al}l
echo sp{el,il," al"}l

echo 
echo "variable exapsion"
name="srgzyq"
echo ${name}$${email}
echo $name${email}

name="srgzyq"
firstname=name
echo ${!firstname}${email}

firstname="srgzyq"
echo ${firstname:=ji}${email}
echo ${cname:=jia}${email}


echo
val=3
echo
echo $(($1+val+2+`date +%m`)) 

echo $(date)
echo `date`
