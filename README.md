# yolov3-tutorial
Tutorial how to use YOLOv3

### To dos 
- [ ] Clone [YOLOv3 Project](https://github.com/ultralytics/yolov3) 
- [ ] Refactor the codes
    - [ ] Make main file to run: `main.py`
    - [ ] Make YOLOv3 Class (Easier to add & integrate another object detection 
            algorithms in the future)
- [ ] Unit Testing
    - [ ] Run test with `1 Image` as the input
    - [ ] Run test with `1 Folder of images` as the input
    - [ ] Run test with `video` as the input
    - [ ] Run test with `RTSP/RTMP real-time video streaming` as the input
- [ ] Additional features
    - [ ] Save raw images into a specific folder: `./export/images/raw/<datetime>`
    - [ ] Save bbox images into a specific folder: `./export/images/bbox/<datetime>`
    - [ ] Save cropped (bbox) images into a specific folder: `./export/images/crop/<datetime>`
    - [ ] Show real-time video: `Raw images` (OpenCV) 
    - [ ] Show real-time video: `BBox images` (OpenCV) 
    - [ ] Export bbox coordinates
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
// TBD

### Contributors 
1. Muhammad Febrian Ardiansyah 
([github](https://github.com/ardihikaru), 
[gitlab](https://gitlab.com/ardihikaru), 
[bitbucket](https://bitbucket.org/ardihikaru3/))

### Important resources 
// TBD

### License 
[MIT](https://choosealicense.com/licenses/mit/)
