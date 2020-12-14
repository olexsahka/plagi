from aa import  file_sim

with open("text.txt", "r") as f:
    text = f.read().split()
sim_table = [0] * len(text)
for i in range(len(text)):
    sim_table[i] = [0] * len(text)
for i in range (len(text)):
    for j in range(len(text)):
        sim_table[i][j]=(file_sim(text[i],text[j]))

print(sim_table)
