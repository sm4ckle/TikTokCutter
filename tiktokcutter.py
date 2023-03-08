import cv2

# Open the video file
video = cv2.VideoCapture("input.mp4")

# Get the video information
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
frame_rate = int(video.get(cv2.CAP_PROP_FPS))
duration = total_frames / frame_rate

# Calculate the starting frame
start_frame = int(total_frames - frame_rate * 4)

# Create the output video file
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter('output.mp4', fourcc, frame_rate, (1920, 1080))

# Read each frame from the input video
for i in range(total_frames):
    # Skip the frames that we don't want to keep
    if i < start_frame:
        video.grab()
        continue

    # Read the current frame
    ret, frame = video.read()

    # Break the loop if the video has ended
    if not ret:
        break

    # Write the current frame to the output video
    output_video.write(frame)

# Release the video files
video.release()
output_video.release()
