import cv2
import os

def extrapolate_frames(video_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Get the frames per second (fps) of the input video
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    print(f"Video FPS: {fps}")
    print(f"Total Frames: {total_frames}")

    # Loop through all frames and save them as images
    # fps*5 should able us to take one frame every 5 seconds
    for frame_num in range(total_frames):
        # Read the next frame
        ret, frame = cap.read()

        # Break the loop if we have reached the end of the video
        if not ret:
            break


        if frame_num % fps*50 ==0 :

            # Save the frame as an image
            frame_filename = os.path.join(output_folder, f"frame_{frame_num + 1}.jpg")

            #rotated_frame = cv2.rotate(frame, cv2.ROTATE_180)
            cv2.imwrite(frame_filename, frame)

        # Print progress
        if frame_num % 100 == 0:
            print(f"Processed {frame_num} frames")

    # Release the video capture object
    cap.release()

    print("Extrapolation complete!")

if __name__ == "__main__":
    # Specify the path to the video file
    video_path = "3. unable to recharge (painful user experience).mov"

    # Specify the output folder for the frames
    output_folder = "output_frames"

    # Call the function to extrapolate frames
    extrapolate_frames(video_path, output_folder)
