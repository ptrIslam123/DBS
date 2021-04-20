#! /bin/bash

cd ../../config/tables/
RES=$(cat init.txt | grep Камера.*Подтвержденная.*тревога.* | wc -l)

echo "Количесвто подтвержденных тревог: "
echo $RES
echo ""