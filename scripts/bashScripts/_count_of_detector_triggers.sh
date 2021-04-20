#! /bin/bash

cd ../../config/tables/
RES=$(cat init.txt | grep Камера.*Начало.*периода.*срабатывания.*детектора.* | wc -l)

echo "Количесвто начала периодов сбрасывания детекторов: "
echo $RES
echo ""