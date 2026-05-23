import os

import requests
import torch


class RaveLoader:

    def download_official_model_by_name(self, model_name: str):
        """Returns official RAVE model from ACIDS' website."""

        model_url = f'https://play.forum.ircam.fr/rave-vst-api/get_model/{model_name}'
        model = self.download_rave_model_from_url(model_url, model_file_path=f'pretrained_model_checkpoints/rave_model_checkpoints/{model_name}.ts')
        return model

    def download_rave_model_from_url(self, model_url: str, model_file_path: str):
        # download rave parameters/weights and build the model
        # url = 'https://play.forum.ircam.fr/rave-vst-api/get_model/musicnet'
        # url = 'https://play.forum.ircam.fr/rave-vst-api/get_model/percussion'
        # url = 'https://play.forum.ircam.fr/rave-vst-api/get_model/vintage'
        # url = 'https://play.forum.ircam.fr/rave-vst-api/get_model/nasa'
        # url = 'https://play.forum.ircam.fr/rave-vst-api/get_model/darbouka_onnx'
        # url = 'https://play.forum.ircam.fr/rave-vst-api/get_model/VCTK'
        # you can learn more about each model at:
        # https://acids-ircam.github.io/rave_models_download

        if not os.path.exists(model_file_path):
            print(f"Downloading model from url: {model_url} to {model_file_path}")
            self.download_file_from_url(model_url, model_file_path)
        else:
            print(f"loading model from {model_file_path}")
        model = torch.jit.load(model_file_path).eval()
        return model

    @staticmethod
    def download_file_from_url(url, file_path):
        """
        Download file from a given URL and save it to the specified file path.
        """
        response = requests.get(url)
        response.raise_for_status()  # This will raise an exception if there is an error
        with open(file_path, 'wb') as file:
            file.write(response.content)
        os.system(f"cp {file_path} interfaces/{file_path.split('/')[-1]}")
    
    @staticmethod
    def load_model_from_file_path(model_file_path: str):
        print(f"loading model from {model_file_path}")
        model = torch.jit.load(model_file_path).eval()
        return model

