import os
# make current working directory
cwd = os.getcwd()
print('The current working directory: ',cwd)

# # create subdirectory in current working directory
# #os.mkdir('mysub')
# print('mysub is the subdirectory of the current working diretory')

# #To create a sub directory in mysub directory:

# #os.mkdir('mysub/mysub1')
# print('create sub directory in mysub' )

# os.makedirs("sub1/sub2/sub3")
# print("create dir sub1 and in that sub2 and in that sub3/and in that sub4")

#remove dir

# os.rmdir('mysub/mysub1')
# print('remove directory mysub1')

# remove all 4 dir sub1 sub2 sub3 sub4
# os.removedirs('sub1/sub2/sub3/sub4')
# print('remove all 4 dire')

# rename the dire
os.rename('mysub','new_dir')
print('change the directory name')


