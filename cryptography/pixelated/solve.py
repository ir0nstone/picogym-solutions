from PIL import Image

img1 = Image.open("scrambled1.png")
img2 = Image.open("scrambled2.png")

pixels1 = img1.load()
pixels2 = img2.load()

result_img = Image.new("RGB", img1.size)
result_pixels = result_img.load()

for x in range(img1.width):
    for y in range(img1.height):
        r1, g1, b1 = pixels1[x, y]
        r2, g2, b2 = pixels2[x, y]

        xor_r = r1 ^ r2
        xor_g = g1 ^ g2
        xor_b = b1 ^ b2

        if xor_r == xor_g == xor_b == 255:
            xor_r = xor_g = xor_b = 0

        result_pixels[x, y] = (xor_r, xor_g, xor_b)

result_img.save("output.png")
