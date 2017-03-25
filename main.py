import imageio
imageio.plugins.ffmpeg.download()

from moviepy.editor import *

def renderNew(vid_name, output_vid_name):
    vid_orig = VideoFileClip(vid_name, audio=False)
    video_size = vid_orig.size
    vid1 = VideoFileClip(vid_name).resize((video_size[0]/2,video_size[1]/2)).set_pos(("left", "top"))
    vid2 = VideoFileClip(vid_name).resize((video_size[0]/2,video_size[1]/2)).set_pos(("right", "top"))
    vid3 = VideoFileClip(vid_name).resize((video_size[0]/2,video_size[1]/2)).set_pos(("right", "bottom"))
    vid4 = VideoFileClip(vid_name).resize((video_size[0]/2,video_size[1]/2)).set_pos(("left", "bottom"))
    final = CompositeVideoClip([vid_orig, vid1, vid2, vid3, vid4])
    final.write_videofile(output_vid_name)

def main():
    # 4 ^ n  
    exponent = 10
    exp_org = exponent
    originalVideo = "trump_output.mp4"
    renderNew(originalVideo, "output{}.mp4".format(str(exp_org - exponent)))
    while exponent > 0:
        if exponent == 1:
            renderNew("output{}.mp4".format(str(exp_org - exponent)), "FINALOUTPUT.webm")
        else:
            renderNew("output{}.mp4".format(str(exp_org - exponent)), "output{}.mp4".format(str(exp_org - exponent + 1)))
        exponent = exponent - 1


if __name__ == "__main__":
    main()
