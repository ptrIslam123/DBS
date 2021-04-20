#! /bin/bash

cd ../../config/tables/
RES=$(cat init.txt | grep Камера.*снята.*с.*охраны.* | wc -l)

echo "Количество снятых с охраны камер: "
echo $RES
echo ""