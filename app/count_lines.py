import os
lines = 0
dirname = '.'
def search(dirname):
	try:
		filenames = os.listdir(dirname)
		for filename in filenames:
			full_filename = os.path.join(dirname, filename)
			if os.path.isdir(full_filename):
				search(full_filename)
			else:
				ext = os.path.splitext(full_filename)[-1]
				if ext == '.css' or ext =='.xml' or ext=='.js': 
					#print(full_filename)
					with open(full_filename) as f:
						for i, l in enumerate(f):
							pass
						print(i + 1)
	except Exception as e:
		print(e)

search('.')
#num_lines = sum(1 for line in open('myfile.txt'))
