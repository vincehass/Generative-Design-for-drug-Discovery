from clamp_common_eval.defaults import get_default_data_splits
data = get_default_data_splits(setting='Cluster')
data = get_default_data_splits(setting='Target') # or get_default_data_splits(setting='Title')
train_data_D1 = data.sample(dataset = "D1", neg_ratio = 2)     # Get D1 and Neg(1 : 2)
train_data_Albican = data.sample(dataset = "D1-177", neg_ratio = 1) # Get C. Albican and 177 Neg
train_data_D2 = data.sample(dataset = "D2", neg_ratio = 1)     # Get D2 and Neg(1 : 1)



# print(train_data_D2)

import pickle
pickle.dump(train_data_D1, open("D1train.pkl", "wb")) 
pickle.dump(train_data_Albican, open("AlbicaNtrain.pkl", "wb")) 
pickle.dump(train_data_D2, open("D2train.pkl", "wb")) 


# import pickle

# with open('D2train.pkl', 'rb') as handle:
#     b = pickle.load(handle)

# print(b)