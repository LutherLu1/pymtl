#=========================================================================
# SignalValue.py
#=========================================================================
# Module containing the SignalValue class.

#-------------------------------------------------------------------------
# SignalValue
#-------------------------------------------------------------------------
# Base class for value types, provides hooks used by SimulationTool.
# Any value that can be passed as a parameter to a Signal object
# (InPort, OutPort, Wire), needs to subclass SignalValue.
class SignalValue( object ):

  #-----------------------------------------------------------------------
  # Write v property
  #-----------------------------------------------------------------------
  @property
  def v( self ):
    return self

  @v.setter
  def v( self, value ):
    self.notify_sim_comb_update()
    self.write( value )

  #-----------------------------------------------------------------------
  # TEMPORARY: Backwards compatibility
  #-----------------------------------------------------------------------
  @property
  def value( self ):
    return self
  @value.setter
  def value( self, value ):
    self.notify_sim_comb_update()
    self.write( value )

  #-----------------------------------------------------------------------
  # Write n property
  #-----------------------------------------------------------------------
  @property
  def n( self ):
    return self._shadow_value

  @n.setter
  def n( self, value ):
    self.notify_sim_seq_update()
    # TODO: get raw int value or copy obj?
    # TODO: implement as shadow_write() instead and make part of ABC?
    self._shadow_value.write( value )

  #-----------------------------------------------------------------------
  # TEMPORARY: Backwards compatibility
  #-----------------------------------------------------------------------
  @property
  def next( self ):
    return self._shadow_value

  @next.setter
  def next( self, value ):
    self.notify_sim_seq_update()
    # TODO: get raw int value or copy obj?
    # TODO: implement as shadow_write() instead and make part of ABC?
    self._shadow_value.write( value )

  #-----------------------------------------------------------------------
  # flop
  #-----------------------------------------------------------------------
  # Update the value to match the _shadow_value (flop the register).
  def flop( self ):
    self.v = self._shadow_value

  #-----------------------------------------------------------------------
  # write (Abstract)
  #-----------------------------------------------------------------------
  # Abstract method, must be implemented by subclasses!
  # TODO: use abc module to create abstract method?
  def write( self, value ):
    raise NotImplementedError( "Subclasses of SignalValue must "
                               "implement the write() method!" )

  #-----------------------------------------------------------------------
  # uint (Abstract)
  #-----------------------------------------------------------------------
  # Abstract method, must be implemented by subclasses!
  # TODO: use abc module to create abstract method?
  def uint( self, value ):
    raise NotImplementedError( "Subclasses of SignalValue must "
                               "implement the uint() method!" )

  #-----------------------------------------------------------------------
  # int (Abstract)
  #-----------------------------------------------------------------------
  # Abstract method, must be implemented by subclasses!
  # TODO: use abc module to create abstract method?
  def int( self, value ):
    raise NotImplementedError( "Subclasses of SignalValue must "
                               "implement the int() method!" )

  #-----------------------------------------------------------------------
  # notify_sim_comb_update
  #-----------------------------------------------------------------------
  # Notify simulator of combinational update.
  # Another abstract method used as a hook by simulator tools.
  # Not meant to be implemented by subclasses.
  # NOTE: This approach uses closures, other methods can be found in:
  #       http://brg.csl.cornell.edu/wiki/lockhart-2013-03-18
  #       Is this the fastest approach?
  def notify_sim_comb_update( self ):
    pass

  #-----------------------------------------------------------------------
  # notify_sim_seq_update
  #-----------------------------------------------------------------------
  # Notify simulator of sequential update.
  # Another abstract method used as a hook by simulator tools.
  # Not meant to be implemented by subclasses.
  # NOTE: This approach uses closures, other methods can be found in:
  #       http://brg.csl.cornell.edu/wiki/lockhart-2013-03-18
  #       Is this the fastest approach?
  def notify_sim_seq_update( self ):
    pass

