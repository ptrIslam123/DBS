#! /bin/bash

cd ../../config/tables/
RES=$(cat init.txt | grep Камера.*Окончание.*периода.*срабатывания.*детектора.* | wc -l)

echo "Количесвто окончаний периодов сбрасывания детекторов: "
echo $RES
echo ""