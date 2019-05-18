from boxfinder import full_box

x=full_box()

print("Width:",abs(x[0]-x[2]))
print("Height:",abs(x[1]-x[3]))
