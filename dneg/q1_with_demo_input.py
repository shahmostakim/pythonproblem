
def solution(S):
    # write your code in Python 3.6
    # print(len(s))
    S = S.strip() 
    #print("text after strip() = {}".format(S))
    list_sent = list()
    i_list_sent = 0
    total_sentence = 0
    total_word = 0
    last_sent_position = 0
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



    # program output  
    print("total {} sentence(s)".format(total_sentence))
    # print the sentences list 
    print("list of sentences: ")
    for sent in list_sent: 
    	print(sent)

    final_lar_sent = list_sent[largest_sen_position]
    print("largest sentence = {}".format(final_lar_sent))


# test 
# python3 q1.py
s = "Hi there! Come here asap. How are you today?"
solution(s)

