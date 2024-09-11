class Scale:
    @staticmethod
    def normalize(df):
        """
        Function for min-max Scaling a pandas DataFrame
        @param:
        Takes a pandas DataFrame: df
        Returns: a normalized DataFrame
        along with a dict containing rescaling
        coef which can be used in below function.
        """
        result = df.copy()
        param = dict()
        liste_attributs = list(df.columns[:-1])
        for feature_name in liste_attributs:
            param['max_value_'+str(feature_name)] = df[feature_name].max()
            param['min_value_'+str(feature_name)] = df[feature_name].min()
            max_value = df[feature_name].max()
            min_value = df[feature_name].min()
            result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
        return result, param

    @staticmethod
    def normalize_zscore(df):
        """
        Function for Z-score Scaling a pandas DataFrame
        @param:
        Takes a pandas DataFrame: df
        Returns: a normalized DataFrame
        along with a dict containing rescaling
        coef which can be used in below function.
        """
        result = df.copy()
        param = dict()
        liste_attributs = list(df.columns[:-1])
        for feature_name in liste_attributs:
            param['mean_'+str(feature_name)] = df[feature_name].mean()
            param['std_'+str(feature_name)] = df[feature_name].std()
            mean = df[feature_name].mean()
            std = df[feature_name].std()
            result[feature_name] = (df[feature_name] - mean) / std
        return result, param

    @staticmethod
    def denorm_zscore(normalized_df, param):
        """
        Function for rescaling a scaled DataFrame
        @param:
        Takes a pandas DataFrame and a dict output from above two functions
        Returns:
            Returns a rescaled DataFrame
        """
        liste_attributs = list(normalized_df.columns[:-1])
        for feature_name in liste_attributs:
            mean = param["mean_"+str(feature_name)]
            std = param["std_"+str(feature_name)]
            normalized_df[feature_name] = (normalized_df[feature_name] * std) + mean
        return normalized_df
