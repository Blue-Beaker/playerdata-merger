#! /bin/python3

#playerdata-merger by Blue_Beaker
#A tool for minecraft to merge playerdata to the level.dat for playing in singleplayer.
import os, shutil
#import sys
try:
    import nbtlib
except ImportError as ex:
    print(ex)
    print('nbtlib not found, is it installed properly?')
#os.chdir(sys.path[0])
levelfile='level.dat'
try:
    level=nbtlib.load(levelfile)
except FileNotFoundError as ex:
    print(ex)
    print('level.dat not found, Execute this script in your save folder!')
playerdatas=os.listdir('playerdata')
for i in range(0,len(playerdatas)):     #asks the user to select which file to be merged
    print(f'{i}: {playerdatas[i]}')
playerfile=playerdatas[int(input("Select the player file you want to merge:"))]
player=nbtlib.load(os.path.join('playerdata',playerfile))
level['Data']['Player']=nbtlib.tag.Compound(player) #Merge playerdata to level.dat/Data/Player
#with open('nbtmerge.log','w') as dump:     #dumps NBT data to a file for debug 
#    dump.write(str(level['Data']))
shutil.copy(levelfile,'level.dat.bak')      #Backups original file
level.save()
