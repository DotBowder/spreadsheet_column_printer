# This application was designed for a user who needed to take columns from a spreadsheet, organize the data,
# and then print the line's formatted data to the screen. It was designed to do this line by line.
# Every row is a chunk of data, and we're printing the specified data to the screen.


# syntax: python3 run.py [spreadsheet filename]


import sys

sepparator = '\t' # If you use a csv, or other delimited text, you can adjust the delimiter here

# Here we open our tab sepparated value file and split it up by every line. We dump all those lines into the 'l' variable.
f = open(sys.argv[1],'r')
l = f.read()
l = l.split('\n')
f.close()


line_0 = l[0].split(sepparator)





print('///////////////////////////////////////////////////////')
print('///////////////////// Options /////////////////////////')
print('///////////////////////////////////////////////////////')
print()

# We've taken the very first line of our spreadsheet, and printed each chunk inside of the line to the screen.
# We've done this so that the user can see a list of options to choose from.
c=0
for entry in line_0:
    print('{} :\t{}'.format(c, entry))
    c+=1





print()
print()
print('///////////////////////////////////////////////////////')
print('/////////////////////// Input /////////////////////////')
print('///////////////////////////////////////////////////////')
print()
print('I\'m going to need you to tell me what lines map to what labels.')
print('Please specifiy the number in the left column.')
print()

# Here we get the user input and assessing the columns we want to grab.
uin = input('Specifiy Header:\t')
header_slot = int(uin)
uin = input('Specifiy Header 2:\t')
header_2_slot = int(uin)
uin = input('Specifiy Time:\t\t')
time_slot = int(uin)
uin = input('Specifiy Body:\t\t')
body_slot = int(uin)
uin = input('Specifiy Footer:\t')
footer_slot = int(uin)




print()
print()
print('///////////////////////////////////////////////////////')
print('///////////////////// Printing ////////////////////////')
print('///////////////////////////////////////////////////////')
print()

# The 'text' variable will be the long string variable that will contain all of the output for the print job.
# Every line of output will be added together and then added on to the end of the 'text' variable.
text = ''

# Start our counter because the variable 'l' is a list, and we need to know what line in the list we're on.
c = 0
for line in l:

    # Here we gather the items from the current line
    # that we need.
    tmp_header = l[c].split(sepparator)[header_slot]
    tmp_header_2 = l[c].split(sepparator)[header_2_slot]
    tmp_time = l[c].split(sepparator)[time_slot]
    tmp_body = l[c].split(sepparator)[body_slot]
    tmp_footer = l[c].split(sepparator)[footer_slot]

    # Remember how earlier, we said that we were going to mash lines of output together and then add them onto the 'text' variable?
    # Well, this is where we do that.
    line_text = tmp_header + '\n' + tmp_header_2 + '\n' + tmp_time + '\n' + tmp_body + '\n' + tmp_footer + '\n\n'
    text = text + line_text

    c += 1

print(text)
#
