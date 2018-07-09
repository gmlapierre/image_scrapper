from google_images_download import google_images_download
import configparser
from itertools import chain
import csv


def read_csv_to_list_of_strings(path):
    with open(path, 'r') as f:
        reader = csv.reader(f)
        words = list(filter(None, list(chain.from_iterable(reader))))  # Flattens 2d list and removes blank strings
    return words


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


def main():
    config = configparser.ConfigParser()
    config.read('image_scrapper.conf')
    classes = read_csv_to_list_of_strings(config['classes']['csv_path'])
    scrape_images(classes, config)


if __name__ == "__main__":
    main()
