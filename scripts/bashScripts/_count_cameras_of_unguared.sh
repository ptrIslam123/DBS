#! /bin/bash

# количество камер сеятых с охраны камер
cd ../../config/tables/
RES=$(cat init.txt | grep Камера.*снята.*с.*охраны.* | wc -l)

echo "Количесвто снятых с охраны камер: "
echo $RES
echo ""
