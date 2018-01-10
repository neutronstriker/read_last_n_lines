# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 23:22:35 2017

@author: Srinivas N
"""

filename  = "datalog.txt"

def listLastNlIndex(f,line_count=5):
    count = 0    
    listofIndexrev = []    
    f.seek(0,2)
    
    #EOF position condition, Check if end of file char is a '\n'
    if f.read(1) == '\n':                  
        listofIndexrev.append(f.tell())
        count = count+1

    try:    
        while count < line_count and f.tell() != 0:
            
            #set cursor one position back
            f.seek(-1,1)                  

            #read value at current position also increments cursor one position ahead.
            if  f.read(1) == '\n':
                #save the cursor value of one position back
                listofIndexrev.append(f.tell()-1)
                count = count+1
                f.seek(-1,1) #i found that whenever a '\n' is encountered cursor increments two points ahead
            
            #since cursor increments one position after read we will set it back one position
            f.seek(-1,1)
        
        listofIndexrev.reverse()
        return listofIndexrev
    #if f.tell() is 0 already and we do a  f.seek(-1,1) then it will result in an IOError,
    #however I could have handled the situation more decoratively by placing a if f.tell() != 0 just
    #before each and every f.seek(-1,1) but for now whatever works is enough.
    except IOError as e:
        print "IOError Exception "
        print str(e)
        listofIndexrev.reverse()        
        return listofIndexrev

'''

f = open(filename,'r')


#print listLastNlIndex(f,3)

f.seek(listLastNlIndex(f,10)[0]+1)

print f.readlines()


f.close()

'''
