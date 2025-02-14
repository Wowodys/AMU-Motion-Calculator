Calculator for movement system of Automatic Manufacturing Unit.

Download just AMUcalc.exe

Used to fine-tune rotation values for AMU firmware stepper motors

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Rotation Distance Calc: To adjust step/mm travel of X and Y stepper motors

Belt Pitch:             Use your respective belt pitch (GT2 = 2, GT3=3, etc)

Number of Teeth:        Number of teeth on the pulley on the motor. (Standard= 16 or 20)

Rotation Distance:      The calculated Rotation Distance to adequately tune AMU to be dimensional accurate (ex: 1 inch of software requested travel = 1 inch of real travel

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
Lead-Screw Driven Axis Rotation Distance Calculation: To make sure that software commanded vertical travel of the printer head reflects actual vertical distance supplied by motor. 

Screw Pitch (mm): From your lead screw. Most are double threaded standard 8mm leadscrews, as used on the ender 3





----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

              !!!!!!!!!!!!!!!!MAKE SURE EXTRUDER IS CLEAR TO PROCEED.!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                               
1. NOTE DOWN THE ROTATION DISTANCE CURRENTLY IN FIRMWARE
2. TELL EXTRUDER TO MOVE 100mm OF MATERIAL
3. CUT OFF EXTRUDED MATERIAL, AND MEASURE WITH CALIPERS TO MAKE SURE 100mm OF REQUESTED MATERIAL = 100mm OF EXTRUDED MATERIAL
4. IF OFF BY MORE THEN (0.5% - 1%), NOTE DOWN THE DISTANCE OF EXTRUDED MATERIAL
5. USE CALCULATOR TO CORRECT ROTATION DISTANCE, AND INPUT INTO FIRMWARE


Extruder Rotation Distance Calc:   To adjust step/mm travel of extruder stepper motors for adequate deposition of material

Previous Rotation Distance:        Use the previous value used in the firmware before calibration 

Actual Extrude Distance:           Real measured amount of material extruded (measured with calipers)

Requested Extrude Distance:        Requested amount of material to extrude (The input request)

Extruder Rotation Distance:        The Calculated Extruder Rotation Distance to put into firmware, which should calibrate extruder to deposit correct distance of requested material. 

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


