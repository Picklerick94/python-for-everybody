# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
spam = 'X-DSPAM-Confidence:'

for line in fh:
    if line.startswith(spam)
      count = count + 1
      line_stripped = line.rstrip()
      find_num = line_stripped.find(':')
      num = line_stripped[find_num : ]
      average = sum(num) / count
    if not line.startswith(spam) : continue
print("Average spam confidence:", float(average))
