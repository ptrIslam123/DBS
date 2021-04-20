#! /bin/bash

cd ../../config/tables/
RES=$(cat init.txt | grep Камера.*Тревога.*обрабатывается.* | wc -l)

echo "Количесвто обрабатываемых тревог: "
echo $RES
echo ""