# CLASS_GSF: CLASS with Generalized Scalar Field

A modified version of CLASS with generalized scalar field written by Kunhao Zhong (kunhao.zhong@stonyrbook.edu). Please email me if there are any questions or mistakes.

The code is inspried by [hi-class](http://miguelzuma.github.io/hi_class_public/), which can calculate any Horndeski model using EFT. Non-conanical scalar field is a subset of Horndeski theory, but CLASS_GSF will evolve the full perturbation equations of the scalar field instead of using EFT.


## Example with dilatonic ghost field(dgf) model

Here's an example of dgf models, with its background evolution and its effect on matter power spectrum. The details about this model can be find at https://arxiv.org/abs/hep-th/0405054. 

![](https://github.com/KunhaoZhong/CLASS_GSF/blob/main/dgf_plot2.png)
![](https://github.com/KunhaoZhong/CLASS_GSF/blob/main/dgf_plot1.png)<!-- .element height="5%" width="5%" -->


## Equations used in GSF perturbation

![](https://github.com/KunhaoZhong/CLASS_GSF/blob/main/pert_eq.png)<!-- .element height="9%" width="10%" -->
The full equations that CLASS_GSF can be found in my notes. The perturbation equations are given in synchronous gauge, where I can't find it in any publication. The peturbative equations are given in Newtonian gauge by https://arxiv.org/abs/1109.1308v3. I use `Xpand` to cross check my calculations, and tested with several examples using hi-class.

Currently there are six parameters in this modification. param(0) is for model selection. parameter 1-3 is for initial condtions that people can easily choose by themselves, and parameter 5-6 is the parameters for different GSF model. Most of the k-essence models only need two parameters, but you can follow the routine to add more parameters.



## Additional features with CLASS_GSF

In this version, we add a second `gsf` called `gsf2` that allows users to have an additional scalar field. This scalar field will not be used in the shooting method that class use to satify the closre relation today(a=1), thus it can be served as an scalar field in the Early Dark Energy(EDE) model. 

On the other hand, both of the two scalar fields can be used as the scalar field Dark Matter, depending on what the user want for the description of DE.


## How to write your own GSF model
Users can modify the `gsf_functions` in the end of `background.c` module, which requires both the Lagragian and derivatives. According to the perturbation theory of GSF, no higher order term is needed to calcualte the first order perturbation. Then no other modification is required. The code will calculate the full background and perturbation evolution of the scalar field. 

It is easy to add extra parameters if needed, just follow the routine used in `gsf_parameters`.

The Python wrapper is now working with cobaya. But you may need to modify it if you want extra parameters or other sampling method (if it's too complicated in YAML file).






=============

CLASS: Cosmic Linear Anisotropy Solving System  {#mainpage}
==============================================

Authors: Julien Lesgourgues, Thomas Tram, Nils Schoeneberg

with several major inputs from other people, especially Benjamin
Audren, Simon Prunet, Jesus Torrado, Miguel Zumalacarregui, Francesco
Montanari, Deanna Hooper, Samuel Brieden, Daniel Meinert, Matteo Lucca, etc.

For download and information, see http://class-code.net


Compiling CLASS and getting started
-----------------------------------

(the information below can also be found on the webpage, just below
the download button)

Download the code from the webpage and unpack the archive (tar -zxvf
class_vx.y.z.tar.gz), or clone it from
https://github.com/lesgourg/class_public. Go to the class directory
(cd class/ or class_public/ or class_vx.y.z/) and compile (make clean;
make class). You can usually speed up compilation with the option -j:
make -j class. If the first compilation attempt fails, you may need to
open the Makefile and adapt the name of the compiler (default: gcc),
of the optimization flag (default: -O4 -ffast-math) and of the OpenMP
flag (default: -fopenmp; this flag is facultative, you are free to
compile without OpenMP if you don't want parallel execution; note that
you need the version 4.2 or higher of gcc to be able to compile with
-fopenmp). Many more details on the CLASS compilation are given on the
wiki page

https://github.com/lesgourg/class_public/wiki/Installation

(in particular, for compiling on Mac >= 10.9 despite of the clang
incompatibility with OpenMP).

To check that the code runs, type:

    ./class explanatory.ini

The explanatory.ini file is THE reference input file, containing and
explaining the use of all possible input parameters. We recommend to
read it, to keep it unchanged (for future reference), and to create
for your own purposes some shorter input files, containing only the
input lines which are useful for you. Input files must have a *.ini
extension. We provide an example of an input file containing a
selection of the most used parameters, default.ini, that you may use as a
starting point.

If you want to play with the precision/speed of the code, you can use
one of the provided precision files (e.g. cl_permille.pre) or modify
one of them, and run with two input files, for instance:

    ./class test.ini cl_permille.pre

The files *.pre are suppposed to specify the precision parameters for
which you don't want to keep default values. If you find it more
convenient, you can pass these precision parameter values in your *.ini
file instead of an additional *.pre file.

The automatically-generated documentation is located in

    doc/manual/html/index.html
    doc/manual/CLASS_manual.pdf

On top of that, if you wish to modify the code, you will find lots of
comments directly in the files.

Python
------

To use CLASS from python, or ipython notebooks, or from the Monte
Python parameter extraction code, you need to compile not only the
code, but also its python wrapper. This can be done by typing just
'make' instead of 'make class' (or for speeding up: 'make -j'). More
details on the wrapper and its compilation are found on the wiki page

https://github.com/lesgourg/class_public/wiki

Plotting utility
----------------

Since version 2.3, the package includes an improved plotting script
called CPU.py (Class Plotting Utility), written by Benjamin Audren and
Jesus Torrado. It can plot the Cl's, the P(k) or any other CLASS
output, for one or several models, as well as their ratio or percentage
difference. The syntax and list of available options is obtained by
typing 'pyhton CPU.py -h'. There is a similar script for MATLAB,
written by Thomas Tram. To use it, once in MATLAB, type 'help
plot_CLASS_output.m'

Developing the code
--------------------

If you want to develop the code, we suggest that you download it from
the github webpage

https://github.com/lesgourg/class_public

rather than from class-code.net. Then you will enjoy all the feature
of git repositories. You can even develop your own branch and get it
merged to the public distribution. For related instructions, check

https://github.com/lesgourg/class_public/wiki/Public-Contributing

Using the code
--------------

You can use CLASS freely, provided that in your publications, you cite
at least the paper `CLASS II: Approximation schemes <http://arxiv.org/abs/1104.2933>`. Feel free to cite more CLASS papers!

Support
-------

To get support, please open a new issue on the

https://github.com/lesgourg/class_public

webpage!
