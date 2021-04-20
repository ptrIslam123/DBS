#! /bin/bash

cd ../../config/tables/
RES=$(cat init.txt | grep Камера.*Пропущенная.*тревога.* | wc -l)

echo "Количесвто пропущенных тревог диспетчером: "
echo $RES
echo ""