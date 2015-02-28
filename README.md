BASE9_PlottingResults
================================

<h3>A Python plotting tool for the results of the BASE-9 package</h3>

<br />

<h4>Table of Contents</h4>
[Summary](#Summary)<br />
[Downloading and Installation](#Install)<br />
[Example of Use](#Use)<br />
[Documentation](#Doc)<br />
[Dependencies](#Deps)<br />
[Other Information](#Other)<br />
<br /><br />


<a name="Summary"/>
<h4>Summary</h4>
====================

This repository houses two Python scripts that allow the user to easily plot results from the output of BASE-9/BASE-N single or mutliple population Bayesian analysis. The [BASE-9 package](https://github.com/argiopetech/BASE) uses Bayesian analysis techniques to determine a best fit isochrone to a cluster of stellar photometry from a set of selected theoretical models.

Each Python script contains a function written to plot all of the iterations of the adaptive Bayesian Markov Chain Monte Carlo exploration of parameter space for a cluster run with BASE-9's output format. More information about the BASE-9 program package itself and its scientific motivation can be found at the BASE-9 GitHub page as well as in the user manual available on [arxiv](http://arxiv.org/).

These plotting functions allow the user to plot each iteration of the adaptive MCMC algorithm for each parameter being sampled (e.g.: age, metallicity, distance, etc.) on the left half of the plot. The rightmost column of the plot shows the cumulative posterior distribution function (PDF) of the results. Across the entire plot, a line can be drawn for each parameter to indicate the prior value given to the MCMC algorithm. In the PDFs, lines can be drawn to indicate the median and 90% confidence intervals for the sampling (any lines may be turned off with the linewidths parameter(s) tuned to 0). The Python code will additionally print these values to the screen.


<br /> <br /><br />





<a name="Install"/>
<h4>Downloading and Installation</h4>
====================

The source code and necessary data files may all be downloaded as a zip, forked, or cloned on a local machine from the [BASE-9 Plotting Results](https://github.com/rwk506/BASE9_PlottingResults) repository.

The primary Python scripts included are **plotres_multi.py** and **plotresY.py**. The files included are:

- **BASEplot_example.py**: Provides two examples of implementing the Python code; suggested template to be adjusted for user's needs.
- **Multipop.png**: An example of an output plot from plotres_multi.py; this is produced by the BASEplot_example.py code.
- **NGC1261.multi.res**: File of output from BASE-9 multiPopMcmc used in the example code to make a plot.
- **NGC1261.single.res**: File of output from BASE-9 singlePopMcmc used in the example code to make a plot.
- **plotres_multi.py**: Main Python code for plotting results from multiPopMcmc.
- **plotresY.py**: Main Python code for plotting results from multiPopMcmc.
- **README.md**: README file.
- **Singlepop.png**: An example of an output plot from plotresY.py; this is produced by the BASEplot_example.py code.

If the user has Python and the necessary packages installed, no further installation should be required to run the code. If scripted, code may be run from outside Python with the command-line call 'python example.py' (where example is the name of the script). If inside Python, the functions plotresY() and plotres_multi() may be called following importing the necessary packages and:

    import plotres_multi.py
    import plotresY.py

Then the two functions, plotresY() and plotres_multi(), may be called as per the documentation and example provided.



<br /> <br /><br />

<a name="Use"/>
<h4>Example of Use</h4>
====================

The plotresY.py package houses the plotresY() function, which will plot the Bayesian MCMC exploration of parameter space from the results file of the BASE-9 singlePopMcmc calculations. The function requires the array of results from the imported results file (in the same order of the file columns - log(Age), Y, [Fe/H], distance modulus, absorption; it is not required import logPost). For those unfamiliar with python, the res file (e.g. the included file NGC1261.single.res) may be imported with the command:

    res_single=loadtxt('NGC1261.single.res',skiprows=1)

Where the first row is skipped as a header. The results can then be plotted using the defaults simply by:

    plotresY.plotresY(res_single)
    
Other options can be included: whether to plot lines of the prior values, whether to start at a particular iteration (e.g.: starting at startn=1000 to avoid the adaptive iterations prior to convergence), changing line styles and colors, etc. Full documentation is given in the function description. The resulting plot can either be saved:

    savefig('Singlepop.png')

or shown on screen:

    plt.show()

<br/>
The use of plotres_multi() is much the same as plotresY(). The plotres_multi.py package houses the plotres_multi() function, which will plot the Bayesian MCMC exploration of parameter space from the results file of the BASE-9 multiPopMcmc calculations. The function requires the array of results from the imported results file (in the same order of the file columns - log(Age), [Fe/H], distance modulus, absorption, YA, YB, Lambda; it is not required import logPost). For those unfamiliar with python, the res file (e.g. the included file NGC1261.multi.res) may be imported with the command:

    res_multi=loadtxt('NGC1261.multi.res',skiprows=1)

Where the first row is skipped as a header. The results can then be plotted using the defaults simply by:

    plotres_multi.plotres_multi(res_multi)
    
Other options can be included: whether to plot lines of the prior values, whether to start at a particular iteration (e.g.: starting at startn=1000 to avoid the adaptive iterations prior to convergence), changing line styles and colors, etc. Full documentation is given in the function description. The resulting plot can either be saved:

    savefig('Multipop.png')

or shown on screen:

    plt.show()

<br/>

For both plotresY() and plotres_multi(), the median 90% confidence intervals are printed for each parameter. These values are also represented by lines in the PDFs on the right portion of the plot.



<br /> <br /><br />

<a name="Docs"/>
<h4>Documentation</h4>
====================

###plotresY()###

This is a function that will take a single population output results file and plot the sampling history and resulting PDFs of the following, assuming that the results file is formatted as a matrix with columns of age, metallicity, distance, extinction, and helium.

Call signature: plotresY(res)
    
where res is the results file; this is typically loaded in a separate line as: res=loadtxt('/path/cluster_results.res',skiprows=1).

Optional keyword arguments:
    
    =========   =======================================================
    Keyword     Description
    =========   =======================================================
    priors :    default=[0,0,0,0,0] in the order of age, metallicity, distance, extinction, and helium. When the default is assumed, no lines for the priors are plotted. Whenever a value other than zero is specified, the prior for that variable is plot as a line.
    startn :    default=0; this is the starting iteration value for plotting the variables.
    color1 :    default='blue'; this is the color of the median and 90% bayesian interval lines in the PDF plots
    color2 :    default='gray'; this is the color of the histograms in the PDF plots
    color3 :    default='red'; this is the color of the prior lines across the entire plot
    ls1 :       default=':', a dotted line; this is the linestyle of the prior lines and bayesian interval lines
    lsty :      default='-', a solid line; this is the linestyle of the median bayesian interval line
    lw1 :       default=1.5; this is the linewidth of the all lines in the plot
    ms1 :       default=0.15; this is the marker size of the sampling history points
    mk :        default='ko', black points; this is the marker format of the sampling history points

Additional options for plotting colors, sizes, formats, etc. can be found in pyplot.plot() and related descriptions. Colors may take any standard HTML string descriptor (re: http://www.w3schools.com/html/html_colornames.asp).



<br/>
###plotres_multi()###

This is a function that will take a single population output results file and plot the sampling history and resulting PDFs of the following, assuming that the results file is formatted as a matrix with columns of age, metallicity, distance,  extinction, helium A, helium B, and proportion.
    
Call signature: plotres_multi(res)

where res is the results file; this is typically loaded in a separate line as: res=loadtxt('/path/cluster_results.res',skiprows=1).

Optional keyword arguments:
    =========   =======================================================
    Keyword     Description
    =========   =======================================================
    priors :    default=[0,0,0,0,0,0,0] in the order of age, metallicity, distance, extinction, helium A, helium B, and proportion. When the default is assumed, no lines for the priors are plotted. Whenever a value other than zero is specified, the prior for that variable is plot as a line.
    startn :    default=0; this is the starting iteration value for plotting the variables.
    color1 :    default='blue'; this is the color of the median and 90% bayesian interval lines in the PDF plots
    color2 :    default='gray'; this is the color of the histograms in the PDF plots
    color3 :    default='red'; this is the color of the prior lines across the entire plot
    ls1 :       default=':', a dotted line; this is the linestyle of the prior lines and bayesian interval lines
    lsty :      default='-', a solid line; this is the linestyle of the median bayesian interval line
    lw1 :       default=1.5; this is the linewidth of the all lines in the plot
    ms1 :       default=0.15; this is the marker size of the sampling history points
    mk :        default='ko', black points; this is the marker format of the sampling history points

Additional options for plotting colors, sizes, formats, etc. can be found in pyplot.plot() and related descriptions. Colors may take any standard HTML string descriptor (re: http://www.w3schools.com/html/html_colornames.asp).




<br /> <br /><br />

<a name="Deps"/>
<h4>Dependencies</h4>
====================

This Python code was written using Python 2.6 and Numpy 1.5.1, but should be compatible with many other versions (though not Python 3.0 or higher). The user may have to install the matplotlib, gridspec, and pylab packages.

Compatible with iPython Notebook (Use %run [name]).




<br /> <br /><br />

<a name="Other"/>
<h4>Other Information</h4>
====================
Author: RWK <br />
License: None, free to use and edit as people wish. <br />
Contact: May be made through GitHub. <br />


