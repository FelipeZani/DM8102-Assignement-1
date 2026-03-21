from gnp_generator import generate_GNP_graph 
import unittest


class GNPGraphGenerator(unittest.TestCase):
    def test_graph_generation(self,):
        S = {0 : {1}, #sample
             1:{0}} # G(2,2)
        S_prime = {1:set(),
                   2:set()}
        n = 2 #Nodes number
        sample = generate_GNP_graph(n,0.5)
        self.assertTrue(sample== S or sample==S_prime) 
        print("Passed test_graph_generation : graph was created with success ") 

    def test_noEdges_gnp_graph(self):
        n = 5
        sample = generate_GNP_graph(n,0)
        neighbours_set = sample.values()
        for neighbours in neighbours_set:
            assert len(neighbours)==0
        print("Passed test_noEdges_gnp_graph : no edges were found") 

    def test_complete_gnp_graph(self):
        n = 5
        sample = generate_GNP_graph(n,1)
        for node,neighbors in sample.items():
            self.assertEqual(len(neighbors),n-1)
            self.assertTrue(node not in neighbors)
        print("Passed test_complete_gnp_graph : Graph is completed") 


    def test_gnp_edges_size(self):
        n = 10 
        graph_edges_nb = 0
        sample = generate_GNP_graph(n,0.1)
        max_possible_edges_nb = int (n*(n-1)*0.5)
        graph_keys = list(sample.keys())
        for key in graph_keys:
            graph_edges_nb+=len(sample[key])
        self.assertTrue(graph_edges_nb<=max_possible_edges_nb)
        
        print("Passed test_gnp_edges_size : correct edge number") 
 
if __name__ == '__main__':
    
    unittest.main()
