import csv, math
class Program:
    """This class was developed to import data from a csv file into a dictionary
    and then utilize two separate dictionaries with matching keys in order to determine
    the Pearson Correlation Coefficient."""

    def Parser(self, filename, column1, column2):
        """Returns a dictionary with data (int format) from two specified columns of 
        a csv file assuming first row is a header row. Removes any k/v pairs that have 
        empty keys."""

        with open(filename, 'rb') as csvfile:
            datafile = csv.reader(csvfile, delimiter=' ', quotechar='|')
  
            # get headers of columns
            for row in csvfile.readlines():
                column = row.split(',')
                header1 = column[column1]
                header2 = column[column2]
                break
            csvfile.seek(0) # return to beginning of csv file 
            csvfile.next() # set up position in file to read data (skip header row)
   

            # storing data in dictionary
            Dict = {}
            for row in csvfile:
                column = row.split(',')
                data1 = column[column1]
                data2 = column[column2]
                Dict[(data1)] = (data2)
            if '' in Dict.keys(): #removing empty keys
                del Dict['']
            Dict = {int(k):float(v) for k, v in Dict.items()} #cast items from string to int/float
            return Dict

    def Average(self, Dict):
        """Returns the mean of a given dictionary using the values"""

        assert len(Dict) > 0 #ensure dictionary contains items
        sum=0 
        for k, v in Dict.iteritems():
            sum += v
        average= float(sum/len(Dict))
        return average

    def Pearson(self, Dict1, Dict2):
        """Returns the Pearson Correlation Coefficient given two dictionaries.
        Correlation will be determined by matching keys across the two dictionaries
        and using the corresponding value pairs for the x and y data sets."""

        n=len(Dict1)
        assert len(Dict1) == len(Dict2)
        assert n>0
        AvgPov=self.Average(Dict1)
        AvgLife= self.Average(Dict2)
        DiffProd=0
        PovDiff2=0
        LifeDiff2=0

        for k in Dict1:
            PovDiff = Dict1[k] - AvgPov
            LifeDiff = Dict2[k] - AvgLife
            DiffProd += PovDiff * LifeDiff
            PovDiff2 += PovDiff * PovDiff
            LifeDiff2 += LifeDiff * LifeDiff
        return DiffProd/math.sqrt(PovDiff2 * LifeDiff2)

if __name__ == '__main__':
    prog = Program()
    PovDict =  prog.Parser ('Health_Indicators.csv', 0, 23)
    LifeDict = prog.Parser ('Life_Expectancy.csv', 0, 8)
    print "-------------"
    print prog.Average(PovDict)
    print prog.Average(LifeDict)
    print prog.Pearson(PovDict, LifeDict)
