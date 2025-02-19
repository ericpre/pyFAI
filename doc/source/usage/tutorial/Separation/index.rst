:Author: Jérôme Kieffer
:Date: 07/04/2021
:Keywords: Tutorial
:Target: Scientists

.. _separate:

Signal separation
=================

The core idea is to separate Bragg-peaks from amorphous signal.
Peaks are always seen as positive outliers on top of background noise or
amorphous signal.
The calculation of the background has gradually improved over time:

Initially, it was a median filter on the azimuthal direction after a 2D intergation.
The obtained background curve was often noisy.
This median filter has been replaced by a sigma-clipping to enforce a normal
distribution of the background.
Finally the sigma-clipping has been implemented
using 1D integrators, avoiding pixel splitting and mixing together rings.

The reconstitution of the Wilson plot is also presented.

.. toctree::
   :maxdepth: 1

   Separate
   Wilson

