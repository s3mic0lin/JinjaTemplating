from jinja2 import Environment, FileSystemLoader
from argparse import ArgumentParser
from yaml import load, Loader
from os import path

# define script arguments
parser = ArgumentParser()
parser.add_argument("-v", "--verbose", dest="verbose",
                    help="toggle verbose mode", action="store_true")
parser.add_argument("-t", "--template", dest="template",
                    help="path to template file", metavar="TEMPLATE", required=True)
parser.add_argument("-p", "--parameters", dest="parameters",
                    help="path to parameters file", metavar="PARAMETERS", required=True)
parser.add_argument("-d", "--destination", dest="destination",
                    help="path to destination file", metavar="DESTINATION", required=True)
args = parser.parse_args()

# read template file
try:
    if (args.verbose):
        print("reading template file ...")
    
    absTemplatePath = path.abspath(args.template)
    environment = Environment(loader=FileSystemLoader(path.dirname(absTemplatePath)))
    template = environment.get_template(path.basename(absTemplatePath))
except Exception as err:
    print("An error occurred while loading the template:\n\t", type(err), err)
    exit(1)

# parse parameters into object
try:
    if (args.verbose):
        print("reading parameters file ...")
    
    absParametersPath = path.abspath(args.parameters)
    parameters = load(open(absParametersPath), Loader=Loader)
except Exception as err:
    print("An error occurred while reading the parameters file:\n\t", type(err), err)
    exit(1)

# render template
try:
    if (args.verbose):
        print("rendering template ...")
    
    rendered = template.render(parameters)
except Exception as err:
    print("An error occurred while rendering the template:\n\t", type(err), err)
    exit(1)

# save result to destination file
try:
    if (args.verbose):
        print("saving result ...")
    
    absDestinationPath = path.abspath(args.destination)

    with open(absDestinationPath, "w+") as result:
        result.write(rendered)
except Exception as err:
    print("An error occurred while saving the result file:\n\t", type(err), err)
    exit(1)

if (args.verbose):
    print("done")
