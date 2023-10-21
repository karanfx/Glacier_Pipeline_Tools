# # import pxr.Usdview 
# import os
# cur_shot = os.environ("SHOT")
# print(cur_shot)

# print('Launch through subprocess')

#converting image seq into video
def seq_converter(ffmpeg_path,input_seq,output_dir):
    import subprocess
    ffmpeg_command = [
        "ffmpeg",
        "-framerate", "24",
        "-i", input_seq,
        "-c:v", "libx264",
        "-vf", "fps=24",
        output_dir
    ]

    try:
        subprocess.run(ffmpeg_command, check=True)
        print("Image sequence converted to video successfully.")
    except subprocess.CalledProcessError as e:
        print("Error:", e)


# seq_converter("ffmpeg","D:/test_seq/v004/test_seq.%04d.png","D:/test_seq/test_explosion_v016.mp4")

import datetime
time = datetime.datetime.now()
print(str(time.strftime("%Y-%m-%d  %H:%M:%S")))