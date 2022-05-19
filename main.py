#First run this py file in vs code to see that it runs without any error, then start your homework.
#print("I can do all things")
'''
Instruction

Find your questions in the comment and write the code below each comment

After, code completion, 
push your code to the same github repo you cloned the assignment.
'''
#################################################################################
'''Question 1'''
#declare a variable called "sports" \
# whose value is a list that contains the element \
# "football","tennis","volleyball","long jump"
'''Your answer to Question 1 below'''
sports = ["football","tennis","volleyball","long jump"]
#print(sport)
'''Question 2'''
#extend the sports list with the more_sports list below \
# and save your new list in a variable called total_sports
more_sports = ["basket ball", "wrestling", "boxing"]
'''Your answer to Question 2 below'''
more_sports = ["basketball", "wrestling", "boxing"]
print(more_sports)
print(sports.extend(more_sports))
print(sports)
total_sports = [
    "football",
    "tennis",
    "volleyball",
    "long jump",
    "basketball",
    "wrestling",
    "boxing"
    ]
print(total_sports)
'''Question 3'''
#sort the elements in total_sports in descending order
'''Your answer to Question 3'''
total_sports.sort(reverse=True)
print(total_sports)
#
'''Question 4'''
#Delete the last element in total_sports and \
# save the new list to a variable called clean_sports, print clean_sports
'''Your answer to Question 4'''
clean_sports = [
    'football',
    'tennis',
    'volleyball',
    'long jump',
    'basketball',
    'wrestling',
    ]
print(clean_sports)
'''Question 5'''
#create a list called counts whose value consist of integers 2,3,6,4,5,7,8,0
#sort the counts list in decending order
#calculate the mean of counts using sum() and len() functions, \
# save the mean in a variable called mean and print the value
'''Your answer to Question 5'''
counts = [2,3,6,4,5,7,8,0]
counts.sort(reverse=True)
print(counts)
print(sum(counts))
print(len(counts))

'''Question 6'''
#create a dictionary called sports_dict with the elements in total_sports list as values\
#and the index of each element as keys
#print the key:value pair of sports_dict
'''Your answer to question 6'''
sports_dict = {
    "0":"football",
    "1":"tennis",
    "2":"volleyball",
    "3":"long jump",
    "4":"basketball",
    "5":"wrestling",
    "6":"boxing"
}
print(sports_dict)


#
'''Question 7'''
#Write the correct form of the code in the doc string below:
#The output of the print statement: The index number of 'boxing' in more_sports list is 2
'''
print(
    f'The index number of 'boxing' in more_sports list is {more_sports.index()}'
)

'''
