
def extract_features(signals, features_to_extract, set_type, target=None):
    """
    Extract features from specified signals to obtain feature vector. The
    features to be extracted as well as additional data are specified by the features_to_extract
    dictionary that has the following form:
    TODO

    Args:
        signals (numpy.ndarray): signals (multichannel, same time values) from which to extract the features.
        features_to_extract (dict): dictionary in specified form specifying which features to extract as well
                                    as additional parameters for the feature extraction process.
        set_type (str): "train" or "test"

    Returns:
        (numpy.ndarray): obtained feature vector.
    """

    if "CSP" in features_to_extract:
        from mne.decoding import CSP
        
        if set_type == "train":
            csp = CSP(transform_into="csp_space") # TODO
            csp.fit(signals, target)
            features_to_extract["CSP"]["csp"] = csp
            trans = csp.transform(signals)
            np.array([np.log(np.var(x, axis=1)) for x in trans])


        elif set_type == "test":
            trans_res = csp.transform(signals)
            # TODO

        else:
            raise(ValueError("Invalid set_type argument value"))






