from anastruct import SystemElements

ss = SystemElements()

ss.add_element(location=[[0, 0], [2.1, 0]])
ss.add_element(location=[[2.1, 0], [5.1, 0]])
ss.add_element(location=[[5.1, 0], [7.2, 0]])
ss.add_element(location=[[2.1, 0], [2.1, -3.05]])
ss.add_element(location=[[5.1, 0], [5.1, -3.05]])

ss.add_support_fixed(node_id=5)
ss.add_support_fixed(node_id=6)

ss.q_load(element_id=[1, 2, 3], q=-10)
ss.solve()

ss.show_bending_moment()
