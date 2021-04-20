#! /bin/bash

cd ../../config/tables/
RES=$(cat init.txt | grep Камера.*Подозрительная.*ситуация.* | wc -l)

echo "Количесвто подозрительных ситуаций: "
echo $RES
echo ""