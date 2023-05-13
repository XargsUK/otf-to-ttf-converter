# OTF to TTF Font Converter

## Project Description

This tool converts OpenType (OTF) fonts to TrueType (TTF) format. It also handles cmap tables in the fonts. It's designed to be easy to use and efficient, with minimal dependencies.

## Prerequisites

To use this tool, you need to have Docker installed on your machine. If you want to use the Makefile or Docker Compose to build and run the Docker container, you also need to have Make and Docker Compose installed, respectively.

## Usage

First, clone the repository:

```bash
git clone https://github.com/XargsUK/otf-to-ttf-converter.git
cd otf-to-ttf-converter
```

Then, put the OTF fonts you want to convert in the `otf` directory.

To build and run the Docker container, you can use the following command:

```bash
docker build -t font-converter .
docker run -v $(pwd)/otf:/otf -v $(pwd)/ttf:/ttf font-converter
```

This will convert the OTF fonts to TTF format and save them in the `ttf` directory.

If you have Make installed, you can use the Makefile to build and run the Docker container:

```bash
make all
```

You can also use Docker Compose to build and run the Docker container:

```bash
docker-compose up --build
```

## Credits

This tool was created by [XargsUK](https://github.com/XargsUK). Feel free to reach out if you have any questions or feedback by raising an [issue](https://github.com/XargsUK/otf-to-ttf-converter/issues).

This project uses the following open-source libraries:

- [Docker](https://www.docker.com/): A platform for developing, shipping, and running applications in containers.
- [FontForge](https://fontforge.org/): A free and open-source font editor.
- [FontTools](https://github.com/fonttools/fonttools): A library for manipulating fonts, written in Python.
- [Python](https://www.python.org/): A high-level programming language for general-purpose programming.
