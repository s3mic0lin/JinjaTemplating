# Jinja Templating

This script is designed to render a [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) template combined with parameters from a [YAML](https://en.wikipedia.org/wiki/YAML) file into a single resulting file.

## Windows installation

Install Python3
```powershell
winget install Python.Python.3.12
```

Install packages
```powershell
python -m pip install -r requirements.txt
```

Hint:  
You may need to open a new powershell window to use python after the installation.

## Ubuntu installation

Install Python3 
```bash
sudo apt install python3
```

Install packages
```powershell
python3 -m pip install -r requirements.txt
```

## Usage

Print help

```bash
# Windows
$ python script.py -h
# Ubuntu
$ python3 script.py -h

# Result
usage: script.py [-h] [-v] -t TEMPLATE -p PARAMETERS -d DESTINATION

options:
  -h, --help            show this help message and exit
  -v, --verbose         toggle verbose mode
  -t TEMPLATE, --template TEMPLATE
                        path to template file
  -p PARAMETERS, --parameters PARAMETERS
                        path to parameters file
  -d DESTINATION, --destination DESTINATION
                        path to destination file
```

The following command loads the template-file `templates/template.drawio.j2` and parameters from `parameters.yml`.  
Those files will be combined and rendered into `results/result.drawio`.

```bash
# Windows
$ python script.py -t templates/template.drawio.j2 -p parameters.yml -d results/result.drawio

# Ubuntu
$ python3 script.py -t templates/template.drawio.j2 -p parameters.yml -d results/result.drawio
```
