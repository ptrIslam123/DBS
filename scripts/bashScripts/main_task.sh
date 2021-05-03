#! /bin/bash


echo "### MAIN_TASK ###"
echo ""

cd ../scripts/bashScripts/

bash ./_count_cameras_of_put_on_guard.sh
bash ./_count_cameras_of_unguarded.sh
bash ./_count_cameras_of_unguared.sh
bash ./_count_of_alarm_macros.sh
bash ./_count_of_cameras_set_up_for_protection.sh
bash ./_count_of_confirming_alarms.sh
bash ./_count_of_detector_reset.sh
bash ./_count_of_detector_triggers.sh
bash ./_count_of_end_of_detection_triggers.sh
bash ./_count_of_false_alarm.sh
bash ./_count_of_missed_alarms.sh
bash ./_count_of_processed_alarms.sh
bash ./_count_of_suspicious_situation.sh
bash ./_count_of_undetected_alarms.sh
bash ./_count_of_unprocessed_alarms.sh


echo "### MAIN_TASK_END ###"
echo ""
echo ""



