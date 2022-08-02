import matplotlib.pylab as mpl
import math
#fig.tight_layout(pad=0.2)
#Font
fontParams = {'font.family' : 'sans-serif',
           'font.serif' : ['Times', 'Computer Modern Roman'],
           'font.sans-serif' : ['Helvetica', 'Computer Modern Sans serif'],
           'svg.fonttype' : 'none',
           #'pdf.fonttype' : 42,
           'text.usetex' : True,
           # To force LaTeX use Helvetica fonts.
           'text.latex.preamble': [
                                    r'\usepackage{siunitx}',
                                    r'\sisetup{detect-all}',
                                    r'\usepackage{helvet}',
                                    r'\usepackage[eulergreek,EULERGREEK]{sansmath}',
                                    r'\sansmath'],
              }
mpl.rcParams.update(fontParams)


def get_figsize(fig_width_pt):
    inches_per_pt = 1.0/72.0                # Convert pt to inch
    golden_mean = (math.sqrt(5)-1.0)/2.0    # Aesthetic ratio
    fig_width = fig_width_pt*inches_per_pt  # width in inches
    fig_height = fig_width*golden_mean      # height in inches
    fig_size =  [fig_width,fig_height]      # exact figsize
    return fig_size

# Constants from ACS Authour Guidelines.
width_single_column = 3.25
width_double_column = 7.00
height_single_column  = width_single_column * 0.618 * 1.1
height_double_column  = width_double_column * 0.618 * 1.1
# single column 
scParams = {'font.size': 8,
           'axes.labelsize' : 8,
           'axes.linewidth' : 1,

           'xtick.major.size' : 2,
           'xtick.major.width' : 0.5,
           'xtick.minor.size' : 1,
           'xtick.minor.width' :0.5,
           'ytick.major.size' : 2,
           'ytick.major.width' : 0.5,
           'ytick.minor.size' : 1,
           'ytick.minor.width' : 0.5,

           #'text.fontsize' : 8,
           'xtick.labelsize' : 8,
           'ytick.labelsize' : 8,

           'figure.figsize' : (width_single_column, height_single_column),
           #'figure.figsize': get_figsize(300),
           'figure.subplot.left' : 0.125,
           'figure.subplot.right' : 0.95,
           'figure.subplot.bottom' : 0.1,
           'figure.subplot.top' : 0.95,
           
           'savefig.dpi' : 300,
           #'savefig.bbox': 'tight',
           # this will crop white spaces around images that will make
           # width/height no longer the same as the specified one.

           'legend.fontsize' : 7.5,
           'legend.frameon' : False,
           'legend.numpoints' : 1,
           'legend.handlelength' : 2,
           'legend.scatterpoints' : 1,
           'legend.labelspacing' : 0.5,
           'legend.markerscale' : 0.9,
           'legend.handletextpad' : 0.5,  # pad between handle and text
           'legend.borderaxespad' : 0.5,  # pad between legend and axes
           'legend.borderpad' : 0.5,  # pad between legend and legend content
           'legend.columnspacing' : 1,  # pad between each legend column


           'lines.linewidth' : 1,
           'lines.markersize' : 4,
           }

dcParams = {'font.size': 11,
           'axes.labelsize' : 13,
           'axes.linewidth' : 1,

           'xtick.major.size' : 4,
           'xtick.major.width' : 1,
           'xtick.minor.size' : 2,
           'xtick.minor.width' :1,
           'ytick.major.size' : 4,
           'ytick.major.width' : 1,
           'ytick.minor.size' : 2,
           'ytick.minor.width' : 1,

           #'text.fontsize' : 8,
           'xtick.labelsize' : 13,
           'ytick.labelsize' : 13,

           'figure.figsize' : (width_double_column, height_double_column),
           #'figure.figsize': get_figsize(300),
           'figure.subplot.left' : 0.125,
           'figure.subplot.right' : 0.95,
           'figure.subplot.bottom' : 0.1,
           'figure.subplot.top' : 0.95,
           
           'savefig.dpi' : 500,
           #'savefig.bbox': 'tight',
           # this will crop white spaces around images that will make
           # width/height no longer the same as the specified one.

           'legend.fontsize' : 13,
           'legend.frameon' : False,
           'legend.numpoints' : 1,
           'legend.handlelength' : 2,
           'legend.scatterpoints' : 1,
           'legend.labelspacing' : 0.5,
           'legend.markerscale' : 0.9,
           'legend.handletextpad' : 0.5,  # pad between handle and text
           'legend.borderaxespad' : 0.5,  # pad between legend and axes
           'legend.borderpad' : 0.5,  # pad between legend and legend content
           'legend.columnspacing' : 1,  # pad between each legend column


           'lines.linewidth' : 2,
           'lines.markersize' : 5,
           }

smallParams = {'font.size': 6,
           'axes.labelsize' : 6,
           'axes.linewidth' : 1,

           'xtick.major.size' : 2,
           'xtick.major.width' : 0.5,
           'xtick.minor.size' : 1,
           'xtick.minor.width' :0.5,
           'ytick.major.size' : 2,
           'ytick.major.width' : 0.5,
           'ytick.minor.size' : 1,
           'ytick.minor.width' : 0.5,

           #'text.fontsize' : 8,
           'xtick.labelsize' : 5,
           'ytick.labelsize' : 5,

           'figure.figsize' : (width_single_column*0.5, width_single_column*0.5),
           #'figure.figsize': get_figsize(300),
           'figure.subplot.left' : 0.125,
           'figure.subplot.right' : 0.95,
           'figure.subplot.bottom' : 0.1,
           'figure.subplot.top' : 0.95,
           
           'savefig.dpi' : 300,
           'figure.dpi' : 300,
           #'savefig.bbox': 'tight',
           # this will crop white spaces around images that will make
           # width/height no longer the same as the specified one.

           'legend.fontsize' : 4.5,
           'legend.frameon' : False,
           'legend.numpoints' : 1,
           'legend.handlelength' : 2,
           'legend.scatterpoints' : 1,
           'legend.labelspacing' : 0.5,
           'legend.markerscale' : 0.9,
           'legend.handletextpad' : 0.5,  # pad between handle and text
           'legend.borderaxespad' : 0.5,  # pad between legend and axes
           'legend.borderpad' : 0.5,  # pad between legend and legend content
           'legend.columnspacing' : 1,  # pad between each legend column


           'lines.linewidth' : 1,
           'lines.markersize' : 4,
           }

f3Params = {'font.size': 6,
           'axes.labelsize' : 4,
           'axes.linewidth' : 1,
           'axes.labelpad' : 0.2,
           'xtick.major.pad'      : 4 ,
           'ytick.major.pad'      : 4 ,
           'xtick.major.size' : 2,
           'xtick.major.width' : 0.5,
           'xtick.minor.size' : 1,
           'xtick.minor.width' :0.5,
           'ytick.major.size' : 2,
           'ytick.major.width' : 0.5,
           'ytick.minor.size' : 1,
           'ytick.minor.width' : 0.5,

           #'text.fontsize' : 8,
           'xtick.labelsize' : 4,
           'ytick.labelsize' : 4,

            'figure.figsize' : (width_single_column, width_single_column*0.4),
           #'figure.figsize': get_figsize(300),
           'figure.subplot.left' : 0.125,
           'figure.subplot.right' : 0.95,
           'figure.subplot.bottom' : 0.1,
           'figure.subplot.top' : 0.95,
           
           'savefig.dpi' : 300,
           'figure.dpi' : 300,
           #'savefig.bbox': 'tight',
           # this will crop white spaces around images that will make
           # width/height no longer the same as the specified one.

           'legend.fontsize' : 4.5,
           'legend.frameon' : False,
           'legend.numpoints' : 1,
           'legend.handlelength' : 2,
           'legend.scatterpoints' : 1,
           'legend.labelspacing' : 0.5,
           'legend.markerscale' : 0.9,
           'legend.handletextpad' : 0.5,  # pad between handle and text
           'legend.borderaxespad' : 0.5,  # pad between legend and axes
           'legend.borderpad' : 0.5,  # pad between legend and legend content
           'legend.columnspacing' : 1,  # pad between each legend column


           'lines.linewidth' : 1,
           'lines.markersize' : 2,
           }

# single column 
sc4fParams = {'font.size': 8,
           'axes.labelsize' : 8,
           'axes.linewidth' : 1,
           'axes.labelpad' : 0.5,
           'xtick.major.size' : 2,
           'xtick.major.width' : 0.5,
           'xtick.minor.size' : 1,
           'xtick.minor.width' :0.5,
           'ytick.major.size' : 2,
           'ytick.major.width' : 0.5,
           'ytick.minor.size' : 1,
           'ytick.minor.width' : 0.5,

           #'text.fontsize' : 8,
           'xtick.labelsize' : 8,
           'ytick.labelsize' : 8,

              'figure.figsize' : (width_single_column, height_single_column*1.2),
           #'figure.figsize': get_figsize(300),
           'figure.subplot.left' : 0.125,
           'figure.subplot.right' : 0.95,
           'figure.subplot.bottom' : 0.1,
           'figure.subplot.top' : 0.95,
           
           'savefig.dpi' : 300,
           #'savefig.bbox': 'tight',
           # this will crop white spaces around images that will make
           # width/height no longer the same as the specified one.

           'legend.fontsize' : 7.5,
           'legend.frameon' : False,
           'legend.numpoints' : 1,
           'legend.handlelength' : 2,
           'legend.scatterpoints' : 1,
           'legend.labelspacing' : 0.5,
           'legend.markerscale' : 0.9,
           'legend.handletextpad' : 0.5,  # pad between handle and text
           'legend.borderaxespad' : 0.5,  # pad between legend and axes
           'legend.borderpad' : 0.5,  # pad between legend and legend content
           'legend.columnspacing' : 1,  # pad between each legend column


           'lines.linewidth' : 1,
           'lines.markersize' : 2,
           }

# single column 
sc2fParams = {'font.size': 6,
           'axes.labelsize' : 6,
           'axes.linewidth' : 1,
           'axes.labelpad' : 0.5,
           'xtick.major.size' : 2,
           'xtick.major.width' : 0.5,
           'xtick.minor.size' : 1,
           'xtick.minor.width' :0.5,
           'ytick.major.size' : 2,
           'ytick.major.width' : 0.5,
           'ytick.minor.size' : 1,
           'ytick.minor.width' : 0.5,

           #'text.fontsize' : 8,
           'xtick.labelsize' : 6,
           'ytick.labelsize' : 6,

              'figure.figsize' : (width_single_column, height_single_column*0.6),
           #'figure.figsize': get_figsize(300),
           'figure.subplot.left' : 0.125,
           'figure.subplot.right' : 0.95,
           'figure.subplot.bottom' : 0.1,
           'figure.subplot.top' : 0.95,
           
           'savefig.dpi' : 300,
           #'savefig.bbox': 'tight',
           # this will crop white spaces around images that will make
           # width/height no longer the same as the specified one.

           'legend.fontsize' : 6,
           'legend.frameon' : False,
           'legend.numpoints' : 1,
           'legend.handlelength' : 2,
           'legend.scatterpoints' : 1,
           'legend.labelspacing' : 0.5,
           'legend.markerscale' : 0.9,
           'legend.handletextpad' : 0.5,  # pad between handle and text
           'legend.borderaxespad' : 0.5,  # pad between legend and axes
           'legend.borderpad' : 0.5,  # pad between legend and legend content
           'legend.columnspacing' : 1,  # pad between each legend column


           'lines.linewidth' : 1,
           'lines.markersize' : 2,
           }

sc1c3rParams = {'font.size': 6,
           'axes.labelsize' : 4,
           'axes.linewidth' : 1,
           'axes.labelpad' : 0.2,
           'xtick.major.pad'      : 4 ,
           'ytick.major.pad'      : 4 ,
           'xtick.major.size' : 2,
           'xtick.major.width' : 0.5,
           'xtick.minor.size' : 1,
           'xtick.minor.width' :0.5,
           'ytick.major.size' : 2,
           'ytick.major.width' : 0.5,
           'ytick.minor.size' : 1,
           'ytick.minor.width' : 0.5,

           #'text.fontsize' : 8,
           'xtick.labelsize' : 4,
           'ytick.labelsize' : 4,

            'figure.figsize' : (width_single_column*0.8, width_single_column*1.2),
           #'figure.figsize': get_figsize(300),
           'figure.subplot.left' : 0.125,
           'figure.subplot.right' : 0.95,
           'figure.subplot.bottom' : 0.1,
           'figure.subplot.top' : 0.95,
           
           'savefig.dpi' : 300,
           'figure.dpi' : 300,
           #'savefig.bbox': 'tight',
           # this will crop white spaces around images that will make
           # width/height no longer the same as the specified one.

           'legend.fontsize' : 4.5,
           'legend.frameon' : False,
           'legend.numpoints' : 1,
           'legend.handlelength' : 2,
           'legend.scatterpoints' : 1,
           'legend.labelspacing' : 0.5,
           'legend.markerscale' : 0.9,
           'legend.handletextpad' : 0.5,  # pad between handle and text
           'legend.borderaxespad' : 0.5,  # pad between legend and axes
           'legend.borderpad' : 0.5,  # pad between legend and legend content
           'legend.columnspacing' : 1,  # pad between each legend column


           'lines.linewidth' : 1,
           'lines.markersize' : 2,
           }

def set_mode(mode):
    if mode == "sc":
        mpl.rcParams.update(scParams)
    elif mode == "dc":
        mpl.rcParams.update(dcParams)
    elif mode == "small":
        mpl.rcParams.update(smallParams)
    elif mode == "3f":
        mpl.rcParams.update(f3Params)
    elif mode == "sc4f":
        mpl.rcParams.update(sc4fParams)
    elif mode == "sc2f":
        mpl.rcParams.update(sc2fParams)
    elif mode == "sc1c3r":
        mpl.rcParams.update(sc1c3rParams)
