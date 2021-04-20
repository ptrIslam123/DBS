#! /bin/bash

cd ../../config/tables/
RES=$(cat init.txt | grep Камера.*поставлена.*на.*охрану.* | wc -l)

echo "Количесвто поставленных на охрану камер: "
echo $RES
echo ""




