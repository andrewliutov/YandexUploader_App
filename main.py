import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        api_url = 'https://cloud-api.yandex.net'
        params = {'path': file_name}
        headers = {'accept': 'application/json',
                   'authorization': f'OAuth {uploader.token}'}
        req = requests.get(api_url + '/v1/disk/resources/upload',
                           params=params, headers=headers)
        upload_url = req.json()['href']
        requests.put(upload_url, headers=headers,
                     files={'file': open(path_to_file, 'rb')})


if __name__ == '__main__':
    path_to_file = input('Введите путь к файлу на Вашем устройстве: ')
    file_name = input('Введите имя для файла на Яндекс.Диске: ')
    token = input('Введите токен: ')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
