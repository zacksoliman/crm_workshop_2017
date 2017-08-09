import os

os.makedirs(os.path.join(os.path.expandusers('~'), 'part', 'merged_corpus'))

path1 = os.join(os.path.expanduser('~'), 'part', 'corpus')
path2 = None # Put second path here


dir_list1 = os.path.listdir(path1)
dir_list2 = os.path.listdir(path2)


