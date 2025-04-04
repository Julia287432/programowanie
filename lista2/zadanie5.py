from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_image, output_image="watermark.png", text="pies",):
    
            image = Image.open(input_image)
            
            if image.mode != 'RGBA':
                image = image.convert('RGBA')
            
            width, height = image.size
            watermark_layer = Image.new("RGBA", image.size, (0,0,0,0))
            draw = ImageDraw.Draw(image)
            
            font = ImageFont.truetype("arial.ttf", 200) 
        
            position = (width / 2, height / 2)

            text_color = (255, 255, 255, 128) 

            draw.text(position, text, font=font, fill=text_color)

            result = Image.alpha_composite(image, watermark_layer)
            result.save(output_image)

add_watermark("C:/Users/julia/OneDrive/Pulpit/Zdjecie-psa.jpg")

