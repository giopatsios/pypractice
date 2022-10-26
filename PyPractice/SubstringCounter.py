# %%
# There is a collection of input strings and a collection of query strings. 
# For each query string, determine how many times it occurs in the list of input strings. 
# Return an array of the results.

strings= ['abcde','sdaklfj','asdjf','na','basdn','sdaklfj','asdjf','na','asdjf','na','basdn','sdaklfj','asdjf']
queries = ['abcde','sdaklfj','asdjf','na','basdn']


for i in range(len(queries)):
    print(strings.count(queries[i]))



# %%



