import os

def html(name):
    return '''
    <img
        class="main-window-imgs"
        src="./src/images/{0}"
        title="{0}"
        alt="{0}"
    />
    '''.format(name)

def src(name :str,i :int):
    return name[0:name.find('.')] + ":this.allImgsDom[{0}],\n".format(i)


def dom(name):
    name1 = name[0: name.find(".")]
    return f'{name1} : new Dom("{name1}"),\n'


names = os.listdir("S:\\Users\\Utkarsh\\Documents\\Project2\\CE8\\src\\images\\Beam and Slab")

count = 108

srcs = ''
doms = ''
htms = ''
for i in range(len(names)):
    htms = htms + html(names[i])
    doms = doms + dom(names[i])
    srcs = srcs + src(names[i],i+count)



# open("temp.txt","w").write()
allItems = f'{htms}\n\n{srcs}\n\n{doms}'
open("temp2.txt","w").write(allItems)

print("Done 👍")
# print(os.__path__)
# 