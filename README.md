# Orientation sensor csv to blender
Transfer smartphone orientation csv data to blender object

This blender script allows you to import **orientation sensor data** recorded in any **sensor logging app** (preferably [Sensor Logger](https://play.google.com/store/apps/details?id=com.kelvin.sensorapp&hl=en_IN) for android) **with the ability to export data in csv format.**

![camera in blender rotating](https://github.com/sensei1307/orientation-sensor-csv-to-blender/blob/main/ezgif-4-732b713947.gif?raw=true)

## Requirements:
 1. Blender, with PANDAS and COPY libraries installed.
 2. Any sort of csv orientation sensor logging app with the following columns:
	 a) time elapsed
	 b) W quaternion value
	c) X quaternion value
	d) Y quaternion value
	e) Z quaternion value

## Steps:
 - [ ] Record and export **orientation csv file**
 - [ ] Open blender and paste in the script in the scripting tab
 - [ ] Paste orientation **csv file path in the script** (instructed)
 - [ ] Open the csv file in a spreadsheet app and note down column positions for above mentioned required columns **(zero-indexing to be accounted for)**
 - [ ] Paste column positions in the script (instructed)
 - [ ] **SELECT** *the object you want to transfer rotation data to*
 - [ ] Run the script
 - [ ] Tweak/Clean/Smooth keyframes as per your requirements!
