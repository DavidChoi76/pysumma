import os
import shutil
import pkg_resources

DELINEATION = pkg_resources.resource_filename(
        __name__, 'meta/grass_delineation.sh')
LC_EXTRACTION = pkg_resources.resource_filename(
        __name__, 'meta/landcover_extraction.r')
SOIL_EXTRACTION = pkg_resources.resource_filename(
        __name__, 'meta/ssurgo_extraction.r')
SOILTEXTURE2GIS = pkg_resources.resource_filename(
        __name__, 'meta/ssurgo_soiltexture2gis.r')
SSURGO_SOILS_DB = pkg_resources.resource_filename(
        __name__, 'meta/ssurgo_soils_db.csv')