#!/usr/bin/env python3


import pickle


class Picky:
    def save(obj, filename):
        file = open(filename + ".obj", "wb")
        pickle.dump(obj, file, pickle.HIGHEST_PROTOCOL)
        file.close()

    def load(filename):
        file = open(filename + ".obj", "rb")
        object_file = pickle.load(file)
        file.close()

        return object_file
