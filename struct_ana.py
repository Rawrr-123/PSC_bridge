from anastruct import SystemElements

ss = SystemElements()

ss.add_element(location=[[0, 0], [0, 4]])
ss.add_element(location=[[0, 4], [4, 4]])
ss.add_element(location=[[4, 4], [4, 0]])
ss.add_element(location=[[4, 4], [6, 4]])

ss.add_support_hinged(node_id=1)
ss.add_support_roll(node_id=4)

ss.q_load(element_id=[2, 4], q=-10)
ss.solve()

ss.show_results()
