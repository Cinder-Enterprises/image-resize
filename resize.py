from PIL import Image
import os

image_sizes = []
steam_sizes = [
    (460, 215),
    (231, 87),
    (616, 353),
    (374, 448),
    (1438, 810),
    (600, 900),
    (3840, 1240),
    (1920, 1080),
    (1280, 720),
    (184, 69),
    (32, 32),
    (444, 208),
    (184, 184),
    (16, 16),
    (24, 24),
    (64, 64),
    (96, 96)
]
kindle_fire_sizes = [
    (512, 512),
    (114, 114),
    (1024, 500)
]

apple_boot_sizes = [
    (640, 1136),
    (640, 960),
    (750, 1334),
    (768, 1024),
    (1024, 768),
    (1125, 2436),
    (1224, 2208),
    (1536, 2048),
    (2048, 1536),
    (2208, 1242),
    (2436, 1125),
    (2688, 1242),
    (2732, 2048)
]
apple_icon_sizes = [
    (1024, 1024),
    (1536, 1536),
    (20, 20),
    (29, 29),
    (40, 40),
    (58, 58),
    (60, 60),
    (76, 76),
    (80, 80),
    (87, 87),
    (114, 114),
    (120, 120),
    (152, 152),
    (167, 167),
    (180, 180)
]
all_stores = [steam_sizes, kindle_fire_sizes, apple_boot_sizes, apple_icon_sizes]

def main():
    for image_file in os.listdir("."):
        if image_file.endswith('.png'):
            for store_size in all_stores:
                for image_size_req in store_size:
                    image_instance = Image.open(image_file)
                    file_name, file_ext = os.path.splitext(image_file)
                    new_image = image_instance.resize(image_size_req)
                    new_image.load()
                    background = Image.new("RGB", new_image.size, (255, 2555, 255))
                    background.paste(new_image, mask=new_image.split()[2])
                    new_image.save("{}{}x{}{}".format(file_name, image_size_req[0], image_size_req[1], file_ext, quality=80))

if __name__ == '__main__':
    main()