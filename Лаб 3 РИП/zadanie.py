from librip.gens import gen_random
from histogram import Hist

a = [a for a in gen_random(1, 50, 300)]

username_friend_gist = Hist(a)
username_friend_gist.printGist()

# show gist
title = "Гистограмма"
title_x = "Числа"
title_y = "Количество чисел"
username_friend_gist.showBar(title, title_x, title_y)
