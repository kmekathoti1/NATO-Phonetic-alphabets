student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    # print(key,value)
    #Access key and value
    pass



import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # print(row.score)
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
# print({row.student:row.score for (index,row) in student_data_frame.iterrows()})

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
alphabets_df=pandas.read_csv("nato_phonetic_alphabet.csv")
print(alphabets_df)
alphabets_dict={row.letter:row.code for (index,row) in alphabets_df.iterrows()}




#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_output=[]
user_input=input("Enter the word: ").upper()
[user_output.append(alphabets_dict[letter]) for letter in user_input if letter in alphabets_dict] #list comprehension
# for letter in user_input:
#     if letter in alphabets_dict:
#         user_output.append(alphabets_dict[letter])
print(user_output)





