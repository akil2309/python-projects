from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()
search_queries =['The smartphone also features an in display fingerprint sensor.',
                 'The pop up selfie camera is placed aligning with the rear cameras.',
                 '''In terms of storage Vivo V15 Pro could offer 
                 up to 6GB of RAM and 128GB of onboard storage.''',
                 'The smartphone could be fuelled by a 3 700mAh battery.',
                 ]


def downloadimg(query):
    arguments = {"keywords": query,
                 "format": "jpg",
                 "limit": 4,
                 "print_urls": True,
                 "size": "medium",
                 "aspect_ratio": "panoramic"}
    try:
        response.download(arguments)
    except FileNotFoundError:
        arguments = {"keywords": query,
                     "format": "jpg",
                     "limit": 4,
                     "print_urls": True,
                     "size": "medium"}
        try:
            response.download(arguments)
        except:
            pass


for query in search_queries:
    downloadimg(query)
    print()