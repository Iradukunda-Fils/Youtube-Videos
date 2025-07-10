from calc import Math

def info_videos(path: list | tuple) -> str:
    print("process video...")
    video_obj = Math(path)
    
    return (f"the video playlist is: {video_obj.numbers} \n"
            f"the length of the play list is: {video_obj.len}"
            )