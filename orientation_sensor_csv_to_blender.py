import bpy
import pandas as pd

#-----------------------------------

#! Rotation sensor data
#! Enter the CSV file path of logged orientation data from your smartphone
#! CSV is converted to a pandas dataframe object
rot_df = pd.read_csv("PATH HERE")

#-----------------------------------

#! OPEN YOUR CSV FILE IN A SPREADSHEET PROGRAM AND CHECK COLUMN POSITIONS !
#! CHECK FOR REQUIRED DATA COLUMNS:
#! 1) time elapsed
#! 2) W quaternion value
#! 3) X quaternion value
#! 4) Y quaternion value
#! 5) Z quaternion value

time_elapsed_col_pos = 1
quaternion_w_col_pos = 5
quaternion_x_col_pos = 4
quaternion_y_col_pos = 3
quaternion_z_col_pos = 2

#-----------------------------------

# Orientation sensor data is usually recorded as quaternions
#! Change as per requirement

ob = bpy.context.active_object
ob.rotation_mode = "QUATERNION"

#-----------------------------------

# Below code can be ignored
#! Run the script

frame_rate = bpy.context.scene.render.fps 

for i in range(1,rot_df.shape[0] ):
    
    ob.rotation_quaternion = ( rot_df.iloc[i,quaternion_w_col_pos] , rot_df.iloc[i,quaternion_x_col_pos] , rot_df.iloc[i,quaternion_y_col_pos] , rot_df.iloc[i,quaternion_z_col_pos] )
    
    frame_gap1 = rot_df.iloc[i,time_elapsed_col_pos] * frame_rate
    
    ob.keyframe_insert(data_path="rotation_quaternion", frame = frame_gap1 )