

class DataCleaner:
    def __init__(self, df):
        self.df = df

    def clean_data(self):
        self.df = self.df.drop(columns=['id'])
        return self.df


