# Space Instagram
Download photos from the site [spacexdata.com](https://spacexdata.com) and from the site
[hubblesite.org](http://hubblesite.org), then uploads them to an Instagram account.

### How to install
In the `.env` file, you need to write your username and password from Instagram
```text
LOGIN_INSTAGRAM = "Your username"
PASSWORD_INSTAGRAM = 'Your Password'
```

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).

### Features

Instagram accepts only .jpg photos of maximum size 1080x1080