from .pdformer.pdformer import Pdformer
from input.config.conf import *
import json

class PdfReader():
    def __init__(self):
        self.result_file = result_file

    def read(self,):
        '''
          read the document and save it into folder
        '''
        root_titles = Pdformer().pdf2json()
        with open(self.result_file, "w") as f:
            json.dump(root_titles, f, indent=2)

    def load(self):
        '''
        load the result from folder
        '''
        if not os.path.exists(self.result_file):
            print("No result_file found! It hasn't been generated yet.")

        with open(self.result_file, "r") as f:
            root_titles = json.load(f)
        return root_titles


    #TODO: 各种 expert ocr