"""
MRMarketBasket1
"""
from mrjob.job import MRJob
from mrjob.step import MRStep

class MRMarketBasket1(MRJob):

    def configure_args(self):
        """
        Additional configuration flag to get the groceries file
    
        :return:
        """
        super(MRMarketBasket1, self).configure_args() 
    
    
    def mapper(self, _, line):
        """
        This is the mapper, it should generate pairs of items
        
        :param line: contains a transaction
        """
        # Each line is a string a,b,c     
        # Return pair key, value
        trans = line.strip().split(',')
        for i in range(len(trans)):
            for j in range(len(trans)):
                if i != j:
                    yield (trans[i], trans[j]), 1
                    
    def reducer(self, key, values):
        """
        Input is a pair of items as key and all the countings
        it has assigned
        
        Output should be at least a pair (key, new counting)
        """
        # Compute reducer here
        yield key, sum(values)
        

    def steps(self):
        return [MRStep(mapper=self.mapper,
                           reducer=self.reducer)]    


if __name__ == '__main__':
    MRMarketBasket1.run()
