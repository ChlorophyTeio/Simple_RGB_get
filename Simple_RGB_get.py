import time
import sensor

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)

i = 0
prev_time = time.time()

while True:
    img = sensor.snapshot()
    i += 1
    current_time = time.time()
    if current_time - prev_time >= 5:
        r, g, b = img.get_pixel(160, 120)
        print("RGB color at (160, 120):", r, g, b)
        prev_time = current_time
    img.draw_cross(160, 120, color=0xFFFFFF, size=3, thickness=1)
