#! /bin/bash

cd ../../config/tables/
RES=$(cat init.txt | grep Камера.*Тревога.*не.*взята.*в.*обработку.* | wc -l)

echo "Количесвто не взятых в обработку тревожных ситуаций: "
echo $RES
echo ""