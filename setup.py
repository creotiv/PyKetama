from distutils.core import setup, Extension

if __name__ == "__main__":
    setup(
          name = "pyketama",
          version = "0.1",
          packages = ['pyketama'],
          ext_modules = [Extension("pyketama.hashes",["pyketama/pyketama.hashes.c"])],
          maintainer = 'Andrey Nikishaev',
	      maintainer_email = 'creotiv@gmail.com',
	      url = 'http://github.com/creotiv/pyketama'
    )
