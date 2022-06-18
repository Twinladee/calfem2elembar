from indeterminatebeam import Support
from indeterminatebeam import Beam
from indeterminatebeam import PointLoadV, PointTorque, DistributedLoadV

beam = Beam(15)

a = Support(0, (1,1,1))
b = Support(5, (0,1,0))
c = Support(15, (0,1,0))

beam.add_supports(a,b,c)

load_1 = DistributedLoadV(10000, (5, 15))

beam.add_loads(load_1)
beam.analyse()

fig_1 = beam.plot_beam_external()
fig_1.show()

fig_2 = beam.plot_beam_external()
fig_2.show()

fig_3 = beam.plot_bending_moment()
fig_3.show()

fig_4 = beam.plot_deflection()
fig_4.show()

fig_6 = beam.plot_beam_diagram()
fig_6.show()

print(1)