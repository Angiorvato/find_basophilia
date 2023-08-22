"""
File: find_basophilia.py
----------------
EN ---------------------------------- English section ----------------------------------

This program highlights cell structures (nuclei or basophils), in order to facilitate 
its visualization and subsequent identification.

------------------------------------- Parameter ------------------------------------------
Image stained with hematoxylin-eosin or Romanowsky-type stains or based on the same principle 
(staining acidic structures in blue and purple tones, such as cell nuclei; and basic components 
in pink tones).

---------------------------------- What is highlighted? ----------------------------------
Cellular structures to make its evaluation and subsequent identification easier.
* Platelets could be included in the structures to be highlighted.

---- NOTE: Could be used to highlight bacteria in Gram stains, however,
not of choice for differentiation between Gram positive and Gram negative.

ES ---------------------------------- Sección en Español ----------------------------------

Este programa destaca las estructuras celulares (núcleos o basófilos), para facilitar
su visualización y posterior identificación.

------------------------------------- Parámetro ------------------------------------------
Imagen coloreada con hematoxilina-eosina, tinciones de tipo Romanowsky o que se basen en 
el mismo principio (teñir estructuras ácidas en tonos azul y púrpura, como por ejemplo los 
núcleos celulares; y componentes básicos en tonos de color rosa).

------------------------------------- ¿Qué resalta? -------------------------------------
Estructuras celulares para hacer más sencilla su evaluación y posterior indentificación.
* Las plaquetas podrían estar incluidas en las estructuras a resaltar.

---- NOTA: Podría utilizarse para resaltar bacterias en tinciones de Gram, sin embargo, 
no es de elección para diferenciación entre Gram positivo y Gram negativo.
"""

# EN - The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed.
# ES - La línea a continuación importa SimpleImage para usar aquí,
# depende del paquete Pillow, así que debe estar instalando.
from simpleimage import SimpleImage

INTENSITY_THRESHOLD = 1.0
NEW_INTENSITY = 1.2

def find_basophilia(filename):
    """
    EN - This function allows to highlight the "sufficiently red" and "sufficiently blue" 
    pixels (which often make up the purple color in RGB) in the image and turns 
    to grayscale all other pixels in the image in order to highlight the basophilia present 
    in the image.
    
    ES - Esta función permite resaltar los píxeles "suficientemente rojos" y "suficientemente azules"
    (que a menudo componen el color púrpura en RGB) en la imagen y convierte a escala 
    de grises de todos los demás píxeles en la imagen con la finalidad de resaltar la basofilia 
    presente en la imagen.
    """
    image = SimpleImage(filename)
    for pixel in image:
        # EN - This converts the image to grayscale.
        # ES - Esto convierte la imagen a escala de grises.
        average = ((pixel.red + pixel.green + pixel.blue)//3)
        # EN - This allows to know if an image is sufficiently red and blue.
        # ES - Esto permite conocer si una imagen es suficientemente roja y azul.
        average_purple = ((pixel.red + pixel.blue)//2)
        if pixel.red and pixel.blue >= average_purple * INTENSITY_THRESHOLD:
            pixel.red = pixel.red * pixel.red * NEW_INTENSITY
            pixel.blue = pixel.blue * pixel.red * NEW_INTENSITY
        # EN - This allows any image that does not meet the mentioned standards to be 
        # converted to grayscale.
        # ES -  Esto permite convertir a escala de grises cualquier imagen que no cumpla 
        # con los estandares mencionados
        elif pixel.red >= 110 and pixel.green >= 90 and pixel.blue >= 110:
            pixel.red = average
            pixel.green = average
            pixel.blue = average
            
    return image
    
def counting_pixels(filename):
    """
    EN - This function allows the user to keep track of the amount of pixel 
    (adding +1 to count_pixels) each time the cycle is repeated for each pixel 
    in the image.
    
    ES - Esta función permite llevar la cuenta de los píxeles presentes en la imagen 
    (sumando +1 a count_pixels) cada vez que el ciclo se repite para cada pixel en la imagen.
    """
    count_pixels = 0
    image = SimpleImage(filename)
    for pixel in image:
        count_pixels +=1
        average = ((pixel.red + pixel.green + pixel.blue)//3)
        average_purple = ((pixel.red + pixel.blue)//2)
        if pixel.red and pixel.blue >= average_purple:
            pixel.red = pixel.red 
            pixel.blue = pixel.blue 
        elif pixel.red >= 100 and pixel.green >= 80 and pixel.blue >= 100:
            pixel.red = average
            pixel.green = average
            pixel.blue = average
    return count_pixels

def main():
    print("") # EN - This is a blank line for aesthetic. / ES - Esta es una línea en blanco para la estética.
    
    # EN -This allows the user to enter the image they want (as long as the 'image' subfolder
    # where their project is stored is located).  
    # ES - Esto le permite al usuario ingresar la imagen que desee (siempre y cuando esté ubicada 
    # la subcarpeta 'image' donde está guardado su proyecto).
    image_name = input('Enter an image name (with the extension, e.g. .jpg, .png, etc): ')
    
    print("") # EN - This is a blank line for aesthetic. / ES - Esta es una línea en blanco para la estética.
    
    DEFAULT_FILE = ('images/' + image_name)
    # EN - This allows the user to enter a brief description of the image they want to evaluate.
    # ES - Esto le permite al usuario ingresar una breve descripción de la imagen que quiere evaluar.
    about_image = input('What did you choose (e.g. blood smear, Gram stain, etc)? ')
    
    print("") # EN - This is a blank line for aesthetic. / ES - Esta es una línea en blanco para la estética.
    imagen = SimpleImage(DEFAULT_FILE)
    
    # EN - This function finds the amount of pixel in the image.
    # ES - Esta función encuentra la cantidad de píxeles en la imagen.
    number_of_pixels_in_the_image = counting_pixels(DEFAULT_FILE)

    # EN - Show the original fire
    # ES - Muestra el incendio forestal original.
    original_image = SimpleImage(DEFAULT_FILE)
    original_image.show()

    # EN - Show the highlighted cells (mostly nucleus), parasite, etc (everything with basophilia on it).
    # ES - Muestra las células (en su mayoría núcleos), parasitos, etc,  resaltados (todo con basofilia en él).
    highlighted_image = find_basophilia(DEFAULT_FILE)
    highlighted_image.show()
    print("There are " + str(number_of_pixels_in_the_image) + " pixels in the " + str(about_image) + " image you chose.")


if __name__ == '__main__':
    main()