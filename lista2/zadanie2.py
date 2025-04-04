from PIL import Image

def generate_thumbnail(input_name, size, output_name):
 
    image = Image.open(input_name)
    
    image = image.convert('RGB')
    
    size_tuple = tuple(map(int, size.split('x')))
    
    image.thumbnail(size_tuple)
    
    image.save(output_name, "JPEG")

generate_thumbnail("C:/Users/julia/OneDrive/Pulpit/Zdjecie-psa.jpg", "100x100", "C:/Users/julia/OneDrive/Pulpit/Zdjecie-psa-mini.jpg")

