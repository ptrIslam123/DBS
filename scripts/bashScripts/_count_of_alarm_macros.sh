#! /bin/bash

cd ../../config/tables/
RES=$(cat init.txt | grep Камера.*Тревога.*инициирована.*макрокомандой.* | wc -l)

echo "Количесвто инициированных тревог макрокомандой: "
echo $RES
echo ""