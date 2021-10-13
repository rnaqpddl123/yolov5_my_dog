import re

source = "data/videos/dog_video-1.avi"

p = re.compile("(/S+)")
asd = p.search(source)


print(source)
print(asd)
