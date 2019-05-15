# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

num_lines = 0
total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    print(line)

    #count the number of lines
    num_lines += 1

    # code to extract float
    fval = float(fval)

    # add to total
    total = total + fval

print("Done")
print("Number of lines:", num_lines)

#turn each line into a float
#maybe use the strip function for this?
for line in fh:
    try:
        float()
    except:
        print("float error")
        quit()
#average those lines
    avg

#print the answer
print("Average spam confidence: ", ())
