# yolov3-tutorial
Tutorial how to use YOLOv3

### To dos 
- [x] Clone [YOLOv3 Project](https://github.com/ultralytics/yolov3) 
- [x] Refactor the codes
    - [x] Make main file to run: `main.py`
    - [x] Make YOLOv3 Class (Easier to add & integrate another object detection 
            algorithms in the future)
- [x] Unit Testing
    - [x] Run test with `1 Image` as the input
    - [x] Run test with `1 Folder of images` as the input
    - [x] Run test with `video` as the input
    - [x] Run test with `RTSP/RTMP real-time video streaming` as the input
- [ ] Additional features
    - [x] Save raw images into a specific folder: `./export/images_txt/<datetime>/raw/`
    - [x] Save bbox images into a specific folder: `./export/images_txt/<datetime>/bbox/`
    - [x] Save cropped (bbox) images into a specific folder: `./export/images_txt/<datetime>/crop/`
    - [x] Export bbox coordinates: `./export/images_txt/<datetime>/txt/`
    - [x] Show real-time video: `Raw images` (OpenCV) 
    - [x] Show real-time video: `BBox images` (OpenCV) 
    - [ ] Calculation of mAP
    - [ ] Documentation to train a custom dataset

### Requirements 
1. Python 3.7++
2. NVIDIA GPU (Optional)

### Installation
1. Install python environment: 
    `$ python3 -m venv venv`
    - If you face error, try install required 
        [depencencies](https://linuxize.com/post/how-to-create-python-virtual-environments-on-ubuntu-18-04/): 
        `$ sudo apt install python3-dev`
        `$ sudo apt install python3-venv`
2. Enable python3 virtual environment
    - Using BASH: `$ . venv/bin/activate`
    - Using [FISH](https://github.com/fish-shell/fish-shell): 
        `$ . venv/bin/activate.fish`
3. Install Python libraries
    - `$ pip install -r requirements.txt`
    - `$ pip install pycocotools==2.0.0` (It needs to be installed separately)

### How to use 
1. Finish the installation procedure
2. Run the `main.py` file. It has several configuration. Here are some example:
    - Input as `list of images` in a specific folder
        - Simple command: `$ python main.py --source-type-folder`
        - Change folder source: `$ python main.py --source-type-folder --source "data/images/sample-4-frames/"`
        - Export all the results (Raw images, bbox images, cropped images/bbox img, bbox information): 
            `$ python main.py --source-type-folder --dump-raw-img --dump-bbox-img --dump-crop-img --save-txt`
    - Input as `video file` or `video stream (RTSP/RTMP)`
        - Simple command: `$ python main.py`
        - Change video file source: `$ python main.py --source "data/videos/customTest_MIRC-Roadside-5s.mp4"`
        - Change CV Out Window size: `$ python main.py --window-size-height 1920 --window-size-width 1080`
        - Change video stream (RTMP) source: `$ python main.py --source "rtmp://<your_ip>"`
        - Change video stream (RTSP) source: `$ python main.py --source "rtsp://<your_ip>"`
        - Stop after processing N frames (e.g.: `N=2`): `$ python main.py --is_limited --max_frames 2`
        - Export all the results (Raw images, bbox images, cropped images/bbox img, bbox information): 
            `$ python main.py --dump-raw-img --dump-bbox-img --dump-crop-img --save-txt"`
    

### Contributors 
1. Muhammad Febrian Ardiansyah 
([github](https://github.com/ardihikaru), 
[gitlab](https://gitlab.com/ardihikaru), 
[bitbucket](https://bitbucket.org/ardihikaru3/))

### Important resources 
1. Git issues
    - [Removed a file from the entire commit history](https://myopswork.com/how-remove-files-completely-from-git-repository-history-47ed3e0c4c35)

### License 
[MIT](https://choosealicense.com/licenses/mit/)
