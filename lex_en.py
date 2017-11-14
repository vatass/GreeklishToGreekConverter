import subprocess

f = open("alphabet_dict/en_caps_noaccent.dict", "r")

filename = 'lexicon_en'
new_file = open(filename+'.txt', 'w')

cnt_words = 0  # counter of dictionary words
counter = 0  # counter of letters of each word

for line in f:
    if len(line) == 0:
        break

    line = line[:-1]  # get rid of change of line at the end
    cnt_words = cnt_words + 1

    s = list(line)

    curr_char = s[0]

    if len(s) == 1:
        curr_state = str(0) + ' ' + str(1) + ' ' + curr_char + '\n'
        new_file.write(curr_state)
    else:
        if counter == 0:  # dummy check, so as to avoid state 1 (used as accept state at the end)
            counter = 2
        curr_state = str(0) + ' ' + str(counter) + ' ' + curr_char + '\n'
        new_file.write(curr_state)

        for i in range(1, len(s) - 1, 1):
            curr_char = s[i]
            curr_state = str(counter) + ' ' + str(counter + 1) + ' ' + curr_char + '\n'
            new_file.write(curr_state)
            counter = counter + 1
        curr_char = s[len(s) - 1]
        curr_state = str(counter) + ' ' + str(1) + ' ' + curr_char + '\n'
        new_file.write(curr_state)
    counter = counter + 1

curr_state = str(1)+'\n'
new_file.write(curr_state)
new_file.close()

bash_call = 'bash word.sh ' + filename + ' fsa_en' + ' en'
subprocess.call(bash_call, shell=True)
f.close()
