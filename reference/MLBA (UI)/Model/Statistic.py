class Statistic:
    def __init__(self,connector=None):
        self.connector = connector
        self.lasted_df=None
    def execCCFD(self,tableName=None):
        if tableName==None:
            sql="select * from credit_dataset"
        else:
            sql = "select * from %s"%tableName
        self.df=self.connector.queryDataset(sql)
        self.lasted_df=self.df
        return self.df
    def processRealityDistribution(self):
        self.dfReality = self.df[['REALITY', 'TARGET']]
        self.dfReality = self.dfReality.groupby(['TARGET', 'REALITY']).size().unstack(fill_value=0).reset_index()

        self.dfReality['Y_percentage'] = round((self.dfReality['Y'] / (self.dfReality['Y'] + self.dfReality['N'])) * 100,2)
        self.dfReality['N_percentage'] = round((self.dfReality['N'] / (self.dfReality['Y'] + self.dfReality['N'])) * 100,2)
        self.lasted_df = self.dfReality
        return self.dfReality
    def processCarDistribution(self):
        self.dfCar = self.df[['CAR', 'TARGET']]
        self.dfCar = self.dfCar.groupby(['TARGET', 'CAR']).size().unstack(fill_value=0).reset_index()

        self.dfCar['Y_percentage'] = round((self.dfCar['Y'] / (self.dfCar['Y'] + self.dfCar['N'])) * 100,2)
        self.dfCar['N_percentage'] = round((self.dfCar['N'] / (self.dfCar['Y'] + self.dfCar['N'])) * 100,2)
        self.lasted_df = self.dfCar
        return self.dfCar
    def processGenderDistribution(self):
        self.dfGender = self.df[['GENDER', 'TARGET']]
        self.dfGender = self.dfGender.groupby(['TARGET', 'GENDER']).size().unstack(fill_value=0).reset_index()

        self.dfGender['F_percentage'] = round((self.dfGender['F'] / (self.dfGender['F'] + self.dfGender['M'])) * 100,2)
        self.dfGender['M_percentage'] = round((self.dfGender['M'] / (self.dfGender['F'] + self.dfGender['M'])) * 100,2)
        self.lasted_df = self.dfGender
        return self.dfGender
    def processYearDistribution(self,fromYear,toYear):
        self.dfYears = self.df[(self.df.YEARS_EMPLOYED >= fromYear) & (self.df.YEARS_EMPLOYED <= toYear)]
        self.dfYears =  self.dfYears.groupby(['YEARS_EMPLOYED', 'TARGET']).size().reset_index(name='Counts')
        self.lasted_df = self.dfYears
        return self.dfYears
    def processAgeDistribution(self,fromAge,toAge):
        self.dfAges = self.df[(self.df.AGE >= fromAge) & (self.df.AGE <= toAge)]
        self.dfAges = self.dfAges.groupby(['AGE','TARGET']).size().reset_index(name='Counts')
        self.lasted_df = self.dfAges
        return self.dfAges
    def processMonthDistribution(self,fromMonth,toMonth):
        self.dfMonths = self.df[(self.df.BEGIN_MONTH >= fromMonth) & (self.df.BEGIN_MONTH <= toMonth)]
        self.dfMonths = self.dfMonths.groupby(['BEGIN_MONTH','TARGET']).size().reset_index(name='Counts')
        self.lasted_df = self.dfMonths
        return self.dfMonths
    def processIncomeType(self):
        self.dfIncomeType = self.df[['INCOME_TYPE', 'TARGET']]
        self.lasted_df = self.dfIncomeType
        return self.dfIncomeType
    def processEducationType(self):
        self.dfEduType = self.df[['EDUCATION_TYPE','TARGET']]
        self.lasted_df = self.dfEduType
        return self.dfEduType
    def processFamilyType(self):
        self.dfFamilyType = self.df[['FAMILY_TYPE','TARGET']]
        self.lasted_df = self.dfFamilyType
        return self.dfFamilyType

