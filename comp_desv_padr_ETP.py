# -*- coding: utf-8 -*-

""" Compute standard deviation of ETP. """

__author__ = "Leidinice Silva"
__email__ = "leidinice.silvae@funceme.br"
__date__ = "20/09/2016"
__description__ = " Compute standard deviation of ETP "

# Import data
import netCDF4
import calendar
import argparse
import datetime
import numpy as np
import numpy.ma as ma

from PyFuncemeClimateTools import Thiessen
from PyFuncemeClimateTools import PlotMaps as pm
from PyFuncemeClimateTools import DefineGrid as dg
from hidropy.preprocessing.write_thiessen import write_thiessen

y1, y2, x1, x2 = -60, 15, -90, -33

mes = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
dic = {'Jan': 31., 'Fev': 28.5, 'Mar': 31., 'Abr': 30., 'Mai': 31., 'Jun': 30., 'Jul': 31., 'Ago': 31., 'Set': 30.,
       'Out': 31., 'Nov': 30., 'Dez': 31.}

cor1 = ('#ffffff', '#ffff00', '#fcd17d', '#ff8000', '#ff0000', '#750000', '#340003') #Paleta
lev1 = (5., 7.5, 10., 12.5, 15., 17.5, 20.)

# Directories of input and output data
path_in = "/home/leidinice/Documentos/musf/dados/"
name = 'pet_CRU_SA_1981_2010_std.nc'
data = netCDF4.Dataset(path_in + name)
var  = data.variables['eto'][:, :, :] # Declaring variable under study to calculate the
lats = data.variables['lat'][:] # Declaring latitude
lons = data.variables['lon'][:] # Declaring longitude

for m in range(0, var.shape[0]):
    print m, mes[m], dic[mes[m]]

    title1 = u'Evapotranspiração Potencial\n Desvio Padrão - {0}'.format(mes[m])

    figou1 = 'plot_STD_CRU_{0}.png'.format(mes[m])

    pm.plotmap(var[m, :, :] * dic[mes[m]], lats, lons,
           latsouthpoint=y1, latnorthpoint=y2, lonwestpoint=x1, loneastpoint=x2, ocean_mask=1,
           fig_name=figou1, fig_title=title1, barcolor=cor1, barlevs=lev1, barinf='max', barloc='right')

    print np.nanmax(var), np.nanmin(var)
