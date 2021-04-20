#~ /bin/bash

cd ../../config/tables/
RES=$(cat small_init.txt | grep Камера.*Ложная.*тревога.* | wc -l)

echo "Количесвто ложных тревог: "
echo $RES
echo ""