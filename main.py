from google_images_download import google_images_download
import configparser


def get_image_classes(config):
    """
    Fetches the classes in the config object and returns a list of strings
    :param config: 
    :return: 
    """
    return config['classes']['key_words'].split(",")


def main():
    config = configparser.ConfigParser()
    config.read('image_scrapper.conf')
    classes = get_image_classes(config)
    scrape_images(classes, config)


def scrape_images(classes, config):
    """
    scrapes the images from google images
    :param classes: a list of strings
    :param config: the config object file
    :return:
    """
    output_directory = config['image_scrapper_parameters']['output_directory']
    chrome_driver = config['image_scrapper_parameters']['chromedriver']
    limit = config['image_scrapper_parameters']['limit']
    size = config['image_scrapper_parameters']['exact_size']
    image_type = config['image_scrapper_parameters']['format']

    for element in classes:
        arguments = {"keywords": element,
                     "output_directory": output_directory,
                     "chromedriver": chrome_driver,
                     "limit": limit,
                     "exact_size": size,
                     "format": image_type}

        response = google_images_download.googleimagesdownload()
        print(element, output_directory, chrome_driver, limit)
        response.download(arguments)


if __name__ == "__main__":
    main()
