from data_utils import data_utils
from feature_extraction import feature_extraction

from sklearn.model_selection import train_test_split


def eval_tts(intervals, target, features_to_extract, test_size=0.2, shuffle=False):
    intervals_train, intervals_test, y_train, y_test = train_test_split(intervals, target, test_size=test_size, shuffle=shuffle)
    import pdb
    pdb.set_trace()
    
    x_train = feature_extraction.extract_features(intervals_train, features_to_extract, set_type="train", target=y_train)


intervals, target = data_utils.get_intervals(data_utils.parse_raw_data("./demo_data/S001R03.edf"), interval_len_s=2.0, overlap=0.5)

eval_tts(intervals, target, {"CSP" : dict()}, test_size=0.2, shuffle=False)


