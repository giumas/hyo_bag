import osimport sys# Always prefer setuptools over distutilsfrom setuptools import setup, find_packages# ---------------------------------------------------------------------------#                             Some helper stuff# ---------------------------------------------------------------------------here = os.path.abspath(os.path.dirname(__file__))def is_windows():    """ Check if the current OS is Windows """    return (sys.platform == 'win32') or (os.name is "nt")def txt_read(*paths):    """ Build a file path from *paths* and return the textual contents """    with open(os.path.join(here, *paths), encoding='utf-8') as f:        return f.read()# ---------------------------------------------------------------------------#                      Populate dictionary with settings# ---------------------------------------------------------------------------# Create a dict with the basic information that is passed to setup after keys are added.setup_args = dict()setup_args['name'] = 'hyo.bag'setup_args['version'] = '0.5.3'setup_args['url'] = 'https://bitbucket.org/gmasetti/hyo_bag/'setup_args['license'] = 'LGPLv3 license'setup_args['author'] = 'Giuseppe Masetti (CCOM,UNH); Brian R. Calder (CCOM,UNH)'setup_args['author_email'] = 'gmasetti@ccom.unh.edu, brc@ccom.unh.edu'## descriptive stuff#description = 'A package to manage Bathymetric Attributed Grid (BAG) data files.'setup_args['description'] = descriptionsetup_args['long_description'] = (txt_read('README.rst') + '\n\n\"\"\"\"\"\"\"\n\n' +                                  txt_read('HISTORY.rst') + '\n\n\"\"\"\"\"\"\"\n\n' +                                  txt_read('AUTHORS.rst') + '\n\n\"\"\"\"\"\"\"\n\n' +                                  txt_read(os.path.join('docs', 'how_to_contribute.rst')))setup_args['classifiers'] = \    [  # https://pypi.python.org/pypi?%3Aaction=list_classifiers        'Development Status :: 4 - Beta',        'Intended Audience :: Science/Research',        'Natural Language :: English',        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',        'Operating System :: OS Independent',        'Programming Language :: Python',        'Programming Language :: Python :: 3',        'Programming Language :: Python :: 3.5',        'Programming Language :: Python :: 3.6',        'Topic :: Scientific/Engineering :: GIS',        'Topic :: Office/Business :: Office Suites',    ]setup_args['keywords'] = "hydrography ocean mapping survey bag openns"## code stuff## requirementssetup_args['setup_requires'] =\    [        "setuptools",        "wheel",    ]setup_args['install_requires'] =\    [        "lxml",        "numpy",        "gdal",  # <2.0 or >=2.1 for freezing    ]if not is_windows():    setup_args['install_requires'].append("h5py")  # since there are issues in building it from pypi on Win# hyo namespace, packages and other filessetup_args['namespace_packages'] = ['hyo']setup_args['packages'] = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests", "*.test*",                                                ])setup_args['package_data'] =\    {        '': ['media/*.png', 'media/*.ico', 'media/*.icns', 'media/*.txt',],        'hyo.bag': [            'iso19139/bag/*',            'iso19139/gco/*',            'iso19139/gmd/*',            'iso19139/gmi/*',            'iso19139/gml/*.xsd',            'iso19139/gml/*.txt',            'iso19139/gml/3.1.1/smil/*',            'iso19139/gsr/*',            'iso19139/gss/*',            'iso19139/gts/*',            'iso19139/xlink/*',            'iso19757-3/*',            'samples/*',        ],    }setup_args['test_suite'] = "tests"setup_args['entry_points'] =\    {        'console_scripts': ['bag_bbox = hyo.bag.tools.bag_bbox:main',                            'bag_elevation = hyo.bag.tools.bag_elevation:main',                            'bag_metadata = hyo.bag.tools.bag_metadata:main',                            'bag_tracklist = hyo.bag.tools.bag_tracklist:main',                            'bag_uncertainty = hyo.bag.tools.bag_uncertainty:main',                            'bag_validate = hyo.bag.tools.bag_validate:main'],    }# ---------------------------------------------------------------------------#                            Do the actual setup now# ---------------------------------------------------------------------------setup(**setup_args)