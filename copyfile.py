import shutil

original = r'C:\Users\Ziyu\Desktop\course\templates\page1.html'

for i in range(2,24):
    target = r'C:\Users\Ziyu\Desktop\course\templates\page{}.html'.format(i)
    shutil.copyfile(original, target)
