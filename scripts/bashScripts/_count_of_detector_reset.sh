#! /bin/bash

cd ../../config/tables/
RES=$(cat init.txt | grep Камера.*Срабатывание.*детектора.*номер.* | wc -l)

echo "Количесвто сбрасываний детектора: "
echo $RES
echo ""