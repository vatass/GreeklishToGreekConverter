

def removegreekshit( word) : 

	wordfixed = []
	index = 0
	for i in range(1, len(word1), 2):
		wordfixed[index] = word[i] 
			

def main():

 import os
 import shutil
 import math
 import difflib

f1 = open("slp_spell_data/trial_co.txt", "r")  
f2 = open("slp_spell_data/trial_wr.txt", "r")
#tempfile = open('temp/outputfile_wrco.txt', "w") # temp file to write the wrong-correct rules 


greekshit = '\xce'

subs = 0
rearr = 0 
total = 0 

for line1, line2 in zip(f1, f2):
        s1 = line1.split()
        s2 = line2.split()

        for curword1, curword2 in zip(s1, s2):  
		cwr = 0 # number of errors per word
		norearr = 0
		len_a = len(curword1) 
		len_b = len(curword2) 
		print("Correct :" + str(curword1)) 
		print("Wrong :" + str(curword2))	 



		condition = len_a - len_b 
# curword1 is the right word 
# curword2 is the wrong one 
# So, char1 is the right and char2 is the wrong 

#We suppose one error at a time 
		errorchars = [0,0] 
		 
		if condition == 0 : # substitution | rearrangement  
			i = -1 # index of words
			flag = 0  
			print("Initial Number of Errors" + str(cwr)+ '\n')
			print("Equal Length\n") 
			for char1,char2 in zip(curword1,curword2):
				i = i + 1 
				if( char1 <> char2 ):

					if flag == 0 :
						wfi = i	
						print( "Diffent Character Spotted for 1st time..\n")  
						errorchars[cwr] = char2   # store the wrong char 
						print(cwr) 
						errorchars[cwr+1] = char1 # store the right char 						
						cwr = cwr + 1 
						subs = subs + 1
						norearr = 1
						flag = 1
					else:
						
						print( "Different Character Spotted for 2nd time..\n")
						print("The index of the 1st is : " + str(wfi)+ '\n')
						print("The index of this is :" + str(i)+ '\n')
						if (i - 2) == wfi  :   
 							print( "Rearragement Error Found...\n")
							rearr = rearr + 1
							subs = subs - 1
							norearr  = 0
							print( '\n'+"Rule: "+greekshit + str(char2)+ ' '+"<->" +greekshit + str(char1))		
						else : 
							cwr = cwr + 1
							subs = subs + 1	
							norearr = 1 
							print("Substitution Found...")
				 			print( '\n'+ "Rule: " + greekshit  + str(char2) + ' ' + greekshit + str(char1) )
								 
							
				else : 

					continue 		       		  
				
			if( norearr == 1 ):
				print("Substitution Found") 
				print( '\n'+ "Rule: " + greekshit  + str(errorchars[0]) + ' ' + greekshit + str(errorchars[1]) ) 	
			
		
		else :
			if ( condition > 0 ) : #  only one  deleted char, dummy  
				
				# first we have to see which character is mising 
				missing_char = "Α" # by default 
				for char1 in curword1 : 
					if char1 in curword2 : 
						continue 
					else
						missing_char = char1 

			        print( "Missing Character Error Found...") 
				print ("Rule: " + "keno " + greekshit + str(missing_char)    
										
				
			         
				print("geia") 










			else: 

			   	# first we have to see which character is added  
				added_char = "Α" # by default 
				for char2 in curword2 : 
					if char2 in curword1 : 
						continue 
					else
						added_char = char2

			        print( "Additional Character Error Found...") 
				print ("Rule: " +  greekshit + str(missing_char)+ " keno " )      
				

				print("geia")



		total = total + cwr
	
print( " Total Subs Found: " + str(subs) + '\n') 
print ( "Total Rearr Found: " + str(rearr) + '\n') 
print( "Total Errors Found: " + str(total) + '\n') 

f1.close()
f2.close()
				 
main () 





