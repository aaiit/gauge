"""
pip install streamlit

git add -A 
git commit -m "update"
git pull
"""

from streamlit_webrtc import webrtc_streamer
import av

class VideoProcessor:
    def __init__(self):
        self.some_value = 0.5

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        # ...
        # self.do_something(img, self.some_value)  # `some_value` is used here
        # ...

        return av.VideoFrame.from_ndarray(img, format="bgr24")


ctx = webrtc_streamer(key="example", video_processor_factory=VideoProcessor)

if ctx.video_processor:
    ctx.video_processor.some_value = st.slider()  # `some_value` is set here