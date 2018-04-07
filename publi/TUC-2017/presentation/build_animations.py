import os
import subprocess
import time


SPLIT_PERIOD = 20
MAX_FRAMES = 10000

pictures = {
    'mono_demo': 430
}

i = 0
for name, nb_frames in pictures.items():
    while i<nb_frames:
        in_gif = os.path.join('animation', name + '.gif')
        out_png = os.path.join('animation', name + '.png')
        next_i = i + SPLIT_PERIOD
        if i==0:
            delete_option = "-delete {}-10000".format(next_i+1)
        else:
            delete_option = "-delete 0-{} -delete {}-10000".format(i, next_i+1)
        cmd = "convert -coalesce {} {} {}".format(delete_option, in_gif, out_png)
        print(cmd)
        os.system(cmd)
        # subprocess.run(["convert", "-coalesce",
        #                 "-delete 0-{}".format(i),
        #                 "-delete {}-10000".format(next_i+1),
        #                 in_gif, out_png])
        i = next_i
