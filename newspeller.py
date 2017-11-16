tempf = open('temp/rarecases_wrco.txt', "w")



def removegreekshit(word): 

	rword = []
	index = 0
	for i in range(1, len(word1), 2):
	wordfixed[index] = word[i] 
		
return rword

def converttogreek(word) : 

	gword = []
	index = 0
	for i in range(1, len(word), 1):
	gword[i] = '\xce' + word[i] 
		
return gword 



def FindMissingChars(word1,word2,diffs):

	for char1,char2 in zip(word1,word2): 
		
		if char1 == char2 : 
			continue 
		else: 
			
return missing 

#αληθεια
#αλληθεια

#παραδωσετε
#παραδωσεται 

def ExtraChars(word1,word2,diffs):
	greekshit = '\xce'
	if diffs == 1 : 
		ind = 0 
		i = 0 
		for char1,char2 in zip(word1,word2): 
			
			if char1 == char2 : 
				continue 
				ind = ind +  1
			else: 
				wi = ind 	# double chars  ex: ΛΛ -> Λ 
				if (word2[ind] == word1[ind-1] and word2[ind-1] == word2[ind] 
			      		a = greekshit + word2[ind] + greekshit + word2[ind]  				   					        b = greekshit + word2[ind] 
					extras = [ a , b ]
				else:
						# shit error ex: ΑΙ -> Ε 
					if ( word1[ind] == '\x95' and word2[ind] == '\x91' and word2[ind+1] == '\x99'):
						a = greekshit + word2[ind] + greekshit +  word2[ind+1] 
						b = greekshit +  word1[ind] == '\x95'
						extras = [ a , b ] 
					else: 
						
		  
	else: 
		print("Rare Case..") 
		gword1 = converttogreek(word1) 
		gword2 = converttogreek(word2)	
		tempf.write(gword1 + '\n')
		tempf.write(gword2 + '\n') 
		
return extras 



				
d# ef Levenstein( word1 , word2 ): 

	





#return differences 


#This function returns a list with tuples (item1,item2,flag) where item1 and item2 constitute the rule and flag is a bollean value.
# flag = 0 is a substitute | flag = 1 is a rearrangement 
def ExamineSubsRearrs( word1, word2, diffs): 

	faults = [[]] 
	i = 0 			# the index for accessing the array 
	if diffs == 1 : 
		# This diff is sure a sub 
		for char1,char2 in zip(word1,word2) : 
			if char1 == char2 : 
				continue 
			else: 
				# The substitution is found !
				faults[i] = [ char2, char1, 0 ]
				i = i + 1  
	if diffs == 2 : 
		# This diff can be either two subs or a rearr 
		# rearr is when chars substituted are same and consecutive
		firsttime = 1
		ind = 0  		 
 		for char1,char2 in zip(word1,word2):
 
			if char1 == char2 : 
				continue 
			else: 
				if firsttime == 1 : 
					wi = ind
					firsttime = 0  				
				else: 
					if (ind - 1) == wi :
						# consecutive -> swap  
					  	faults[i] = [ char2, char1, 1]       
						i = i + 1 
					else : 
						faults[i] = [ word2[wi], word1[wi], 0]  
						i = i + 1
						faults[i] = [ word2[ind],word1[ind], 0]
	else: 		
		 
		firsttime = 1
		ind = 0			
		for char1,char2 in zip(word1,word2):  	
				
			if char1 == char2 : 
				continue 
			else:  		
				if firsttime == 1:
					wi = ind 
					firsttime = 0
				else: 
					if (ind - 1) == wi 
						#consecutive -> swap 
						faults[i] = [ char2, char1, 1] 
						i = i + 1
						firsttime = 1 

					else: 
						faults[i] = [ word2[wi], word1[wi], 0]  
						i = i + 1
						faults[i] = [ word2[ind], word1[ind], 0]  										
	return faults 


def main():

 import os
 import shutil
 import math
 import difflib

f1 = open("slp_spell_data/trial_co.txt", "r")  
f2 = open("slp_spell_data/trial_wr.txt", "r")
tempfile = open('temp/outputfile_wrco.txt', "w") # temp file to write the wrong-correct rules 


greekshit = '\xce'

subs = 0
rearr = 0
delt = 0 
extra = 0  
total = 0 

for line1, line2 in zip(f1, f2):
        s1 = line1.split()
        s2 = line2.split()

        for curword1, curword2 in zip(s1, s2):  

	word1 = removegreekshit(curword1)
	word2 = removegreekshit(curword2) 
	
	if word1 in word2 : 
		continue 
	else 
		# here words have differences. Let's find them out !


		differences = Levenstein(word1,word2) 
		
		condition = len(curword1) - len(curword2) 
		
		if condition == 0  
			# Equal length
			 
			faults_list = ExamineSubsRearrs(word1,word2,differences)
			
			# Retrieve Info faults_list			
			for l = 1 in len(faults_list):
				tmp = faults_list[l]
				if tmp[2] == 1 : 
					rearr = rearr + 1
					a = "rearr" + greekshit + str(tmp[0]) + ' ' + greekshit  + str(tmp[1]) +  '\n'
				else: 
					subs = subs + 1
		 			a = "subs" + greekshit + str(tmp[0]) + ' ' + greekshit + str(tmp[1]) +  '\n'
				
				tempfile.write(a) 
				

		elif condition > 0: 
			# curword2 missing letters 
			missing = [] 	
			missing = FindMissingChars(word1,word2) 		 
			
			for n = 0 in len(missing): 
				a = "miss" + "keno" + '\n' + greekshit + str(missing[n]) + '\n'  
				tempfile.write(a)
		else: 

			# curword2 has extra letters 
					
			print("geia") 
			extra = [] 
			extra = FindExtraChars(word1,word2,Differences) 
			
			for m = 0 in len(extra): 
				a = "extra" + greekshit + str(extra[n]) + ' ' + "keno" + '\n' 
				tempfile.write(a) 				
				





		
main () 	



