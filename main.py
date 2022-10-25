import requests
import lxml
from tqdm import tqdm
from bs4 import BeautifulSoup
import img2pdf


def get_data():
    headers = {
        "accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / avif, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3;q = 0.9",
        "user-agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 104.0.5112.124YaBrowser /"
                      " 22.9.3.886Yowser / 2.5Safari / 537.36"
    }

    img_list = []
    for i in range(1, 49):
        url = f"https://www.recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg"
        req = requests.get(url, headers=headers)
        responce = req.content

        with open(f'media/{i}.jpeg', 'wb') as file:
            file.write(responce)
            img_list.append(f'media/{i}.jpeg')
            print(f'Download {i} of 48')
    print("#" * 20)
    print(img_list)

    with open("result.pdf", "wb") as f:
        f.write(img2pdf.convert(img_list))

    print("PDF file download successfully!")

def main():
    get_data()

if __name__ == '__main__':
    main()