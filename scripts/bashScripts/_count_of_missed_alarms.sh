#! /bin/bash

cd ../../config/tables/
RES=$(cat small_init.txt | grep Камера.*Пропущенная.*тревога.* | wc -l)

echo "Количесвто пропущенных тревог: "
echo $RES
echo ""