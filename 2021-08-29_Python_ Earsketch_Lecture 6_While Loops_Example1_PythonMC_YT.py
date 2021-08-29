#For Loops in EarSketch-  Jan 16, 2019_WHILE LOOPS
#		python code
#		script_name:While Loops-Example 1_earSketch
#
#		author: Ernie Yijie
#		description:While Loops- Example 1_Basic Build-up
#


#WHILE LOOPS in EarSketch- Jan 16, 2019_video timelapse 5:05 

from earsketch import *
init()
setTempo(120)

#--------------------------------------------------------
EDM_Beats = [HOUSE_DEEP_SINELEAD_002,RD_UK_HOUSE_MAINBEAT_4,RD_UK_HOUSE_MAINBEAT_6,RD_UK_HOUSE__ACIDLINE_2,RD_UK_HOUSE__FMBASS_2,Y34_SNARE_1,
Y39_BASS_1,Y39_PERCUSSION_2,Y55_PERCUSSION_3,HOUSE_SFX_WHOOSH_007,
RD_UK_HOUSE__SFX_LEADPULSAR_1,RD_UK_HOUSE__SFX_LFOGARBLES_1]
#---------------------------------------------------------


#---------------------------While Loop-------------------------------
track = 1
start = 5
counter = 1


while counter <= 9:
    insertMedia(RD_UK_HOUSE__SFX_WIREUP_1,track,start)
    start+=7
    counter+=1
#---------------------------------------------------------------------
track = 2
start =1
end = 16
beats =EDM_Beats

#----------------------------------------

for beat in beats:
    # fitMedia is like insertMedia
    #except it allows you to change the length of the track
    # it has another parameter,end,which specifies where
    # the track will stop
    fitMedia(beat, track,start,end)
    start+=3
    end+=5
    track+=1


print("you there matey!")  # optional

finish()
