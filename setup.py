import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "tahmin",
    version = "0.0.1",
    author = "Fatih Emre KAYA",
    author_email = "kaa_femre_1998@hotmail.com",
    description = ("Tahmin Uygulaması"),
    keywords = "example test tutorial",
    url = "https://git.heroku.com/test-tahmin.git",
)