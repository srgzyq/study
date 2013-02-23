#!/bin/bash

server=$1

#cat ./ares.server.log | grep  'Zhenqi.refresh' | grep -v "Waiting"

cat ./ares.server.log | grep  $1 | grep -v "Waiting"

