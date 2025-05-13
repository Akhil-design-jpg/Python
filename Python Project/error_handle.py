file = open('youtube.txt','w')

try:
    file.write('chai aur code')
finally:
    file.close()
    
    # same as code written above
with open('youtube.txt','w') as file:
    file.write('Chai aur python')