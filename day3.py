#slicing
#you can use either the indexing operator or the slice function
#[start:stop:step]....the starting index is inclusive while the stopping index is exclusive

name = "Samuel Mwaura"

first_name = name[0:6] #you can use [:6]
last_name = name[7:13] #you can use [7:]
nick_name = name[0:13:3] #you can use [::3]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(nick_name)
print(reversed_name)

#the slice function

website = "https://youtube.com"
slice = slice(8,-4)
print(website[slice])