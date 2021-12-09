
def solution(S):
    # write your code in Python 3.6
    S = S.strip() 
    list_sent = list() # list of individual sentences
    i_list_sent = 0 # counter to parse list of individual sentences
    total_sentence = 0 # total sentence found 
    total_word = 0 # counts words for each individual sentence and reset everytime with a new sentence 
    last_sent_position = 0 # pointer to identify from where to start parsing the next sentence 
    length = len(S)
    i = 0
    while(i<length): 
    	c = S[i]
    	if(i+1 == length and c!='.' and c!='?' and c!='!'): 
    		total_sentence+=1
    		total_word+=1
    		list_sent.append(S[last_sent_position:i+1])
    	
    	elif(c=='.' or c=='?' or c=='!'): 
    		list_sent.append(S[last_sent_position:i+1])
    		total_sentence+=1 
    		last_sent_position = i+1
    		
    		if(last_sent_position != len(S)):
	    		while(S[last_sent_position] == " "): 
	    			last_sent_position+=1
    		
    		total_word = 0

    	elif(c==" "): 
    		total_word+=1

    	i+=1

    # find largest sentence. parse each sentence from list_sent
    max_word = 0
    largest_sen_position = 0
    sen_position = 0 
    for sen in list_sent: 
    	i = 0 
    	word_count = 0
    	while(i<len(sen)):
    		if(sen[i] == " " or i+1==len(sen)): 
    			word_count+=1

    		i+=1

    	if(word_count>max_word): 
    		max_word = word_count
    		largest_sen_position = sen_position

    	sen_position+=1


