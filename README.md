# Hyperlink

Based on Microsoft Azure cognitive APIs, our software can generate a video based on
users' pure text input. By analyzing the key phrases and words in the text, our software
will find the most matching pictures online with Bing search API, and then generate
a video composed of these pictures. The software aims to help children, people have
reading disorder and undereducated people to better understanding the text and raise
their further interest in reading and learning.

## Getting Started

Firstly, install all dependecies by runnning "dependency.py". Then user shall type in
the enter 0.0.0.0:8080 in their browser and then enter the text they want to generate 
a video for. They need to specify the gender and language that they expect in the video.

### Dependencies

This package depends on the following softwares:

- Python Library: `requests`, `sox`
- System Packages: `ffmpeg`


## Code Example

* Bing Image Search API
* Bing Speech API

## Built With

* [Azure](https://www.azure.com) - The cognitive service used
* [Web.py](https://www.webpy.org) - The web framework used

## Authors

* **Dingcheng Hu** - [UC San Diego]
* **Pengyu Chen** - [UC San Diego]
* **Wanhui Qiao** - [UC San Diego]
* **Renxu Hu** - [UC San Diego]
* **Zhibo Chen** - [UC San Diego]

## License

This project is licensed under the GPL v3.0  License.

We made this decision since `ffmpeg` is licensed under GPL.

## Additional Notice

Although we've included several API keys, but you are not authorized to use 
those keys without written consent from us. You are subject to any financial
charges that may occur if you used our included API keys.


## Acknowledgments

Azure and its APIs belong to Microsoft, Inc.
