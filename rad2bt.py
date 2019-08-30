def rad2bt(wn,radiance):
	"""
	Computes brightness temperature given wavenumbers and radiances.
	
	 Inputs:
		wn		  wavenumbers (Nx1) in 1/cm 
	
	 Outputs:
		bt	  computed brightnes temperature (Nx1) in Kelvin
	....Adapted for Python by Von P. Walden
	                          20 January 2011
	  fundamental constants:
	"""
	from numpy import log
	
	h = 6.6260755e-34  # Planck constant in Js
	c1 = 2*h*c*c*1e8
	c2 = h*c/k*1e2
	bt = c2*wn / (log(1 + (c1*pow(wn,3)) / (radiance/1000.)))
	
	return bt